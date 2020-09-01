import requests, pprint, random, discord, asyncio, os
from discord.ext import commands, tasks
from itertools import cycle
from secret import token

client = commands.Bot(command_prefix='.')
TOKEN = token
status = cycle(["With Tor's feelings", 'War Thunder','& Getting Cat Facts'])

#f = requests.get('https://api.imgflip.com/get_memes')
r = requests.get('https://cat-fact.herokuapp.com/facts')
#w = requests.get('http://en.wikipedia.org/w/api.php?action=query&generator=random&grnnamespace=0&prop=extracts&exchars=500&format=json')
#s = requests.get('eu.api.blizzard.com')

@client.event
async def on_ready():
    change_status.start()
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    #print(client.users)

@client.command()
async def ping(ctx):
    await ctx.send(f'{round(client.latency * 1000)}ms')
    await ctx.trigger_typing()


@client.command(aliases=['factcat']) #shows a funny cat fact
async def catfact(ctx):
    await ctx.trigger_typing()
    await ctx.send(r.json()['all'][random.randint(1,200)]['text'])


@client.command()
async def repeat(ctx, *, args):
    await ctx.send(f"""I am repeating {ctx.author.mention} with: {args}
"""*5)
    

@client.command(aliases=[':eyes:'])
async def eyes(ctx):
    await ctx.send(':eyes:')


@client.command(aliases=['8ball','Eightball'])
async def _8ball(ctx,*,arg):
    await ctx.send(f"""Question: {arg} \nAnswer: {random.choice(['Definatly!','Most likely','Probably','Maybe','with extreme certainty!','No way!'])}""")

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


client.run(TOKEN)

