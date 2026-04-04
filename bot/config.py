"""環境変数管理"""

import os

if os.path.exists(".env"):
    from dotenv import load_dotenv

    load_dotenv()


class Config:
    DISCORD_TOKEN: str = os.getenv("DISCORD_TOKEN", "")
    QUIZ_CHANNEL_ID: str = os.getenv("QUIZ_CHANNEL_ID", "")
    QUIZ_DATA_DIR: str = os.getenv(
        "QUIZ_DATA_DIR",
        os.path.join(os.path.expanduser("~"), "hisho-bot", "data", "quiz"),
    )
    WEB_URL: str = os.getenv("WEB_URL", "https://kotohira-quiz.pages.dev")

    @classmethod
    def validate(cls) -> None:
        if not cls.DISCORD_TOKEN:
            raise ValueError("DISCORD_TOKEN が未設定です")
        if not cls.QUIZ_CHANNEL_ID:
            raise ValueError("QUIZ_CHANNEL_ID が未設定です")
