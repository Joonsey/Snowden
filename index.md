# Welcome to Snowden!
Snowden is a general use Discord bot with some funny quirks and commands.  
for instance: 
- can post random cat facts using an API.
- can find random wikipidia posts and post them in the chat.
- can repeat something from a person like a @person (works perfectly if you require someone's attention).
- can send eyes in chat. 👀
- can send it's own ping to show lag.

## Why would you use Snowden?

Don't know, maybe you're a masochist?

## Why is he named Snowden?

Asked my mom what would be a call name for a robot and she was totally ignoring my question while ranting about [Edward Snowden](https://en.wikipedia.org/wiki/Edward_Snowden).

## A list of references to project Snowden and their opinions.

Respected person | Totally legit opinion
-----------------|----------------------
Tor | great bot!
Rasmus | awesome yo
Noel | donkey
Leon | 😎

---

# But how does he work and how do I use him?

Soon after you've downloaded and set him up you'll realise that i have not documented his commands almost at all.
But worry not! That's what this is for 😇.

**This is the ping command**
```python
@client.command()
async def ping(ctx):
    await ctx.send(f'{round(client.latency * 1000)}ms')
    await ctx.trigger_typing()
```
It sends a message containing the delay of the bot in chat.  

**This is the catfact command**
```python
@client.command(aliases=['factcat'])
async def catfact(ctx):
    await ctx.trigger_typing()
    await ctx.send(r.json()['all'][random.randint(1,200)]['text'])
```
When you send either .catfact or .factcat it will go through the data it has collected from the API and chose a random line of taxt between 1-200 of the updated data set.  

**The repeat command**
```python
@client.command()
async def repeat(ctx, *, args):
    await ctx.send(f"""I am repeating {ctx.author.mention} with: {args}
"""*5)
```
It will repeat the context of the message input after the inital .repeat command and the person who initiated the command (to expose those who uses it for malicious intent 😪) 5 times.  

**The eyes command**
```python
@client.command(aliases=[':eyes:'])
async def eyes(ctx):
    await ctx.send(':eyes:')
```
It sends 👀 in the chat. Almost as if it's looking for something.  

**8 ball command**
```python
@client.command(aliases=['8ball','Eightball'])
async def _8ball(ctx,*,arg):
    await ctx.send(f"""Question: {arg} \nAnswer: {random.choice(['Definatly!','Most likely','Probably','Maybe','with extreme certainty!','No way!'])}""")
```
When calling this command it wall chocie a random response from the list passed along with the question asked.
