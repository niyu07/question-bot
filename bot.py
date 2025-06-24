import discord

print("discord読み込みOK")

TOKEN = "YOUR_TOKEN"

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("Botがログインしました！")

@client.event
async def on_message(message):
    print(f"受け取った: {message.content}")
    if message.author == client.user:
        return

    if message.content == "こんにちは":
        await message.channel.send("Hello！")

print("起動開始")
client.run(TOKEN)
print("終了？")