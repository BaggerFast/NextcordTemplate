from nextcord.ext.commands import Bot, Cog, Context


# todo: OtherCogs
class __MainOtherCog(Cog):

    def __init__(self, bot: Bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self) -> None:
        print('I am ready!!!')


def register_other_cogs(bot: Bot) -> None:
    bot.add_cog(__MainOtherCog(bot))
