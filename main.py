import asyncio
from pyrogram import Client
import config
from utils.channel import send_test_message, add_backup_admin, get_channel_info
from utils.logger import send_log

app = Client(
    "session_controller",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    session_string=config.STRING_SESSION,
)

async def main():
    async with app:
        await send_log(app, "🔥 Connected using string session")

        try:
            await get_channel_info(app)
            await send_test_message(app)

            # ⚠️ Run only once to add backup admin
            await add_backup_admin(app)

            await send_log(app, "✅ All tasks completed successfully")

        except Exception as e:
            await send_log(app, f"❌ ERROR:\n{e}")

if __name__ == "__main__":
    asyncio.run(main())