import discord, random, aiohttp, json
from discord.ext import commands
from typing import Union
from google_trans_new import google_translator as Translator

class Other(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
        self.answers = ["Yes.", "No.", "My sources say yes!", "Most likely.", "I don't know.", "Maybe, sometimes.", "Outlook is good.", "Signs point to yes.", "Definitely!", "Absolutely!", "Nope.", "No thanks, I won’t be able to make it.", "No Way!", "It's certain.", "It's decidedly so.", "Without a doubt.", "Yes - definitely.", "You can rely on it.", "As I see it, yes."]
        
    @commands.command(aliases=['tr'])   
    async def translate(self, ctx, lang: str, *, text : str):
        await ctx.send(embed=discord.Embed(title="Translated!", description=Translator().translate(text, lang_tgt=lang)))
        
    @commands.command()       
    async def say(self, ctx, *, text : str):
        """
        Make the bot say anything!
        """
        
        await ctx.send(text)
        
    @commands.command(aliases=['profile-picture', 'profile-pic', 'pfp', 'av'])
    async def avatar(self, ctx, user : Union[discord.Member, int]):
        """
        Responds with a user's avatar.  
        """   
        await ctx.send(embed=discord.Embed(colour=discord.Colour.from_rgb(64, 59, 58), title="Avatar").set_image(url=str(user.avatar_url)))          
                
    @commands.command()       
    async def advice(self, ctx):
        """
        Get some advice!
        """
        
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.adviceslip.com/advice", headers={'content-type': 'application/json'}) as res:
                data = await res.text()
                data = json.loads(data)
                advice = data['slip']['advice']
        await ctx.send(embed=discord.Embed(colour=discord.Colour.from_rgb(64, 59, 58), title="Advice", desription=advice))
        
    @commands.command(aliases=['botinfo', 'whomademe', 'bot-maker', 'bot-creator'])  
    async def about(self, ctx):
        """
        Learn about the bot and it's creator!
        """
        await ctx.send("Made by hyperzone#1185 with :heart: full code is available on GitHub https://github.com/galnir/Master-Bot")
    
    @commands.command(name='8ball', aliases=['eightball'])
    async def magicball(self, ctx, *, question : str):
        """
        Get the answer to anything!
        """
        await ctx.send(embed=discord.Embed(title="Magic 8ball", description=random.choice(self.answers), colour=discord.Colour.from_rgb(64, 59, 58)))
      

def setup(bot):
    bot.add_cog(Other(bot))                         
