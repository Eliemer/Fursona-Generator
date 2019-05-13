import discord
import auth
from animals import getFursona

client = discord.Client()
prefix = '?'
enable = {}

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return # dont read your own msgs

    if not msg.content.startswith(prefix):
        return # dont read non-commands

    if msg.content == prefix + 'enable':
        enable[msg.channel] = True
        await msg.channel.send('Channel enabled')

    if msg.content == prefix + 'disable':
        enable[msg.channel] = False
        await msg.channel.send('Channel disabled')

    if not msg.channel in enable:
        enable[msg.channel] = False

    if not enable[msg.channel]:
        return # disabled bot

    if msg.content == prefix + 'fursona':
        embed = discord.Embed(
        title='Fursona Generator',
        url='https://www.github.com/Eliemer/Fursona-Generator',
        color=3447003
        )
        name = getFursona()[0]
        link = 'https://www.google.com/search?q={1}'.format(name, '+'.join(name.split()))
        animal = f'__[{name}]({link})__'
        embed.add_field(name='Your fursona is', value=animal, inline=False)
        await msg.channel.send(embed=embed)

    if msg.content == prefix + 'shutdown':
        print('\n\nShutting down')
        print('Goodbye!\n------\n')
        await msg.channel.send('Shutting down. Goodbye!')
        await client.logout()
        sys.exit()

@client.event
async def on_ready():
    print('\n\nLogged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(auth.token)
