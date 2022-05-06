# invite link:
# https://discord.com/api/oauth2/authorize?client_id=744024313476415540&permissions=8&scope=bot
# run on heroku server and locally

import os
import psutil
from dotenv import load_dotenv

import discord
from discord.ext import commands
from discord.utils import get

from constants import *