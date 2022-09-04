from nextcord.ext.commands import Cog, Bot


# todo: UserCogs
class __MainUserCog(Cog):

    def __init__(self, bot: Bot):
        self.bot = bot


def register_user_cogs(bot: Bot) -> None:
    bot.add_cog(__MainUserCog(bot))
