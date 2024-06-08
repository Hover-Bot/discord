import discord
import asyncio
from discord.ext import commands
import os
import sys
import time
from discord_slash import SlashCommand, SlashContext

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)
slash = SlashCommand(bot, sync_on_cog_reload=True)

# Décorateur pour vérifier si l'utilisateur est le propriétaire
def is_owner():
    def predicate(ctx):
        return ctx.author.id == 1218502926885060649
    return commands.check(predicate)

# Fonction pour redémarrer le programme
def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)

# Événement de connexion
@bot.event
async def on_ready():
    print(f"{bot.user.name} s'est bien connecté")

# Commandes
@slash.slash(name="version", description='Donne ma version.')
async def version(ctx: SlashContext):
    await ctx.send('Je suis à ma 38ème version')

@slash.slash(name="eteindre", description='Désactive le bot')
async def eteindre(ctx: SlashContext):
    await ctx.send(f"Commande acceptée.", hidden=True)
    await asyncio.sleep(2)
    await ctx.send("Le bot va être désactivé")
    await asyncio.sleep(2)
    print('Le bot va être désactivé')
    await asyncio.sleep(2)
    await bot.close()

@slash.slash(name="service", description='Le bot fait des excuses.')
async def service(ctx: SlashContext):
    await ctx.send('Je suis de nouveau en service, Désolé pour le dérangement. @everyone')

@slash.slash(name="site", description='Donne le site du bot.')
async def site(ctx: SlashContext):
    await ctx.send('Je suis fier de vous présenter mon propre site !! @everyone: https://hover-bot.github.io/discord/')

@slash.slash(name="ping", description='Donne le ping du bot.')
async def ping(ctx: SlashContext):
    """ Pong ! """
    before = time.monotonic()
    message = await ctx.send("Pong!")
    ping = (time.monotonic() - before) * 1000
    await asyncio.sleep(1)
    await ctx.edit(content=f"Mon ping est de `{int(ping)}ms`")
    print(f'Ping {int(ping)}ms')

@slash.slash(name="infoutilisateur", description='Donne les informations sur un utilisateur.')
async def infoutilisateur(ctx: SlashContext, member: discord.Member = None):
    member = member or ctx.author
    embed = discord.Embed(title="User Info", description=member.mention, color=member.color)
    embed.add_field(name="Name", value=member.name, inline=True)
    embed.add_field(name="Joined", value=member.joined_at.strftime("%Y-%m-%d"), inline=True)
    embed.add_field(name="Registered", value=member.created_at.strftime("%Y-%m-%d"), inline=True)
    
    # Vérifie si le membre a un avatar
    if member.avatar:
        embed.set_thumbnail(url=member.avatar.url)
    else:
        embed.set_thumbnail(url=member.default_avatar.url)
        
    await ctx.send(embed=embed)

bot.run(os.getenv('DISCORD_BOT_TOKEN'))
