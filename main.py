import discord
from discord.ext import commands 
import config

intents = discord.Intents.all() # Always use intents
bot = commands.Bot(command_prefix="u!", intents=intents)
presence = discord.Game('idk') # Bot presence

# event
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=presence) # set presence
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
    embed = discord.Embed()
    # In case not of a value
    if avatar == None:
        embed.type = 'rich'
        embed.colour = 0xED4245
        embed.url = f'https://discord.com/users/{ctx.author.id}'
        embed.title = f'Avatar of **{ctx.author}**'
        embed.set_image(url=ctx.author.display_avatar)
        await ctx.send(embed = embed) # Send embed
    # Returns a value...
    else:
        embed.type = 'rich'
        embed.colour = 0xED4245
        embed.url = f'https://discord.com/users/{avatar.id}'
        embed.title = f'Avatar of **{avatar}**'
        embed.set_image(url=avatar.display_avatar)
        await ctx.send(embed = embed)

@bot.hybrid_command(name="ping", description="Ping")
async def ping(ctx):
    embed = discord.Embed()
    embed.type = 'rich'
    embed.colour = 0xFEE75C
    embed.description = f'Currently the ping is {round(bot.latency * 1000)}ms' 
    embed.set_footer(text='Ping!', icon_url=None)
    await ctx.send(embed = embed)

bot.run(config.token) 