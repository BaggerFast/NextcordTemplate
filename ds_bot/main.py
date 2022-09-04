from nextcord import Intents
from nextcord.ext.commands import Bot

from ds_bot.misc import Env, Config
from ds_bot.cogs import register_all_cogs
from ds_bot.database.models import register_models


def start_bot():
    intents = Intents.default()
    intents.message_content = True

    bot = Bot(Config.CMD_PREFIX, intents=intents)

    register_all_cogs(bot)
    register_models()

    bot.run(Env.TOKEN)
