import os
from pyrogram import Client, filters 
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import CallbackQuery
import random
import datetime
from pyrogram.errors import UserNotParticipant

HK = Client(
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
👨‍💻 CREATOR   - [THIS PERSON](t.me/TheEvil_HK)
✏ LANGUAGE   - [PYTHON](www.python.org)
📕 FRAMEWORK  - [PYROGRAM](www.pyrogram.org)
📢 UPDATES    - [SOUL TECHIEZZ](t.me/SoulTechiezz)
👥 SUPPORT    - [SUPPORT GROUP](t.me/SoulTechiezzSupport)
💡 SOURCE CODE - [CLICK ME](https://github.com/MREVILHK/ST-Info-Bot)
"""
    
PICS = [
 "https://telegra.ph/file/af70e7dc00143bfb02a9b.jpg",
 "https://telegra.ph/file/d5844d488b9f87037f91d.jpg",
 "https://telegra.ph/file/93c7fdd8366b1b803902c.jpg",
 "https://telegra.ph/file/6ada2cada4ced48da2f58.jpg",
 "https://telegra.ph/file/9ecd114ca46245b12778a.jpg",
 "https://telegra.ph/file/be41355a8b68a4763273d.jpg",
 "https://telegra.ph/file/feaf2dac1e87d70892175.jpg",
 "https://telegra.ph/file/76fdc5f660c66ccb1e91e.jpg",
 "https://telegra.ph/file/e883cc5ec5111ff8752d4.jpg",
 "https://telegra.ph/file/cccc78224dca8951d006b.jpg",
 "https://telegra.ph/file/be562b3308796b4fc42ff.jpg"
]

@HK.on_message(filters.private & filters.command("start"))
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
            InlineKeyboardButton("CREATOR 👨‍💻", url="t.me/TheEvil_HK"),
            InlineKeyboardButton("SUPPORT 👥", url="t.me/SoulTechiezzSupport")
            ]]
            )
    )


@HK.on_message(filters.private & filters.command("help"))
async def help(client, message):
    await message.reply_photo(
        photo=random.choice(PICS),
        caption=HELP_MSG,
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("🤖 JOIN UPDATES CHANNEL 🤖", url="t.me/SoulTechiezz"),
            ],[
            InlineKeyboardButton("CREATOR 👨‍💻", url="t.me/TheEvil_HK"),
            InlineKeyboardButton("SUPPORT 👥", url="t.me/SoulTechiezzSupport")
            ]]
            )
    )


@HK.on_message(filters.private & filters.command("about"))
async def about(client, message):
    await message.reply_photo(
        photo=random.choice(PICS),
        caption=ABOUT_MSG,
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("🤖 JOIN UPDATES CHANNEL 🤖", url="t.me/SoulTechiezz"),
            ],[
            InlineKeyboardButton("CREATOR 👨‍💻", url="t.me/TheEvil_HK"),
            InlineKeyboardButton("SUPPORT 👥", url="t.me/SoulTechiezzSupport")
            ]]
            )
    )

@HK.on_message(filters.private & filters.command("info"))
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
            InlineKeyboardButton("CREATOR 👨‍💻", url="t.me/TheEvil_HK"),
            InlineKeyboardButton("SUPPORT 👥", url="t.me/SoulTechiezzSupport")
            ]]
            )
    )

        



@HK.on_message(filters.private & filters.command("id"))
async def id(client, message):
    await message.reply_text(        
        text=f"**Your ID :** {message.from_user.id}",
        disable_web_page_preview=True,
    )


print("Bot Started!")

SOULTG.run()
