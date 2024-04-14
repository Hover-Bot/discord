import discord
import asyncio
from discord import app_commands
from discord.ext import commands
import os
import sys
import socket
import time
from discord import Interaction



intents = discord.Intents().all()
bot = commands.Bot(command_prefix="!", intents=intents)















def is_owner(func):
  def predicate(interaction: discord.Interaction):
    if interaction.user.id == 1218502926885060649:
      return True
  return app_commands.check(predicate)


def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)



@bot.event
async def on_ready():
  print(f"{bot.user.name} s'est bien connecté")

  try:
    synced = await bot.tree.sync(guild=discord.Object(id=1182060624822423642))
    print(f"{len(synced)} commande ont été activer")

  except Exception as e:
    print(e)



@bot.tree.command(guild=discord.Object(id=1182060624822423642), description='Donne ma version.')
async def version(interaction: discord.Interaction):
    await interaction.response.send_message('Je suis a ma 38ime version')


  


@bot.tree.command(guild=discord.Object(id=1182060624822423642), description='désactive le bot')
async def eteindre(interaction: discord.Interaction):
  await interaction.response.send_message(f"Commande acceptée.", ephemeral=True)
  await asyncio.sleep(2)
  await interaction.followup.send("Le bot vas être désactivé")
  await asyncio.sleep(2)
  print('Le bot vas être désactivé')
  await asyncio.sleep(2)
  await bot.close()

@bot.tree.command(guild=discord.Object(id=1182060624822423642), description='Le bot fait des excuse .')
async def service(interaction: discord.Interaction):
    await interaction.response.send_message('Je suis de nouveau en service , Désolé pour le dérangement.@everyone')

@bot.tree.command(guild=discord.Object(id=1182060624822423642), description='Donne le site du bot.')
async def site(interaction: discord.Interaction):
    await interaction.response.send_message('Je suis fier de vous présenter mon propre site !! @everyone:https://hover-bot.github.io/discord/')
  
@bot.tree.command(guild=discord.Object(id=1182060624822423642), description='Donne le ping du bot')
async def ping(interaction: discord.Interaction):
    """ Pong ! """
    before = time.monotonic()
    message = await interaction.response.send_message("Pong!")
    ping = (time.monotonic() - before) * 1000
    await asyncio.sleep(1)
    await interaction.edit_original_response(content=f"Mon ping est de `{int(ping)}ms`")
    print(f'Ping {int(ping)}ms')


@bot.tree.command(guild=discord.Object(id=1182060624822423642), description='Donne le site du bot.')
async def infoutilisateur(interaction: discord.Interaction, member: discord.Member = None):
    member = member
    embed = discord.Embed(title="User Info", description=member.mention, color=member.color)
    embed.add_field(name="Name", value=member.name, inline=True)
    embed.add_field(name="Joined", value=member.joined_at.strftime("%Y-%m-%d"), inline=True)
    embed.add_field(name="Registered", value=member.created_at.strftime("%Y-%m-%d"), inline=True)
    
    # Vérifie si le membre a un avatar
    if member.avatar:
        embed.set_thumbnail(url=member.avatar.url)
    else:
        embed.set_thumbnail(url=member.default_avatar.url)
        
    await interaction.response.send_message(embed=embed)

bot.run("TOKENBOT")
