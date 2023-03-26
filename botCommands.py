import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
#from google import search
#from googleapiclient.discovery import build
##Cost $0.005 per google search
# Start of commands file
# Command prefix (!)
# List of current commands w/description
DevPSUBot = commands.Bot(command_prefix = '!', intents=discord.Intents.all())

#help-Explains the contents of the discord bot
DevPSUBot.remove_command('help')
@DevPSUBot.command()
async def help(ctx):
 embed = discord.Embed(
  title = 'Bot Commands',
  color = discord.Colour.dark_blue(),
  description='Welcome to help section of chat bot. Here is a list of basic commands!'
 )
 embed.add_field(
  name = '!help',
  value = 'List all of the commands.',
  inline = False
 )
 embed.add_field(
  name = '!info',
  value = 'Display information about the server.',
  inline = False
 )
 embed.add_field(
  name = 'translate',
  value = 'Command Format: Directly type into chat "translate <your text> to <language>\n Type <!languagekeys>" to find a list of all valid language keys!',
  inline = False
 )
 embed.add_field(
  name = '!languagekeys',
  value = 'Display a list of all valid translation languages.',
  inline = False
 )
 embed.add_field(
  name = '!languagekeys',
  value = 'Display a list of all valid translation languages.',
  inline = False
 )
 embed.add_field(
  name = '!search <URL>',
  value = 'Search for a video using the provided URL link',
  inline = False
 )
 embed.set_thumbnail(url='')
 await ctx.send(embed=embed)

@DevPSUBot.command()
async def info(ctx):
 # ctx = content (info about how command executed)
 #!info
 await ctx.send(ctx.guild)
 await ctx.send(ctx.author)
 await ctx.send(ctx.message.id)

@DevPSUBot.command()
async def search(ctx, arg = None):
 if(arg == None):
  await ctx.send(f'Please provide a URL')
 #Implement code using google api to search google for the video play it in the chat thorugh an embeded response.

#load_dotenv()
#token = os.getenv('TOKEN')
#DevPSUBot.run(token)