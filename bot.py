from telegram import Bot
from config import TOKEN,CHAT_ID

bot = Bot(token=TOKEN)

async def send_signal(text,img):

    await bot.send_photo(
        chat_id=CHAT_ID,
        photo=open(img,"rb"),
        caption=text
    )
