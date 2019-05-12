import discord
import auth
from animals import getFursona

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "?fursona":
        animal = getFursona()
        msg = 'Your fursona is:\n\t*{0}*\n\nhttps://www.google.com/search?q={1}'.format(animal[0], '+'.join(animal[0].split()))
        await message.channel.send(msg)

    if message.content == "?logout":
        print('logged out by {0}'. format(message.author))
        await client.logout()


@client.event
async def on_ready():
    print('\n\nLogged in as')
    print(client.user.name)
    print(client.user.id)
    print('------\n\n')

client.run(auth.token)
