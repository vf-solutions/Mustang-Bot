# invite link:
# https://discord.com/api/oauth2/authorize?client_id=957743101995274280&permissions=8&scope=bot
# python local-bot.py

from email import message
import discord
from discord.ext import commands
from discord.utils import get

from constants import *

intents = discord.Intents.all()
client = commands.Bot(command_prefix = '$', intents=intents)
client.remove_command("$help")

def getToken():
  with open('assets/token.txt', 'r') as file: # read file content
    data = file.read().replace('\n', '')
    return data # store file contents in data

def getID():
  return f"{client.user.id}"

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online, activity=discord.Game(name="React to my messages in #welcome-and-rules to show others the classes you are in"))
  print("My body is ready")
  print('We have logged in as {0.user}'.format(client))
  print("Name: {}".format(client.user.name))
  print("ID: {}".format(client.user.id))

@client.event
async def on_message(message):
  await client.process_commands(message)
  if (message.author.bot) and (message.author.id == client.user.id): # checks if message is from bot
    global all_roles_list
    print(message.embeds)
    for embed in (message.embeds):
      for field in embed.fields:
        # print(field.name)
        print(field.value)
        value = field.value
        for i in range(len(all_roles_list)):
          if all_roles_list[i] in value:
            await message.add_reaction(all_roles_list[i])
  elif message.channel.id == 957465271830970389:
    general = message.guild.get_channel(957465202767564883)
    rules = message.guild.get_channel(957466979936129044)
    message = f'Welcome {message.author.mention}! Make sure to check {rules.mention} for server rules and roles.'
    await general.send(message)
  else:
    print(message.author.name)

@client.event
async def on_raw_reaction_add(payload):
  message_id = payload.message_id
  if payload.user_id != client.user.id: #checks if reaction is from bot
    print("Add role initiated")
    guild_id = payload.guild_id
    guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)
    value = payload.emoji.name
    # print(value) used in debugging
    global all_roles_list
    for i in range(len(all_roles_list)):
      if all_roles_list[i] in value:
        role = discord.utils.get(guild.roles, name=all_roles_dict[all_roles_list[i]])
        print(role)
        break
    if role is None:
      print("Role not found")
      await guild.create_role(name=all_roles_dict[all_roles_list[i]], mentionable=True)
      for i in range(len(all_roles_list)):
        if all_roles_list[i] in value:
          role = discord.utils.get(guild.roles, name=all_roles_dict[all_roles_list[i]])
          print(role)
          break
    member = payload.member
    if member:
      await role.edit(mentionable=True)
      await member.add_roles(role)
      print("success")
    else:
      print("Member not found")
  else:
    print("The bot reacted")
    print(payload.user_id)

@client.event
async def on_raw_reaction_remove(payload):
  message_id = payload.message_id
  if payload.user_id != client.user.id: #checks if reaction is from bot
    print("Remove role initiated")
    guild_id = payload.guild_id
    guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)
    value = payload.emoji.name
    # print(value) used in debugging
    global all_roles_list
    for i in range(len(all_roles_list)):
      if all_roles_list[i] in value:
        role = discord.utils.get(guild.roles, name=all_roles_dict[all_roles_list[i]])
        print(role)
        break
    if role is None:
      print("Role not found")
      await guild.create_role(name=all_roles_dict[all_roles_list[i]], mentionable=True)
      for i in range(len(all_roles_list)):
        if all_roles_list[i] in value:
          role = discord.utils.get(guild.roles, name=all_roles_dict[all_roles_list[i]])
          print(role)
          break
    member = get(guild.members, id=payload.user_id)
    if member:
      await role.edit(mentionable=True)
      await member.remove_roles(role)
      print("success")
    else:
      print("Member not found")
  else:
    print("The bot reacted")
    print(payload.user_id)

@client.event
async def on_member_join(member):
  guild = member.guild
  print(guild)
  rules = guild.get_channel(957466979936129044)
  intro = guild.get_channel(957465271830970389)
  pick_roles = guild.get_channel(745093331318734989)
  
  
  embed=discord.Embed(color=0xC99117, title="Welcome!", description=f"{member.mention}, Welcome to Cal Poly '26! Tell us a little bit about yourself in {intro.mention} to gain full access!\nUnsure how to do so? Check {rules.mention} for a quick example!")
  embed.set_thumbnail(url="https://media.discordapp.net/attachments/957716447755374673/957761766501257226/Cal-Poly-University-Seal.png")

  user = client.get_user(member.id)
  await user.send(embed=embed)



@client.command()
async def setroles(ctx):
  channel = ctx.message.channel
  if ctx.message.author.guild_permissions.administrator:
    async for message in channel.history(limit=200): # clears all of the bot messages in the channel
      if message.author == client.user:
        await message.delete()
    await ctx.message.delete()
    global special_roles
    # TODO remove previous messages the bot sent in the channel
    for key in special_roles.keys():
      embed=discord.Embed(color=0xFF0000)
      embed.add_field(name=f"Role Menu: {key}", value="React to give yourself a role.", inline=False)
      for subkeys in special_roles[key].keys():
        embed.add_field(name="\u200b", value=f'{subkeys} : {special_roles[key][subkeys]}', inline=False)
      await ctx.send(embed=embed)
  else:
    msg = f"Sorry {ctx.message.author.mention}, only Admins can use this command"
    await channel.send(msg)

@client.command()
async def test(ctx, *, arg):
  print(arg)
  await ctx.send(arg)

@client.command()
async def ping(ctx):
  print(ctx)
  await ctx.send(f'Pong! {round(client.latency * 1000)} ms')

client.run(getToken())