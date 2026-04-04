"""kotohira-quiz Discord Bot — 毎朝7:00に2問投稿 + Webリンク"""

import asyncio
import json
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import discord
from discord.ext import commands, tasks

from config import Config
from daily_teaser import post_daily_teaser
from quiz_store import load_questions

JST = ZoneInfo("Asia/Tokyo")

# 二重送信防止（日付文字列を記録）
_posted_date: str = ""


class PersistentTeaserView(discord.ui.View):
    """Bot再起動後もボタンが動くPersistent View"""

    def __init__(self) -> None:
        super().__init__(timeout=None)

    @discord.ui.button(
        label="placeholder",
        style=discord.ButtonStyle.secondary,
        custom_id="teaser_persistent_placeholder",
    )
    async def _placeholder(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button,
    ) -> None:
        pass

    async def interaction_check(
        self, interaction: discord.Interaction,
    ) -> bool:
        custom_id = (
            interaction.data.get("custom_id", "")
            if interaction.data
            else ""
        )
        if not custom_id.startswith("teaser_"):
            return True

        parts = custom_id.split("_")
        if len(parts) < 3:
            return True

        question_id = parts[1]
        selected = parts[2]

        q = _find_question(question_id)
        if not q:
            await interaction.response.send_message(
                "❓ 問題データが見つかりません。",
                ephemeral=True,
            )
            return False

        correct = selected == q["answer"]
        if correct:
            msg = "✅ **正解！**"
        else:
            msg = (
                f"❌ **不正解…** "
                f"正解は **{q['answer']}**"
            )
        msg += f"\n💡 {q.get('explanation', '')}"
        await interaction.response.send_message(
            msg, ephemeral=True,
        )
        return False


def _find_question(question_id: str) -> dict | None:
    """問題IDから問題データを検索"""
    for qt in ["kotohira", "english"]:
        for q in load_questions(qt):
            if q["id"] == question_id:
                return q
    return None


class QuizBot(commands.Bot):
    def __init__(self) -> None:
        intents = discord.Intents.default()
        super().__init__(
            command_prefix="!",
            intents=intents,
            help_command=None,
        )

    async def setup_hook(self) -> None:
        self.add_view(PersistentTeaserView())
        self.check_quiz_time.start()
        print("QuizBot 起動準備中...")

    async def on_ready(self) -> None:
        print(f"QuizBot 起動完了: {self.user}")
        await self.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.playing,
                name="琴平デイリークイズ",
            )
        )

    @tasks.loop(minutes=5)
    async def check_quiz_time(self) -> None:
        """5分ごとにチェック、07:00なら投稿"""
        global _posted_date
        try:
            now = datetime.now(JST)
            diff = (now.hour * 60 + now.minute) - (7 * 60)
            if not (0 <= diff < 5):
                return

            today = now.strftime("%Y-%m-%d")
            if _posted_date == today:
                return
            _posted_date = today

            channel = self.get_channel(
                int(Config.QUIZ_CHANNEL_ID)
            )
            if not channel:
                print(
                    f"チャンネル未発見: {Config.QUIZ_CHANNEL_ID}"
                )
                _posted_date = ""
                return

            await post_daily_teaser(channel)  # type: ignore[arg-type]
            print(f"クイズ投稿完了: {today}")

        except Exception as e:
            _posted_date = ""
            print(f"クイズ投稿エラー: {e}", file=sys.stderr)

    @check_quiz_time.before_loop
    async def before_check(self) -> None:
        await self.wait_until_ready()


async def main() -> None:
    Config.validate()
    bot = QuizBot()
    await bot.start(Config.DISCORD_TOKEN)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("QuizBot を停止します")
