import discord
from discord.ext import commands
import requests


class AnimalCommands(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.command(description="Displays all supported animal commands")
    async def animals(self, ctx):
        description = '**Supported animal keywords:**' + '\n' + '`dog`, `cat`, `bird`, `panda`, `redpanda`, `fox`, `koala`, `raccoon`, `kangaroo`, `whale`' \
                      '\n' + '\n' + '**Example:**' + '\n' + '`$keyword` to get image or `$keywordfact` to get fact'

        embed = discord.Embed(
            title="Animal commands",
            description=description
        )
        await ctx.send(embed=embed)

    @commands.command(description="Gives out a random dog image")
    async def dog(self, ctx):
        # Making a GET request to the endpoint
        resp = requests.get("https://some-random-api.ml/img/dog")
        # Checking if response has a healthy status code
        if 300 > resp.status_code >= 200:
            content = resp.json()
            embed = discord.Embed(
                title="Random Dog picture"
            )
            embed.set_image(url=content['link'])
            await ctx.reply(embed=embed)
        else:
            await ctx.reply("Recieved a bad status code of " + str(resp.status_code))

    @commands.command(description="Gives out a random dog fact", aliases=['dogf'])
    async def dogfact(self, ctx):
        # Making a GET request to the endpoint
        resp = requests.get("https://some-random-api.ml/facts/dog")
        # Checking if response has a healthy status code
        if 300 > resp.status_code >= 200:
            content = resp.json()
            embed = discord.Embed(
                title="Random Dog fact",
                description=content['fact']
            )
            await ctx.reply(embed=embed)
        else:
            await ctx.reply("Recieved a bad status code of " + str(resp.status_code))

    @commands.command(description="Gives out a random cat image")
    async def cat(self, ctx):
        # Making a GET request to the endpoint
        resp = requests.get("https://some-random-api.ml/img/cat")
        # Checking if response has a healthy status code
        if 300 > resp.status_code >= 200:
            content = resp.json()
            embed = discord.Embed(
                title="Random Cat picture"
            )
            embed.set_image(url=content['link'])
            await ctx.reply(embed=embed)
        else:
            await ctx.reply("Recieved a bad status code of " + str(resp.status_code))

    @commands.command(description="Gives out a random cat fact", aliases=['catf'])
    async def catfact(self, ctx):
        # Making a GET request to the endpoint
        resp = requests.get("https://some-random-api.ml/facts/cat")
        # Checking if response has a healthy status code
        if 300 > resp.status_code >= 200:
            content = resp.json()
            embed = discord.Embed(
                title="Random Cat fact",
                description=content['fact']
            )
            await ctx.reply(embed=embed)
        else:
            await ctx.reply("Recieved a bad status code of " + str(resp.status_code))

    @commands.command(description="Gives out a random bird image", aliases=['birb'])
    async def bird(self, ctx):
        # Making a GET request to the endpoint
        resp = requests.get("https://some-random-api.ml/img/birb")
        # Checking if response has a healthy status code
        if 300 > resp.status_code >= 200:
            content = resp.json()
            embed = discord.Embed(
                title="Random Bird picture"
            )
            embed.set_image(url=content['link'])
            await ctx.reply(embed=embed)
        else:
            await ctx.reply("Recieved a bad status code of " + str(resp.status_code))

    @commands.command(description="Gives out a random bird fact", aliases=['birdf', 'birbfact', 'birbf'])
    async def birdfact(self, ctx):
        # Making a GET request to the endpoint
        resp = requests.get("https://some-random-api.ml/facts/birb")
        # Checking if response has a healthy status code
        if 300 > resp.status_code >= 200:
            content = resp.json()
            embed = discord.Embed(
                title="Random Bird fact",
                description=content['fact']
            )
            await ctx.reply(embed=embed)
        else:
            await ctx.reply("Recieved a bad status code of " + str(resp.status_code))

    @commands.command(description="Gives out a random panda image")
    async def panda(self, ctx):
        # Making a GET request to the endpoint
        resp = requests.get("https://some-random-api.ml/img/panda")
        # Checking if response has a healthy status code
        if 300 > resp.status_code >= 200:
            content = resp.json()
            embed = discord.Embed(
                title="Random Panda picture"
            )
            embed.set_image(url=content['link'])
            await ctx.reply(embed=embed)
        else:
            await ctx.reply("Recieved a bad status code of " + str(resp.status_code))

    @commands.command(description="Gives out a random panda fact", aliases=['pandaf'])
    async def pandafact(self, ctx):
        # Making a GET request to the endpoint
        resp = requests.get("https://some-random-api.ml/facts/panda")
        # Checking if response has a healthy status code
        if 300 > resp.status_code >= 200:
            content = resp.json()
            embed = discord.Embed(
                title="Random Panda fact",
                description=content['fact']
            )
            await ctx.reply(embed=embed)
        else:
            await ctx.reply("Recieved a bad status code of " + str(resp.status_code))

    @commands.command(description="Gives out a random red panda image")
    async def redpanda(self, ctx):
        # Making a GET request to the endpoint
        resp = requests.get("https://some-random-api.ml/img/red_panda")
        # Checking if response has a healthy status code
        if 300 > resp.status_code >= 200:
            content = resp.json()
            embed = discord.Embed(
                title="Random Red Panda picture"
            )
            embed.set_image(url=content['link'])
            await ctx.reply(embed=embed)
        else:
            await ctx.reply("Recieved a bad status code of " + str(resp.status_code))

    @commands.command(description="Gives out a random red panda fact", aliases=['redpandaf'])
    async def redpandafact(self, ctx):
        # Making a GET request to the endpoint
        resp = requests.get("https://some-random-api.ml/facts/red_panda")
        # Checking if response has a healthy status code
        if 300 > resp.status_code >= 200:
            content = resp.json()
            embed = discord.Embed(
                title="Random Red Panda fact",
                description=content['fact']
            )
            await ctx.reply(embed=embed)
        else:
            await ctx.reply("Recieved a bad status code of " + str(resp.status_code))

    @commands.command(description="Gives out a random fox image")
    async def fox(self, ctx):
        # Making a GET request to the endpoint
        resp = requests.get("https://some-random-api.ml/img/fox")
        # Checking if response has a healthy status code
        if 300 > resp.status_code >= 200:
            content = resp.json()
            embed = discord.Embed(
                title="Random Fox picture"
            )
            embed.set_image(url=content['link'])
            await ctx.reply(embed=embed)
        else:
            await ctx.reply("Recieved a bad status code of " + str(resp.status_code))

    @commands.command(description="Gives out a random fox fact", aliases=['foxf'])
    async def foxfact(self, ctx):
        # Making a GET request to the endpoint
        resp = requests.get("https://some-random-api.ml/facts/fox")
        # Checking if response has a healthy status code
        if 300 > resp.status_code >= 200:
            content = resp.json()
            embed = discord.Embed(
                title="Random Fox fact",
                description=content['fact']
            )
            await ctx.reply(embed=embed)
        else:
            await ctx.reply("Recieved a bad status code of " + str(resp.status_code))

    @commands.command(description="Gives out a random koala image")
    async def koala(self, ctx):
        # Making a GET request to the endpoint
        resp = requests.get("https://some-random-api.ml/img/koala")
        # Checking if response has a healthy status code
        if 300 > resp.status_code >= 200:
            content = resp.json()
            embed = discord.Embed(
                title="Random Koala picture"
            )
            embed.set_image(url=content['link'])
            await ctx.reply(embed=embed)
        else:
            await ctx.reply("Recieved a bad status code of " + str(resp.status_code))

    @commands.command(description="Gives out a random koala fact", aliases=['koalaf'])
    async def koalafact(self, ctx):
        # Making a GET request to the endpoint
        resp = requests.get("https://some-random-api.ml/facts/koala")
        # Checking if response has a healthy status code
        if 300 > resp.status_code >= 200:
            content = resp.json()
            embed = discord.Embed(
                title="Random Koala fact",
                description=content['fact']
            )
            await ctx.reply(embed=embed)
        else:
            await ctx.reply("Recieved a bad status code of " + str(resp.status_code))

    @commands.command(description="Gives out a random raccoon image")
    async def raccoon(self, ctx):
        # Making a GET request to the endpoint
        resp = requests.get("https://some-random-api.ml/img/raccoon")
        # Checking if response has a healthy status code
        if 300 > resp.status_code >= 200:
            content = resp.json()
            embed = discord.Embed(
                title="Random Raccoon picture"
            )
            embed.set_image(url=content['link'])
            await ctx.reply(embed=embed)
        else:
            await ctx.reply("Recieved a bad status code of " + str(resp.status_code))

    @commands.command(description="Gives out a random raccoon fact", aliases=['raccoonf'])
    async def raccoonfact(self, ctx):
        # Making a GET request to the endpoint
        resp = requests.get("https://some-random-api.ml/facts/raccoon")
        # Checking if response has a healthy status code
        if 300 > resp.status_code >= 200:
            content = resp.json()
            embed = discord.Embed(
                title="Random Raccoon fact",
                description=content['fact']
            )
            await ctx.reply(embed=embed)
        else:
            await ctx.reply("Recieved a bad status code of " + str(resp.status_code))

    @commands.command(description="Gives out a random kangaroo image")
    async def kangaroo(self, ctx):
        # Making a GET request to the endpoint
        resp = requests.get("https://some-random-api.ml/img/kangaroo")
        # Checking if response has a healthy status code
        if 300 > resp.status_code >= 200:
            content = resp.json()
            embed = discord.Embed(
                title="Random Kangaroo picture"
            )
            embed.set_image(url=content['link'])
            await ctx.reply(embed=embed)
        else:
            await ctx.reply("Recieved a bad status code of " + str(resp.status_code))

    @commands.command(description="Gives out a random kangaroo fact", aliases=['kangaroof'])
    async def kangaroofact(self, ctx):
        # Making a GET request to the endpoint
        resp = requests.get("https://some-random-api.ml/facts/kangaroo")
        # Checking if response has a healthy status code
        if 300 > resp.status_code >= 200:
            content = resp.json()
            embed = discord.Embed(
                title="Random Kangaroo fact",
                description=content['fact']
            )
            await ctx.reply(embed=embed)
        else:
            await ctx.reply("Recieved a bad status code of " + str(resp.status_code))

    @commands.command(description="Gives out a random whale image")
    async def whale(self, ctx):
        # Making a GET request to the endpoint
        resp = requests.get("https://some-random-api.ml/img/whale")
        # Checking if response has a healthy status code
        if 300 > resp.status_code >= 200:
            content = resp.json()
            embed = discord.Embed(
                title="Random Whale picture"
            )
            embed.set_image(url=content['link'])
            await ctx.reply(embed=embed)
        else:
            await ctx.reply("Recieved a bad status code of " + str(resp.status_code))

    @commands.command(description="Gives out a random whale fact", aliases=['whalef'])
    async def whalefact(self, ctx):
        # Making a GET request to the endpoint
        resp = requests.get("https://some-random-api.ml/facts/whale")
        # Checking if response has a healthy status code
        if 300 > resp.status_code >= 200:
            content = resp.json()
            embed = discord.Embed(
                title="Random Whale fact",
                description=content['fact']
            )
            await ctx.reply(embed=embed)
        else:
            await ctx.reply("Recieved a bad status code of " + str(resp.status_code))


# Must have a setup function
def setup(client):
    # Add the class to the cog
    client.add_cog(AnimalCommands(client))
