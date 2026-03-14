import asyncio
from telegram import Bot
from config import TOKEN, CHAT_ID

bot = Bot(token=TOKEN)

async def send_signal(text):
    await bot.send_message(
        chat_id=CHAT_ID,
        text=text
    )

async def main():

    while True:

        text = """
ULTRA SMC SNIPER V7

PAIR: BTC/USD
TYPE: BUY

ENTRY: 65000
SL: 64500
TP: 66500
RR: 1:3
"""

        await send_signal(text)

        await asyncio.sleep(300)  # 5 minut

asyncio.run(main())
