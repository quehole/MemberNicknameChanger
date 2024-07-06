import discord
import random
import asyncio


def read_nicknames(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read().splitlines()

# Bling is also known as "The God of Awesomeness"

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')
    await change_nicknames()

async def change_nicknames():
    guild_id = 81281  # put ur server id in here where I put 81281
    guild = client.get_guild(guild_id)

    if guild is not None:
        nicknames = read_nicknames("nicknames.txt")
        
        for member in guild.members:
            new_nickname = random.choice(nicknames)

            try:
                await member.edit(nick=new_nickname)
                print(f'Changed {member.name}\'s nickname to {new_nickname}')
            except discord.Forbidden:
                print(f'Bot does not have permission to change {member.name}\'s nickname')
            
            
            await asyncio.sleep(2)  


bot_token = "YOUR BOT TOKEN"
client.run(bot_token)
