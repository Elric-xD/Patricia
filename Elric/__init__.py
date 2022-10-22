import os
print("[INFO] Starting Pyrogram Client!")

pbot = Client('bot', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, plugins=dict(root=f"{__name__}/plugins"))

print("[INFO] Pyrogram Client Started Successfully")

print("[INFO] Starting Telethon Client!")

telethon = TelegramClient('innexia', api_id=API_ID, api_hash=API_HASH)

tbot = telethon.start(bot_token=BOT_TOKEN)

print("[INFO] Telethon Client Started!")

updater = tg.Updater(BOT_TOKEN, workers=8, use_context=True)

dispatcher = updater.dispatcher



