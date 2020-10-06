import requests, pprint, random, discord, asyncio, os
from discord.ext import commands, tasks
from itertools import cycle
from secret import token, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET
#import tweepy
client = commands.Bot(command_prefix='.')
TOKEN = token
status = cycle(["With Tor's feelings", 'War Thunder','& Getting Cat Facts', 'Jailbait for Jonsey'])
thingsRasmusSaid = []
#Twitter auth
#auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
#auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

#snufkin = tweepy.API(auth)
#body = {
#    "template_id" : 112126428,
#    "password" : "starcraft",
#    "username" : "Joonsey",
#    "text0" : "...",
#    "text1" : "...",
#}
f = requests.get('https://api.imgflip.com/get_memes')
r = requests.get('https://cat-fact.herokuapp.com/facts')
raiderio = requests.get('https://raider.io/api/v1/mythic-plus/affixes?region=eu&locale=en').json()
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

class memes(commands.Cog):
    """A bunch of memes that you can customize with arguments.
    Arguments are differantiated by ','."""
    @commands.command(aliases=['memet', 'mt'])
    async def memetemplate(self, ctx):
        "random meme template"
        n = f.json()["data"]["memes"][random.randint(0,len(f.json()["data"]["memes"]))]
        await ctx.send(n['url'])
        await ctx.send(n['name'] +", id: " + n['id'])

    @commands.command(aliases=['m1', 'db'])
    async def meme1(self, ctx, *args):
        "cheeting boyfriend meme, takes 3 arguments"
        arg1, arg2, arg3 = " ".join(args).split(",")[0]," ".join(args).split(",")[1], " ".join(args).split(",")[2]
        await ctx.send(requests.post("https://api.imgflip.com/caption_image", data={
        "template_id" : 112126428,
        "password" : "starcraft",
        "username" : "Joonsey",
        "boxes[0][text]" : arg1, 
        "boxes[1][text]" : arg2,
        "boxes[2][text]": arg3}).json()['data']['url'])
        await ctx.message.delete()

    @commands.command(aliases=["redbutton","2choices","choices","button", "m2"])
    async def meme2(self, ctx, *args):
        "red button, two choices meme, takes 2 arguments"
        arg1, arg2 = " ".join(args).split(",")[0]," ".join(args).split(",")[1]
        await ctx.send(requests.post("https://api.imgflip.com/caption_image", data={
        "template_id" : 87743020,
        "password" : "starcraft",
        "username" : "Joonsey",
        "text0" : arg1,
        "text1" : arg2}).json()['data']['url'])
        await ctx.message.delete()

    @commands.command(aliases=["bigbrain","expandingbrain","eb","brain", "m3"])
    async def meme3(self, ctx, *args):
        "expanding brain meme, takes 4 arguments"
        arg1, arg2, arg3, arg4 = " ".join(args).split(",")[0]," ".join(args).split(",")[1], " ".join(args).split(",")[2], " ".join(args).split(",")[3] 
        await ctx.send(requests.post("https://api.imgflip.com/caption_image", data={
        "template_id" : 93895088,
        "password" : "starcraft",
        "username" : "Joonsey",
        "boxes[0][text]" : arg1, 
        "boxes[1][text]" : arg2,
        "boxes[2][text]" : arg3,
        "boxes[3][text]" : arg4}).json()['data']['url'])
        await ctx.message.delete()

    @commands.command(aliases=['slap', "m4"])
    async def meme4(self, ctx, *args):
        "batman slapping robbin meme, takes 2 arguments"
        arg1, arg2 = " ".join(args).split(",")[0]," ".join(args).split(",")[1]
        await ctx.send(requests.post("https://api.imgflip.com/caption_image", data={
        "template_id" : 438680,
        "password" : "starcraft",
        "username" : "Joonsey",
        "text0" : arg1,
        "text1" : arg2}).json()['data']['url'])
        await ctx.message.delete()

    @commands.command(aliases=['car','drift','m5'])
    async def meme5(self, ctx, *args):
        "car drifting hard right meme, takes 3 arguments"
        arg1, arg2, arg3 = " ".join(args).split(",")[0]," ".join(args).split(",")[1], " ".join(args).split(",")[2]
        await ctx.send(requests.post("https://api.imgflip.com/caption_image", data={
        "template_id" : 124822590,
        "password" : "starcraft",
        "username" : "Joonsey",
        "boxes[0][text]" : arg1, 
        "boxes[1][text]" : arg2,
        "boxes[2][text]": arg3}).json()['data']['url'])
        await ctx.message.delete()

    @commands.command(aliases=['m6','cat', "catgirls", 'catwoman'])
    async def meme6(self, ctx, *args):
        "2 women mad at cat, takes 2 arguments"
        arg1, arg2 = " ".join(args).split(",")[0]," ".join(args).split(",")[1]
        await ctx.send(requests.post("https://api.imgflip.com/caption_image", data={
        "template_id" : 188390779,
        "password" : "starcraft",
        "username" : "Joonsey",
        "text0" : arg1,
        "text1" : arg2}).json()['data']['url'])
        await ctx.message.delete()

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
async def _8ball(ctx,*, arg):
    "Helps you see your future (or past)"
    await ctx.send(f"""Question: {arg} \nAnswer: {random.choice(['Definitely!','Most likely','Probably','Maybe','with extreme certainty!','No way!'])}""")

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.event
async def on_message(message):
    if message.author.id == 311125741616234507:
        thingsRasmusSaid.append(str(message.content))
        print("Rasmus just said something! He said: ", message.content)
    elif message.author.id == 267112523335991307:
        if "gay" in message.content.lower():
            await message.channel.send(":eyes:")
    await client.process_commands(message)
    
@client.command(aliases=['weather'])
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
    embedVar = discord.Embed(title="I have no clue how to use this properly", description=" ".join(args), color=0x00ff00)
    await ctx.send(embed=embedVar)
    await ctx.message.delete()

@client.command()
async def affixes(ctx):
    "Gets weekly Mythic+ affix information"
    embeded = discord.Embed(title="Raider.io Affixes", color=0x00ff00)
    embeded.add_field(name=raiderio["affix_details"][0]['name'],value=raiderio["affix_details"][0]['description'])
    embeded.add_field(name=raiderio["affix_details"][1]['name'],value=raiderio["affix_details"][1]['description'])
    embeded.add_field(name=raiderio["affix_details"][2]['name'],value=raiderio["affix_details"][2]['description'])
    embeded.add_field(name=raiderio["affix_details"][3]['name'],value=raiderio["affix_details"][3]['description'])
    #await ctx.send(">>> **" + raiderio["affix_details"][0]['name']+"** "+"\n"+
    #raiderio["affix_details"][0]['description']+"\n"
    #+"**"+raiderio["affix_details"][1]['name']+"** "+"\n"+
    #raiderio["affix_details"][1]['description']+"\n"
    #+"**"+raiderio["affix_details"][2]['name']+"** "+"\n"+
    #raiderio["affix_details"][2]['description']+"\n"
    #+"**"+raiderio["affix_details"][3]['name']+"** "+"\n"+
    #raiderio["affix_details"][3]['description'])
    await ctx.send(embed=embeded)
client.add_cog(memes())
client.run(TOKEN)

#snufkin.update_status(thingsRasmusSaid)

