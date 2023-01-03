import discord
from discord.ext import commands 
import config

intents = discord.Intents.all() # Always use intents
bot = commands.Bot(command_prefix="u!", intents=intents)
presence = discord.Streaming(
    name="Run", 
    twitch_name="Someone", 
    platform="Twitch", 
    url="https://github.com", 
    game="game"
    ) # Bot presence

# event
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=presence) # apply presence
    print(f"Well done, Im {bot.user.name}. Lets gooo.") # very good 
    try:
        # synchronization for slash commands
        sync = await bot.tree.sync()
        print(f"synced with {len(sync)} slash commands.")
    except Exception as e:
        print(e) # maybe error
    
@bot.hybrid_command(name="say", description="I repeat your words...") # First slash command. Say 
async def say(ctx, *, arg): 
    await ctx.send(arg)


@bot.hybrid_command(name="avatar", description="Show any avatar")
async def avatar(ctx, avatar: discord.Member=None):
    if avatar == None:
        await ctx.send(f'Avatar of **{ctx.author}** {ctx.author.display_avatar}')
    else:
        await ctx.send(f'Avatar of **{avatar}** {avatar.display_avatar}')

@bot.hybrid_command(name="ping", description="Ping")
async def ping(ctx):
    await ctx.send(f'Currently the ping is {round(bot.latency * 1000)}ms')

bot.run(config.token) 