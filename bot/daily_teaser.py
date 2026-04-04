"""毎朝2問（琴平1 + 英語1）をボタン回答付きで個別投稿 + Webリンク"""

import discord

from config import Config
from quiz_store import select_questions


class SingleAnswerView(discord.ui.View):
    """1問分の4択ボタンView"""

    def __init__(self, q: dict) -> None:
        super().__init__(timeout=86400)
        self.q = q

        choices = q.get("choices", [])
        labels = ["A", "B", "C", "D"]
        for i, label in enumerate(labels):
            if i < len(choices):
                text = choices[i].split(". ", 1)[1] if ". " in choices[i] else choices[i]
                btn = discord.ui.Button(
                    label=f"{label}. {text}",
                    style=discord.ButtonStyle.secondary,
                    custom_id=f"teaser_{q['id']}_{label}",
                )
                btn.callback = self._make_cb(label)
                self.add_item(btn)

    def _make_cb(self, selected: str):  # noqa: ANN202
        async def callback(
            interaction: discord.Interaction,
        ) -> None:
            correct = selected == self.q["answer"]
            if correct:
                msg = "✅ **正解！**"
            else:
                msg = (
                    f"❌ **不正解…** "
                    f"正解は **{self.q['answer']}**"
                )
            msg += f"\n💡 {self.q.get('explanation', '')}"
            await interaction.response.send_message(
                msg, ephemeral=True,
            )

        return callback


async def post_daily_teaser(
    channel: discord.TextChannel,
) -> None:
    """チャンネルに琴平1問 + 英単語1問を個別投稿"""
    kotohira = select_questions("kotohira", count=1)
    english = select_questions("english", count=1)

    if not kotohira and not english:
        await channel.send(
            "⚠️ 出題可能な問題がありません。"
        )
        return

    # === 琴平町クイズ ===
    if kotohira:
        q = kotohira[0]
        embed = discord.Embed(
            title="🏛️ 琴平町クイズ",
            description=q["question"],
            color=0xD4A574,
        )
        view = SingleAnswerView(q)
        await channel.send(embed=embed, view=view)

    # === 英単語クイズ ===
    if english:
        q = english[0]
        pattern = q.get("pattern", "en_to_ja")
        tag = "英→日" if pattern == "en_to_ja" else "日→英"
        embed = discord.Embed(
            title=f"🔤 英単語クイズ ・ {tag}",
            description=q["question"],
            color=0x5B8DEF,
        )
        view = SingleAnswerView(q)
        await channel.send(embed=embed, view=view)

    # === Webリンク ===
    await channel.send(
        f"📝 **残り8問はWebで！** → {Config.WEB_URL}"
    )
