#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒✯ ᥉᥆ᥙᖇᥴᥱ ᥲᥣᥲᤁᥲꪔᥲ ✯▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒✯  https://t.me/a_l_a_z_a_m_a_099   ✯▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒✯ https://t.me/damalazama ✯▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒

from ᥉᥆ᥙᖇᥴᥱ ᥲᥣᥲᤁᥲꪔᥲ.plugins.play.filters import command
from pyrogram import filters

from ᥉᥆ᥙᖇᥴᥱ ᥲᥣᥲᤁᥲꪔᥲ import app
from ᥉᥆ᥙᖇᥴᥱ ᥲᥣᥲᤁᥲꪔᥲ.misc import SUDOERS
from ᥉᥆ᥙᖇᥴᥱ ᥲᥣᥲᤁᥲꪔᥲ.utils.database import add_off, add_on
from ᥉᥆ᥙᖇᥴᥱ ᥲᥣᥲᤁᥲꪔᥲ.utils.decorators.language import language


@app.on_message(command(["السجل"]) & SUDOERS)
@language
async def logger(client, message, _):
    usage = _["log_1"]
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip().lower()
    if state == "تفعيل":
        await add_on(2)
        await message.reply_text(_["log_2"])
    elif state == "تعطيل":
        await add_off(2)
        await message.reply_text(_["log_3"])
    else:
        await message.reply_text(usage)
