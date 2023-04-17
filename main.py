import os
from pyrogram import Client, filters 
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import CallbackQuery
import random
import datetime
from pyrogram.errors import UserNotParticipant

SOULTG = Client(
    "ST-Info-Bot",
    bot_token=os.environ.get("BOT_TOKEN"),
    api_hash=os.environ.get("API_HASH"),
    api_id=int(os.environ.get("API_ID"))
)

force_channel = "SoulTechiezz"

START_MSG = """ Hello {},
I AM A POWERFUL TELEGRAM BOT TO GIVE INFORMATIONS TO YOU...😎
    
IT IS EASY TO USE ME JUST HIT HERE /help ...
    
I WILL SEND YOU INFORMATION WHAT YOU WANT. LET'S ENJOY...😍"""
    
HELP_MSG = """Hello,

Bot Commands
----------------
/start - Check I am alive.
/help  - To view this help section.
/about - About me.
/info  - Information About You.
/id    - Your User ID

@SoulTechiezz"""
    
ABOUT_MSG = """
🤖 NAME      - ST INFO BOT
👨‍💻 CREATOR   - [THIS PERSON](https://github.com/SOULTG/)
✏ LANGUAGE   - [PYTHON](www.python.org)
📕 FRAMEWORK  - [PYROGRAM](www.pyrogram.org)
📢 UPDATES    - [SOUL TECHIEZZ](t.me/SoulTechiezz)
👥 SUPPORT    - [SUPPORT GROUP](t.me/SoulTechiezzSupport)
💡 SOURCE CODE - [CLICK ME](https://github.com/SOULTG/ST-Info-Bot)
"""
    
PICS = [
 "https://telegra.ph/file/9e126bf7a3f665c66e5bc.jpg",
 "https://telegra.ph/file/2e855495d0e61ddfd9278.jpg",
 "https://telegra.ph/file/fa20fdd1fe520ca081a94.jpg",
 "https://telegra.ph/file/2fac2a130eb6313b79ad0.jpg",
 "https://telegra.ph/file/fb9e9676ca01c6052808a.jpg",
 "https://telegra.ph/file/03b0f392dd0658276e834.jpg",
 "https://telegra.ph/file/0d952075a7c56896b7dcf.jpg",
 "https://telegra.ph/file/c3317c8a72142f96e5aa2.jpg",
 "https://telegra.ph/file/81698b182a00a97697a22.jpg",
 "https://telegra.ph/file/93a1a4a50a1e3c3de3ddd.jpg",
 "https://telegra.ph/file/9b11ac6d5532f8477d5a1.jpg",
 "https://telegra.ph/file/a703f3ca0a01c804a4b52.jpg",
 "https://telegra.ph/file/ecb5aaeb78905afcb6737.jpg",
 "https://telegra.ph/file/79a8aceffd57df6c398b7.jpg",
 "https://telegra.ph/file/a160ba0221d7595b06846.jpg"
]

@SOULTG.on_message(filters.private & filters.command("start"))
async def start(client, message):
    if force_channel:
        try:
            user = await client.get_chat_member(force_channel, message.from_user.id)
            if user.status == "kicked out":
                await message.reply_text("You Are Banned")
                return
        except UserNotParticipant :
            await message.reply_text(
                text="PLEASE SUBSCRIBE MY CHANNEL TO USE ME",
                reply_markup=InlineKeyboardMarkup( [[
                 InlineKeyboardButton("🤖 JOIN UPDATES CHANNEL 🤖", url=f"t.me/{force_channel}")
                 ]]
                 )
            )
            return
    await message.reply_photo(
        photo=random.choice(PICS),
        caption=START_MSG.format(message.from_user.mention),
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("🤖 JOIN UPDATES CHANNEL 🤖", url="t.me/SoulTechiezz"),
            ],[
            InlineKeyboardButton("CREATOR 👨‍💻", url="www.github.com/SOULTG"),
            InlineKeyboardButton("SUPPORT 👥", url="t.me/SoulTechiezzSupport")
            ]]
            )
    )


@SOULTG.on_message(filters.private & filters.command("help"))
async def help(client, message):
    await message.reply_photo(
        photo=random.choice(PICS),
        caption=HELP_MSG,
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("🤖 JOIN UPDATES CHANNEL 🤖", url="t.me/SoulTechiezz"),
            ],[
            InlineKeyboardButton("CREATOR 👨‍💻", url="www.github.com/SOULTG"),
            InlineKeyboardButton("SUPPORT 👥", url="t.me/SoulTechiezzSupport")
            ]]
            )
    )


@SOULTG.on_message(filters.private & filters.command("about"))
async def about(client, message):
    await message.reply_photo(
        photo=random.choice(PICS),
        caption=ABOUT_MSG,
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("🤖 JOIN UPDATES CHANNEL 🤖", url="t.me/SoulTechiezz"),
            ],[
            InlineKeyboardButton("CREATOR 👨‍💻", url="www.github.com/SOULTG"),
            InlineKeyboardButton("SUPPORT 👥", url="t.me/SoulTechiezzSupport")
            ]]
            )
    )

@SOULTG.on_message(filters.private & filters.command("info"))
async def info(client, update):
    await update.reply_photo(
        photo=random.choice(PICS),
        caption=f"""--**Information**--

**🙋🏻‍♂️ First Name :** {update.from_user.mention}
**🧖‍♂️ Your Second Name :** {update.from_user.last_name if update.from_user.last_name else 'None'}
**🧑🏻‍🎓 Your Username :** {update.from_user.username}
**🆔 Your Telegram ID : {update.from_user.id}
**🔗 Your Profile Link :** {update.from_user.mention}""",
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("🤖 JOIN UPDATES CHANNEL 🤖", url="t.me/SoulTechiezz"),
            ],[
            InlineKeyboardButton("CREATOR 👨‍💻", url="www.github.com/SOULTG"),
            InlineKeyboardButton("SUPPORT 👥", url="t.me/SoulTechiezzSupport")
            ]]
            )
    )
        



@SOULTG.on_message(filters.private & filters.command("id"))
async def id(client, message):
    await message.reply_text(        
        text=f"**Your ID :** {message.from_user.id}",
        disable_web_page_preview=True,
    )


print("Bot Started!")

SOULTG.run()
