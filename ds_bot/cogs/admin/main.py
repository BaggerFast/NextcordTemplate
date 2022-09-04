from nextcord.ext.commands import Cog, Bot


# todo: AdminCogs
class __MainAdminCog(Cog):

    def __init__(self, bot: Bot):
        self.bot = bot


def register_admin_cogs(bot: Bot) -> None:
    bot.add_cog(__MainAdminCog(bot))
