import discord
from discord.ext import commands
import os

# Ambil token dari environment variable (AMAN untuk hosting)
TOKEN = os.getenv("MTQwNzA2NDA4MjgwMDE4MTM4MA.GWZnc-.hCtKmBihAwS1vSBD8fuJoA7fiCT9w4myO-T6gA")

SOURCE_CHANNEL_ID = 1406882509903499284
TARGET_CHANNEL_ID = 1392575073562394695

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot sudah login sebagai {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.channel.id == SOURCE_CHANNEL_ID:
        target_channel = bot.get_channel(TARGET_CHANNEL_ID)
        if target_channel:
            content = f"**{message.author.display_name}:** {message.content}"
            if message.attachments:
                files = [await att.to_file() for att in message.attachments]
                await target_channel.send(content, files=files)
            else:
                await target_channel.send(content)

    await bot.process_commands(message)

bot.run(TOKEN)
