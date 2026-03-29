from pyrogram import Client
import config

async def send_log(app: Client, text: str):
    """
    Send logs to your Telegram group (LOG_GROUP_ID).
    """
    try:
        await app.send_message(
            config.LOG_GROUP_ID,
            f"📜 **LOG**\n\n{text}"
        )
    except Exception as e:
        print(f"[LOGGER ERROR] {e}")