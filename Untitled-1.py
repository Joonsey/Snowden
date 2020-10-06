import requests, pprint, random, discord, asyncio, os
from discord.ext import commands, tasks
from itertools import cycle
from secret import token, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET
#import tweepy
client = commands.Bot(command_prefix='.')
TOKEN = token
status = cycle(["With Tor's feelings", 'War Thunder','& Getting Cat Facts'])
thingsRasmusSaid = []
#Twitter auth
#auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
#auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

#snufkin = tweepy.API(auth)

#f = requests.get('https://api.imgflip.com/get_memes')
r = requests.get('https://cat-fact.herokuapp.com/facts')
#w = requests.get('http://en.wikipedia.org/w/api.php?action=query&generator=random&grnnamespace=0&prop=extracts&exchars=500&format=json')
#s = requests.get('eu.api.blizzard.com')
w = requests.get('https://api.met.no/weatherapi/locationforecast/2.0/compact?altitude=142&lat=59.7472&lon=10.3883')
værdata = w.json()['properties']['timeseries'][0]['data']['instant']['details']
værtid = w.json()['properties']['timeseries'][0]['time']
værbilde = w.json()['properties']['timeseries'][0]['data']['next_1_hours']['summary']['symbol_code']

def værcheck():
    if "rain" in værbilde:
        return ":cloud_rain:"
    elif "sunny" or "clear" in værbilde:
        return ":sunny:"
    elif "cloudy" in værbilde:
        return ":cloud:"
    elif "fog" in værbilde:
        return ":fog:"
    elif "thunder" in værbilde:
        return ":thunder_cloud_rain:"
    else:
        return ":cloud:"
#    if værbilde == "heavyrain":
#        return ":cloud_rain:"
#    elif værbilde == "clearsky":
#        return ":sunny:"
#    elif værbilde == "cloudy":
#        return ":cloud:"
#    elif værbilde == "fair":
#        return ":white_sun_small_cloud:"
#    elif værbilde == "fog":
#        return ":fog:"
#    elif værbilde == "heavyrainandthunder":
#        return ":thunder_cloud_rain:"
#    elif værbilde == "heavyrainshowers" or "heavyrainshowersandthunder":
#        return ":thunder_cloud_rain:"
#    elif værbilde == "heavysleet":
#
@client.event
async def on_ready():
    change_status.start()
    print('Logged in as', client.user.name)
    #print(client.user.name)
    #print(client.user.id)
    #print(client.users)

@client.command()
async def ping(ctx):
    "Displays ping"
    await ctx.send(f'{round(client.latency * 1000)}ms')
    await ctx.trigger_typing()


@client.command(aliases=['factcat'])
async def catfact(ctx):
    "Sends a random fact about cats"
    await ctx.trigger_typing()
    await ctx.send(r.json()['all'][random.randint(1,200)]['text'])


@client.command()
async def repeat(ctx, *, args):
    "Repeats argument passed 5 times"
    await ctx.send(f"""I am repeating {ctx.author.mention} with: {args}
"""*5)
    

@client.command(aliases=[':eyes:'])
async def eyes(ctx):
    "Send :eyes:"
    await ctx.send(':eyes:')


@client.command(aliases=['8ball','Eightball'])
async def _8ball(ctx,*,arg):
    "Helps you see your future (or past)"
    await ctx.send(f"""Question: {arg} \nAnswer: {random.choice(['Definatly!','Most likely','Probably','Maybe','with extreme certainty!','No way!'])}""")

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.event
async def on_message(message):
    if message.author.id == 311125741616234507:
        thingsRasmusSaid.append(str(message.content))
        print("Rasmus just said something! He said: ", message.content)
    await client.process_commands(message)
        
    
@client.command()
async def vær(ctx):
    "Shows weather information in MY local area"
    await ctx.send("The temperature is: " + str(værdata["air_temperature"]) + "°C \n" +
'The air humidity is: ' + str(værdata["relative_humidity"]) + "% \n"
'The wind speed is: ' + str(værdata["wind_speed"]) + 'm/s \n'
'The data was collected at: ' + str(værtid))
    await ctx.send(værcheck())


@client.command()
async def shame(ctx):
    "Shames rasmus >:("
    await ctx.send(" **-** ".join(thingsRasmusSaid))

@client.command()
async def embed(ctx, *args):
    embedVar = discord.Embed(title="I have no clue how to use this properly", description="At all", color=0x00ff00)
    embedVar.add_field(name="Field1", value=" ".join(args), inline=False)
    embedVar.add_field(name="Field2", value="Whoever used this is an idiot lmao", inline=False)
    await ctx.send(embed=embedVar)

client.run(TOKEN)

#snufkin.update_status(thingsRasmusSaid)

