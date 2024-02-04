# (c) @PremiumBotz https://telegram.me/premiumbotz
import random
import asyncio
from pyrogram import Client
from pyrogram.errors import FloodWait
from config import Config


premiumbotz = Client("Join Telegram @PremiumBotz", api_id=Config.API_ID, api_hash=Config.API_HASH, session_string=Config.SESSION_STRING, in_memory=True, no_updates=True)


async def main():
        await premiumbotz.start()
        print(f"Userbot [@{premiumbotz.me.username}] started!")
        messages = [Config.MESSAGE1, Config.MESSAGE2, Config.MESSAGE3, Config.MESSAGE4, Config.MESSAGE5]
        chats = Config.TARGET_GROUPS
        while True:
            for chat in chats:
                index = random.randint(0, len(messages)-1)
                text = messages[index]
                try:
                    await premiumbotz.send_message(chat_id=chat, text=text)
                except FloodWait as t:
                    print(f"Floodwait {t.value}s")
                    await asyncio.sleep(t.value)
                    await premiumbotz.send_message(chat_id=chat, text=text)
                except Exception as e:
                    print(f"chat: @{chat} - {e}")
            await asyncio.sleep(120)
        #await premiumbotz.stop()
    
        
premiumbotz.run(main())  
