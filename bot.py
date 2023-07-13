from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import filters, Client, errors, enums
from pyrogram.errors import UserNotParticipant
from pyrogram.errors.exceptions.flood_420 import FloodWait
from database import add_user, add_group, all_users, all_groups, users, remove_user
from configs import cfg
import random, asyncio

app = Client(
    "approver",
    api_id=cfg.API_ID,
    api_hash=cfg.API_HASH,
    bot_token=cfg.BOT_TOKEN
)

gif = [
    'https://te.legra.ph/file/17cba675fe3c88987494e.jpg',
    'https://te.legra.ph/file/17cba675fe3c88987494e.jpg',
    'https://te.legra.ph/file/17cba675fe3c88987494e.jpg',
]


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Main process ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_chat_join_request(filters.group | filters.channel & ~filters.private)
async def approve(_, m : Message):
    op = m.chat
    kk = m.from_user
    try:
        add_group(m.chat.id)
        await app.approve_chat_join_request(op.id, kk.id)
        img = random.choice(gif)
        await app.send_video(kk.id,img, "**Hello {}!\nWelcome To {}\n\n__Powerd By : @AMBOTYT__**".format(m.from_user.mention, m.chat.title))
        add_user(kk.id)
    except errors.PeerIdInvalid as e:
        print("user isn't start bot(means group)")
    except Exception as err:
        print(str(err))    
 
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Start ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("start"))
async def op(_, m :Message):
    try:
        await app.get_chat_member(cfg.CHID, m.from_user.id) 
        if m.chat.type == enums.ChatType.PRIVATE:
            keyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("💕 ᴄʜᴀɴɴᴇʟ", url="https://t.me/RadhaX2Support"),
                        InlineKeyboardButton("💕 ꜱᴜᴘᴘᴏʀᴛ", url="https://t.me/RadhaX2Support")
                    ],[
                        InlineKeyboardButton("🥺 ᴀᴅᴅ ᴍᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ", url="https://t.me/Auto_approveRobot?startgroup")
                    ]
                ]
            )
            add_user(m.from_user.id)
            await m.reply_photo("https://te.legra.ph/file/2c54beb88a7f260ceb2ce.jpg", caption="**🦊 ʜᴇʟʟᴏ {}!\nɪ'ᴍ ᴀɴ ᴀᴜᴛᴏ ᴀᴩᴩʀᴏᴠᴇ [ᴀᴅᴍɪɴ ᴊᴏɪɴ ʀᴇqᴜᴇꜱᴛꜱ]({}) ʙᴏᴛ.\nɪ ᴄᴀɴ ᴀᴩᴩʀᴏᴠᴇ ᴜꜱᴇʀꜱ ɪɴ ɢʀᴏᴜᴩꜱ/ᴄʜᴀɴɴᴇʟꜱ.ᴀᴅᴅ ᴍᴇ ᴛᴏ yᴏᴜʀ ᴄʜᴀᴛ ᴀɴᴅ ᴩʀᴏᴍᴏᴛᴇ ᴍᴇ ᴛᴏ ᴀᴅᴍɪɴ ᴡɪᴛʜ ᴀᴅᴅ ᴍᴇᴍʙᴇʀꜱ ᴩᴇʀᴍɪꜱꜱɪᴏɴ.\n\n__ Pᴏᴡᴇʀᴅ ʙy : @GhostRadha__**".format(m.from_user.mention, "https://t.me/telegram/153"), reply_markup=keyboard)
    
        elif m.chat.type == enums.ChatType.GROUP or enums.ChatType.SUPERGROUP:
            keyboar = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("💁‍♂️ Start me private 💁‍♂️", url="https://t.me/Autoapprove2_bot?start=start")
                    ]
                ]
            )
            add_group(m.chat.id)
            await m.reply_text("**🦊 ʜᴇʟʟᴏ {}!\nᴡʀɪᴛᴇ ᴍᴇ ᴩʀɪᴠᴀᴛᴇ ꜰᴏʀ ᴍᴏʀᴇ ᴅᴇᴛᴀɪʟꜱ**".format(m.from_user.first_name), reply_markup=keyboar)
        print(m.from_user.first_name +" Is started Your Bot!")

    except UserNotParticipant:
        key = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🍀 Check Again 🍀", "chk")
                ]
            ]
        )
        await m.reply_text("**⚠️ᴀᴄᴄᴇꜱꜱ ᴅᴇɴɪᴇᴅ!⚠️\n\nᴩʟᴇᴀꜱᴇ ᴊᴏɪɴ @{} ᴛᴏ ᴜꜱᴇ ᴍᴇ.ɪꜰ yᴏᴜ ᴊᴏɪɴᴇᴅ ᴄʟɪᴄᴋ ᴄʜᴇᴄᴋ ᴀɢᴀɪɴ ʙᴜᴛᴛᴏɴ ᴛᴏ confirm.**".format(cfg.FSUB), reply_markup=key)

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ callback ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_callback_query(filters.regex("chk"))
async def chk(_, cb : CallbackQuery):
    try:
        await app.get_chat_member(cfg.CHID, cb.from_user.id)
        if cb.message.chat.type == enums.ChatType.PRIVATE:
            keyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("💕 ᴄʜᴀɴɴᴇʟ", url="https://t.me/RadhaX2Update"),
                        InlineKeyboardButton("💕 ꜱᴜᴘᴘᴏʀᴛ", url="https://t.me/RadhaX2Support")
                    ],[
                        InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ", url="https://t.me/Autoapprove2_bot?startgroup")
                    ]
                ]
            )
            add_user(cb.from_user.id)
            await cb.message.edit("**🦊 ʜᴇʟʟᴏ {}!\nɪ'ᴍ ᴀɴ ᴀᴜᴛᴏ ᴀᴩᴩʀᴏᴠᴇ [ᴀᴅᴍɪɴ ᴊᴏɪɴ ʀᴇqᴜᴇꜱᴛꜱ]({}) ʙᴏᴛ.\nɪ ᴄᴀɴ ᴀᴩᴩʀᴏᴠᴇ ᴜꜱᴇʀꜱ ɪɴ ɢʀᴏᴜᴩꜱ/ᴄʜᴀɴɴᴇʟꜱ.ᴀᴅᴅ ᴍᴇ ᴛᴏ yᴏᴜʀ ᴄʜᴀᴛ ᴀɴᴅ ᴩʀᴏᴍᴏᴛᴇ ᴍᴇ ᴛᴏ ᴀᴅᴍɪɴ ᴡɪᴛʜ ᴀᴅᴅ ᴍᴇᴍʙᴇʀꜱ ᴩᴇʀᴍɪꜱꜱɪᴏɴ.\n\n__ Pᴏᴡᴇʀᴅ ʙy : @GhostRadha__**".format(cb.from_user.mention, "https://t.me/telegram/153"), reply_markup=keyboard, disable_web_page_preview=True)
        print(cb.from_user.first_name +" Is started Your Bot!")
    except UserNotParticipant:
        await cb.answer("🙅‍♂️ yᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴊᴏɪɴᴇᴅ ᴛᴏ ᴄʜᴀɴɴᴇʟ ᴊᴏɪɴ ᴀɴᴅ ᴛʀy ᴀɢᴀɪɴ. 🙅‍♂️")

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ info ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("users") & filters.user(cfg.SUDO))
async def dbtool(_, m : Message):
    xx = all_users()
    x = all_groups()
    tot = int(xx + x)
    await m.reply_text(text=f"""
🍀 Chats Stats 🍀
🙋‍♂️ Users : `{xx}`
👥 Groups : `{x}`
🚧 Total users & groups : `{tot}` """)

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Broadcast ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("bcast") & filters.user(cfg.SUDO))
async def bcast(_, m : Message):
    allusers = users
    lel = await m.reply_text("`⚡️ ᴩʀᴏᴄᴇꜱꜱɪɴɢ...`")
    success = 0
    failed = 0
    deactivated = 0
    blocked = 0
    for usrs in allusers.find():
        try:
            userid = usrs["user_id"]
            #print(int(userid))
            if m.command[0] == "bcast":
                await m.reply_to_message.copy(int(userid))
            success +=1
        except FloodWait as ex:
            await asyncio.sleep(ex.value)
            if m.command[0] == "bcast":
                await m.reply_to_message.copy(int(userid))
        except errors.InputUserDeactivated:
            deactivated +=1
            remove_user(userid)
        except errors.UserIsBlocked:
            blocked +=1
        except Exception as e:
            print(e)
            failed +=1

    await lel.edit(f"✅ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟ ᴛᴏ `{success}` ᴜꜱᴇʀꜱ.\n❌ ꜰᴀɪʟᴅ ᴛᴏo `{failed}` ᴜꜱᴇʀꜱ.\n👾 ꜰᴏᴜɴᴅ `{blocked}` Blocked users \n👻 Found `{deactivated}` ᴅᴇᴀᴄᴛɪᴠᴀᴛᴇᴅ ᴜꜱᴇʀꜱ.")

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Broadcast Forward ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("fcast") & filters.user(cfg.SUDO))
async def fcast(_, m : Message):
    allusers = users
    lel = await m.reply_text("`⚡️ ᴩʀᴏᴄᴇꜱꜱɪɴɢ...`")
    success = 0
    failed = 0
    deactivated = 0
    blocked = 0
    for usrs in allusers.find():
        try:
            userid = usrs["user_id"]
            #print(int(userid))
            if m.command[0] == "fcast":
                await m.reply_to_message.forward(int(userid))
            success +=1
        except FloodWait as ex:
            await asyncio.sleep(ex.value)
            if m.command[0] == "fcast":
                await m.reply_to_message.forward(int(userid))
        except errors.InputUserDeactivated:
            deactivated +=1
            remove_user(userid)
        except errors.UserIsBlocked:
            blocked +=1
        except Exception as e:
            print(e)
            failed +=1

    await lel.edit(f"✅ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟ ᴛᴏ `{success}` ᴜꜱᴇʀꜱ.\n❌ ꜰᴀɪʟᴅ ᴛᴏo `{failed}` ᴜꜱᴇʀꜱ.\n👾 ꜰᴏᴜɴᴅ `{blocked}` Blocked users \n👻 Found `{deactivated}` ᴅᴇᴀᴄᴛɪᴠᴀᴛᴇᴅ ᴜꜱᴇʀꜱ.")

print("ɪ'ᴍ ᴀʟɪᴠᴇ ɴᴏᴡ!")
app.run()
