import os
import discord
import subprocess
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

# paiza_picker.py を実行して出力を取得
result = subprocess.run(["python3", "main.py"], capture_output=True, text=True)
output = result.stdout.strip()  # 改行などを取り除く

# Discordへ送信する準備
intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    channel = client.get_channel(CHANNEL_ID)
    if channel is None:
        print(f"チャンネルが見つかりません。CHANNEL_ID={CHANNEL_ID} を確認してください。")
    else:
        await channel.send(output)
    await client.close()

client.run(TOKEN)