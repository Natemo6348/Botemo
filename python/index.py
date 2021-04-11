import discord, asyncio, json
from discord.ext import commands

class Botemo(commands.AutoShardedBot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

def read_json(file):
    with open(file, "r") as f:
        secrets = json.loads(f)
    return secrets

data = read_json('../secrets.json')

bot = Botemo(command_prefix=data['prefix'], owner_id=data['discord_owner_id'])

@bot.event
async def on_ready():
    print(f"{bot.user} is Ready!")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{bot.command_prefix}help"))

bot.run(data['token'])
