from pyrogram import Client
import config
from utils.logger import send_log

async def get_channel_info(app: Client):
    chat = await app.get_chat(config.CHANNEL)
    msg = f"📢 Channel: {chat.title}\n🆔 ID: {chat.id}"
    print(msg)
    await send_log(app, msg)

async def send_test_message(app: Client):
    await app.send_message(
        config.CHANNEL,
        "✅ Session is working. Channel is under control."
    )
    await send_log(app, "📩 Test message sent to channel")

async def add_backup_admin(app: Client):
    try:
        await app.promote_chat_member(
            config.CHANNEL,
            config.OWNER_ID,
            privileges={
                "can_manage_chat": True,
                "can_post_messages": True,
                "can_edit_messages": True,
                "can_delete_messages": True,
                "can_invite_users": True,
            },
        )
        await send_log(app, "👑 Backup admin added successfully")
    except Exception as e:
        await send_log(app, f"⚠️ Failed to add admin:\n{e}")