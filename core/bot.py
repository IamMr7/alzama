#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒✯ ᥉᥆ᥙᖇᥴᥱ ᥲᥣᥲᤁᥲꪔᥲ ꪔᥙ᥉Ꭵᥴ ✯▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒✯  https://t.me/a_l_a_z_a_m_a_099   ✯▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒✯ https://t.me/a_l_a_z_a_m_a_099 ✯▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒

from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus, ParseMode

import config

from ..logging import LOGGER


class Zelzaly(Client):
    def __init__(self):
        LOGGER("᥉᥆ᥙᖇᥴᥱ ᥲᥣᥲᤁᥲꪔᥲ ꪔᥙ᥉Ꭵᥴ").info(f"جارِ بدء تشغيل البوت . . .")
        super().__init__(
            name="ZelzalMusic",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            parse_mode=ParseMode.HTML,
            max_concurrent_transmissions=7,
        )

    async def start(self):
        await super().start()
        self.id = self.me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.username = self.me.username
        self.mention = self.me.mention

        try:
            await self.send_message(
                chat_id=config.LOGGER_ID,
                text=f"<u><b>» تم تشغيل الميـوزك لـ البوت {self.mention} ✅ :</b><u>\n\n- ɪᴅ : <code>{self.id}</code>\n- ɴᴀᴍᴇ : {self.name}\n- ᴜsᴇʀɴᴀᴍᴇ : @{self.username}",
            )
        except (errors.ChannelInvalid, errors.PeerIdInvalid):
            LOGGER(__name__).error(
                "» قم باضافة البـوت مشـرفـاً بكافة الصلاحيات في مجموعـة السجـل"
            )
            exit()
        except Exception as ex:
            LOGGER(__name__).error(
                f"Bot has failed to access the log group/channel.\n  Reason : {type(ex).__name__}."
            )
            exit()

        a = await self.get_chat_member(config.LOGGER_ID, self.id)
        if a.status != ChatMemberStatus.ADMINISTRATOR:
            LOGGER(__name__).error(
                "» قم برفـع البـوت مشـرفـاً بكافة الصلاحيات في مجموعـة السجـل"
            )
            exit()
        LOGGER("᥉᥆ᥙᖇᥴᥱ ᥲᥣᥲᤁᥲꪔᥲ ꪔᥙ᥉Ꭵᥴ").info(f" تم بدء تشغيل البوت {self.name} ...✓")

    async def stop(self):
        await super().stop()
