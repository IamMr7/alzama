#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒✯ ᥉᥆ᥙᖇᥴᥱ ᥲᥣᥲᤁᥲꪔᥲ ✯▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒✯  https://t.me/a_l_a_z_a_m_a_099   ✯▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒✯ https://t.me/damalazama ✯▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒

import random

from ᥉᥆ᥙᖇᥴᥱ ᥲᥣᥲᤁᥲꪔᥲ.plugins.play.filters import command
from pyrogram import filters
from pyrogram.types import Message

from ᥉᥆ᥙᖇᥴᥱ ᥲᥣᥲᤁᥲꪔᥲ import app
from ᥉᥆ᥙᖇᥴᥱ ᥲᥣᥲᤁᥲꪔᥲ.misc import db
from ᥉᥆ᥙᖇᥴᥱ ᥲᥣᥲᤁᥲꪔᥲ.utils.decorators import AdminRightsCheck
from ᥉᥆ᥙᖇᥴᥱ ᥲᥣᥲᤁᥲꪔᥲ.utils.inline import close_markup
from config import BANNED_USERS


@app.on_message(
    command(["shuffle", "cshuffle"]) & ~BANNED_USERS
)
@AdminRightsCheck
async def admins(Client, message: Message, _, chat_id):
    check = db.get(chat_id)
    user_mention = message.from_user.mention if message.from_user else "المشـرف"
    if not check:
        return await message.reply_text(_["queue_2"])
    try:
        popped = check.pop(0)
    except:
        return await message.reply_text(_["admin_15"], reply_markup=close_markup(_))
    check = db.get(chat_id)
    if not check:
        check.insert(0, popped)
        return await message.reply_text(_["admin_15"], reply_markup=close_markup(_))
    random.shuffle(check)
    check.insert(0, popped)
    await message.reply_text(
        _["admin_16"].format(user_mention), reply_markup=close_markup(_)
    )
