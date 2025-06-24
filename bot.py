import discord

print("discord読み込みOK")

TOKEN = "MTM4NDg5MTIwNTU0Nzk4Mjg5OA.GEE3P_.7QSU5gKsuLex13L5hRek7MDzR1Rrg1TR8JyZHg"

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