import ctypes
import os
import sys

import discord
import easygui
from anonfile import AnonFile
from discord.ext import commands
from dotenv import load_dotenv

ctypes.windll.kernel32.SetConsoleTitleW("anonuploader - login")
try:
    cols = os.get_terminal_size().columns
except (OSError, ValueError):
    cols = 0
os.system("cls")
if not os.path.isfile(".env"):
    with open(".env", "w") as f:
        f.write("TOKEN=\n")
load_dotenv()

ascii_art = r"""                                         .__                    .___            
_____    ____   ____   ____  __ ________ |  |   _________     __| _/___________ 
\__  \  /    \ /  _ \ /    \|  |  \____ \|  |  /  _ \__  \   / __ |/ __ \_  __ \
 / __ \|   |  (  <_> )   |  \  |  /  |_> >  |_(  <_> ) __ \_/ /_/ \  ___/|  | \/
(____  /___|  /\____/|___|  /____/|   __/|____/\____(____  /\____ |\___  >__|   
     \/     \/            \/      |__|                   \/      \/    \/     
   D  I  S  C  O  R  D   F  I  L  E   L  I  M  I  T   B  Y  P  A  S  S  E  R   
"""
print("\033[1;90m")
print("\n".join(line.center(cols) for line in ascii_art.splitlines()))
print("─" * cols)
print("This tool will never use your token for malicious purposes.".center(cols))

token = os.getenv("TOKEN")
anon = AnonFile()
client = commands.Bot(command_prefix="?", self_bot=True,
                      guild_subscription_options=discord.GuildSubscriptionOptions.off())
client.remove_command("help")


@client.command()
async def upload(ctx):
    await ctx.message.delete()
    file_path = easygui.fileopenbox()
    file_uploaded = anon.upload(file_path, progressbar=True)
    await ctx.send(file_uploaded.url.geturl())


@client.command()
async def stop(ctx):
    await ctx.message.delete()
    sys.exit(0)


# noinspection PyUnusedLocal
@client.event
async def on_command_error(ctx, error):
    pass


@client.event
async def on_ready():
    os.system("cls")
    await client.change_presence(status=discord.Status.dnd)
    ctypes.windll.kernel32.SetConsoleTitleW("anonuploader - ?upload")
    print("\033[1;90m")
    print("\n".join(line.center(cols) for line in ascii_art.splitlines()))
    print("─" * cols)
    print(f"Logged in as {str(client.user)}".center(cols))
    print("WARNING: This is a selfbot, it is not recommended to use this tool in public servers!".center(cols))


if __name__ == "__main__":
    try:
        client.run(token)
    except (discord.LoginFailure, AttributeError):
        sys.stderr = None
        print("\033[1;91m")
        print("I couldn't find a valid token to log in with.".center(cols))
        print("If this is your first time running this tool, please populate your token into '.env'.".center(cols))
        print("\033[0m")
        sys.exit(1)
