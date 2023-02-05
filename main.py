import discord
from discord.ext import commands 
import config
import vt 

client = vt.Client("your api token")
intents = discord.Intents.all() # Always use intents
bot = commands.Bot(command_prefix="u!", intents=intents)
presence = discord.Game('idk') # Bot presence

errorEmbed = discord.Embed(
    type = 'rich', 
    colour = 0xED4245, 
    description = 'An unexpected error has occurred. Please check the link/file and try again later.',
)

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
    
@bot.hybrid_command(name="url", description="Scan urls...") # First slash command. Say 
async def say(ctx, url): 
    try:
     url_id = vt.url_id(url)
     url = await client.get_object("/urls/{}".format(url_id))
     result = url.last_analysis_stats
 
     embed = discord.Embed(
        type = 'rich', 
        colour = 0xED4245,
        title = f'Results:',
     )

     embed.add_field(name='Harmless', value=result['harmless'], inline=True)
     embed.add_field(name='Malicious', value=result['malicious'], inline=True)
     embed.add_field(name='Suspicious', value=result['suspicious'], inline=True)
     embed.add_field(name='Timeout', value=result['timeout'], inline=True)
     embed.add_field(name='Undetected', value=result['undetected'], inline=True)
     await ctx.send(embed = embed)

    except Exception as e:
        await ctx.send(embed = errorEmbed)
        print(e)

bot.run(config.token) 
