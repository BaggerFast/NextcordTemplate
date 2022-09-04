from nextcord.ext.commands import Bot

from ds_bot.cogs.admin import register_admin_cogs
from ds_bot.cogs.other import load_other_cogs
from ds_bot.cogs.user import register_user_cogs


def register_all_cogs(bot: Bot) -> None:
    cogs = (
        register_user_cogs,
        register_admin_cogs,
        load_other_cogs,
    )
    for cog in cogs:
        cog(bot)
