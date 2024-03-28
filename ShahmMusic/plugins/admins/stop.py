#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒✯ ᥉᥆ᥙᖇᥴᥱ ᥲᥣᥲᤁᥲꪔᥲ ✯▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒✯  https://t.me/a_l_a_z_a_m_a_099   ✯▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒✯ https://t.me/damalazama ✯▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒

from ᥉᥆ᥙᖇᥴᥱ ᥲᥣᥲᤁᥲꪔᥲ.plugins.play.filters import command
from pyrogram import filters
from pyrogram.types import Message

from ᥉᥆ᥙᖇᥴᥱ ᥲᥣᥲᤁᥲꪔᥲ import app
from ᥉᥆ᥙᖇᥴᥱ ᥲᥣᥲᤁᥲꪔᥲ.core.call import Zelzaly
from ᥉᥆ᥙᖇᥴᥱ ᥲᥣᥲᤁᥲꪔᥲ.utils.database import set_loop
from ᥉᥆ᥙᖇᥴᥱ ᥲᥣᥲᤁᥲꪔᥲ.utils.decorators import AdminRightsCheck
from ᥉᥆ᥙᖇᥴᥱ ᥲᥣᥲᤁᥲꪔᥲ.utils.inline import close_markup
from config import BANNED_USERS


@app.on_message(
    command(["/stop", "اسكت", "انهاء", "ايقاف"]) & ~BANNED_USERS
)
@AdminRightsCheck
async def stop_music(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return
    await Zelzaly.stop_stream(chat_id)
    await set_loop(chat_id, 0)
    user_mention = message.from_user.mention if message.from_user else "المشـرف"
    await message.reply_text(
        _["admin_5"].format(user_mention), reply_markup=close_markup(_)
    )
