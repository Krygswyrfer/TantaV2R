# ==============================     importing modules     ==============================

# from asyncio.events import new_event_loop
# from asyncio.windows_events import SelectorEventLoop
# from asyncio import streams
# from cgitb import text
from asyncio import streams
from discord.utils import get
import discord, asyncio, io, colorama, random
from discord import FFmpegPCMAudio
import time, requests, nekos, sys, os, config
from discord.ext.commands import cooldown, BucketType
# from discord.ext.commands.converter import MessageConverter
from discord.embeds import Embed
from youtube_dl import YoutubeDL
import random
from discord.ext import commands
from colorama import Fore, Back, Style 
from discord.ext.commands import has_permissions, CheckFailure
from config import *
# from datetime import datetime
from colorama import init
import aiohttp
import urllib.request,urllib.parse,urllib.error
import shelve
import keykeeper
import PrePrep



# ==============================     bot preparation, status and startup     ==============================


intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix="tn? ", intents=intents, help_command = None)
conf_bot_prefix = "tn? "
nsfw_enabled = True

queues = {}
def check_queue(ctx, id):
    if queues[id] != []:
        voice = ctx.guild.voice_client
        music = queues[id].pop(0)
        voice.play(music, after=lambda x=None: check_queue(ctx, ctx.message.guild.id))


@client.event
async def on_ready():
    gameStat = random.choice(PrePrep.playingList)
    watchStat = random.choice(PrePrep.watchingList)
    listenStat = random.choice(PrePrep.listeningList)
    streamStat = random.choice(PrePrep.streamingList)
    #await client.change_presence(activity=discord.Game(name=gameStat))
    #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=watchStat))
    #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=listenStat))
    await client.change_presence(activity=discord.Streaming(name=streamStat, url="https://www.twitch.tv/guavxx")) # "https://www.youtube.com/w
    print(f"Tanta is operational. Have at it.\nStatus message: {streamStat}")

@client.event
async def on_message(message):



    await client.process_commands(message)


# ==============================     generic commands     ==============================


@client.command()
async def help(ctx, specifier = None, page = None):  # One embed page should cover 10 commands
    user = ctx.message.author
    if page is None:
        page = "1"
    if specifier is None:
        embed = discord.Embed(title = "The helpful help list (Categories)", colour=PrePrep.colRan())
        embed.add_field(name="Generic", value='General utility commands\n`(6 commands)`', inline=False)
        embed.add_field(name="Images", value='Self explanatory image commands\n`(7 commands)`', inline=False)
        embed.add_field(name="VC", value='Unstable VC commands\n`(7 commands)`', inline=False)
        embed.add_field(name="Humour", value='Slightly humourous commands\n`(8 commands)`', inline=False)
        embed.add_field(name="Interaction", value='Commands for user-to-user interaction\n`12 commands`', inline=False)
        embed.add_field(name="Weeb", value='A neat collection of catgirl pictures and GIFs (not JIFs), plus other weeb stuff\n`11 commands`', inline=False)
        embed.add_field(name="NSFWeeb", value='NSFW weeb images and gifs to further fuel your degeneracy\n`26 commands`', inline=False)
        embed.set_footer(text = "Run tn? help [category] for more information")

    elif specifier.lower() == "generic":
        embed = discord.Embed(title = "The helpful help list (Generic commands)", colour = PrePrep.colRan())
        embed.add_field(name="delet", value='Banish messages to the Shadow Realm\n`Restricted Access`', inline=False)
        embed.add_field(name="help", value='Shows a helpful help list', inline=False)
        embed.add_field(name="terminate", value='A less efficient way to cleanly cease functionality\n`Restricted Access`', inline=False)
        embed.add_field(name="ping", value='Used to check if Tanta is still functioning', inline=False)
        embed.add_field(name="toggle", value='Toggle a command on or off\n`Restricted Access`', inline=False)
        embed.set_footer(text = "Run tn? help [command] for flavour text and command usage format")

    elif specifier.lower() == "images":
        embed = discord.Embed(title = "The helpful help list (Image commands)", colour = PrePrep.colRan())
        embed.add_field(name="clown", value='Clown someone', inline=False)
        embed.add_field(name="siegeop", value='Randomly pull an operator from the R6S roster', inline=False)
        embed.add_field(name="goose", value='A random goose image to laugh at', inline=False)
        embed.add_field(name="lizard", value='A random lizard image to look at', inline=False)
        embed.add_field(name="meowpic", value='A nice cat picture to admire', inline=False)
        embed.add_field(name="meowgif", value='A nice cat gif (not jif) to admire', inline=False)
        embed.add_field(name="mewofact", value='Not an image but a random cat fact', inline=False)
        embed.set_footer(text = "Run tn? help [command] for flavour text and command usage format")

    elif specifier.lower() == "vc":
        embed = discord.Embed(title = "The helpful help list (VC commands)", colour = PrePrep.colRan())
        embed.add_field(name="altplay", value='Play pre-determined music in a VC', inline=False)
        embed.add_field(name="curb", value='Curb your Enthusiasm', inline=False)
        embed.add_field(name="join", value='Summon Tanta to the VC\n`Restricted Access`', inline=False)
        embed.add_field(name="leave", value='Unsummon Tanta from the VC\n`Restricted Access`', inline=False)
        embed.add_field(name="pause", value='Stoppeth thy musick\n`Restricted Access`', inline=False)
        embed.add_field(name="resume", value='Thou doth desire thy musick\n`Restricted Access`', inline=False)
        embed.add_field(name="skip", value='Track suck, skip.\n`Restricted Access`', inline=False)
        embed.set_footer(text = "Run tn? help [command] for flavour text and command usage format")

    elif specifier.lower() == "humour":
        embed = discord.Embed(title = "The helpful help list (Humour commands)", colour = PrePrep.colRan())
        embed.add_field(name="gaymeter", value='Measure your gay level', inline=False)
        embed.add_field(name="identify", value='Learn what your pronoun is', inline=False)
        embed.add_field(name="iqcheck", value='Find out your IQ', inline=False)
        embed.add_field(name="psize", value='Tanta is not horny but she will measure your pp', inline=False)
        embed.add_field(name="likely", value='Tag 2 users and find out which of those 2 is more likely to do something', inline=False)
        embed.add_field(name="roulette", value='Place your life on the line and play Russian Roulette', inline=False)
        embed.add_field(name="rsstrivia", value='Learn some Rainbow Six Siege trivia', inline=False)
        embed.add_field(name="trivt", value='Play an un-fun trivia game', inline=False)
        embed.set_footer(text = "Run tn? help [command] for flavour text and command usage format")

    elif specifier.lower() == "interaction":
        if page == "1":
            embed = discord.Embed(title = f"The helpful help list (Interaction commands) Page 1/2", colour = PrePrep.colRan())
            embed.add_field(name="baka", value="Call someone a baka, simple as that", inline=False)
            embed.add_field(name="cuddle", value="Wholesome cuddling", inline=False)
            embed.add_field(name="feed", value="Wholesome feeding", inline=False)
            embed.add_field(name="gasm", value="Orgasm in awe to someone", inline=False)
            embed.add_field(name="hug", value="Wholesome hugging", inline=False)
            embed.add_field(name="kiss", value="Wholesome kissing", inline=False)
            embed.add_field(name="pat", value="Wholesome headpats", inline=False)
            embed.add_field(name="poke", value="Virtually annoy someone slightly", inline=False)
            embed.add_field(name="slap", value="Show your disdain for someone", inline=False)
            embed.add_field(name="smug", value="Idk, act smug to someone?", inline=False)
            embed.set_footer(text = "Run tn? help [command] for some flavour text and command usage format")
        elif page == "2":
            embed = discord.Embed(title = "The helpful help list (Interaction commands) Page 2/2", colour = PrePrep.colRan())
            embed.add_field(name="spank", value="Mete out as many beatings as you see fit", inline=False)
            embed.add_field(name="tickle", value="Be a mischievious scallywag", inline=False)
            embed.set_footer(text = "Run tn? help [command] for flavour text and command usage format")

    elif specifier.lower() == "weeb":
        if page == "1":
            embed = discord.Embed(title = "The helpful help list (Weeb commands) Page 1/2", colour = PrePrep.colRan())
            embed.add_field(name="waifu", value="Have a waifu", inline=False)
            embed.add_field(name="morewaifu", value="Have another waifu", inline=False)
            embed.add_field(name="neko", value="Have a catgirl", inline=False)
            embed.add_field(name="moreneko", value="Have another catgirl. Or...", inline=False)
            embed.add_field(name="nekogif", value="Have a neko in GIF (not JIF)", inline=False)
            embed.add_field(name="morenekogif", value="Have another neko in GIF (not JIF)", inline=False)
            embed.add_field(name="gecg", value="Spreading GECG awareness", inline=False)
            embed.add_field(name="foxgirl", value="Have a foxgirl", inline=False)
            embed.add_field(name="randem", value="View a contextually irrelevant and random image", inline=False)
            embed.add_field(name="avatar", value="Have a new avatar picture", inline=False)
            embed.set_footer(text = "Run tn? help [command] for flavour text and command usage format")

        elif page == "2":
            embed = discord.Embed(title = "The helpful help list (Interaction commands) Page 2/2", colour = PrePrep.colRan())
            embed.add_field(name="quotes", value="Retrieve a random quote from a random anime", inline=False)
            embed.set_footer(text = "Run tn? help [command] for flavour text and command usage format")

    elif specifier.lower() == "nsfweeb":
        if page == "1":
            embed = discord.Embed(title = "The helpful help list (NSFW weeb commands) Page 1/3", colour = PrePrep.colRan())
            embed.add_field(name="feet", value="Feet pics", inline=False)
            embed.add_field(name="yuri", value="Yuri pics", inline=False)
            embed.add_field(name="trap", value="Trap pics", inline=False)
            embed.add_field(name="futanari", value="Futanari pics", inline=False)
            embed.add_field(name="hololewd", value="Hololewd pics", inline=False)
            embed.add_field(name="lewdkemo", value="Lewdkemo pics", inline=False)
            embed.add_field(name="cum", value="Lots of it", inline=False)
            embed.add_field(name="erokemo", value="Erokemo pics", inline=False)
            embed.add_field(name="les", value="Les pics", inline=False)
            embed.add_field(name="wallpaper", value="A wallpaper", inline=False)
            embed.set_footer(text = "Run tn? help [command] for flavour text and command usage format")
            
        elif page == "2":
            embed = discord.Embed(title = "The helpful help list (NSFW weeb commands) Page 2/3", colour = PrePrep.colRan())
            embed.add_field(name="lewdk", value="Lewdk pics", inline=False)
            embed.add_field(name="lewd", value="More lewd pics", inline=False)
            embed.add_field(name="eroyuri", value="Enhanced yuri pics... erotic.", inline=False)
            embed.add_field(name="eron", value="Eron pics", inline=False)
            embed.add_field(name="bj", value="BJ pics", inline=False)
            embed.add_field(name="nsfw_neko_gif", value="Pretty self-explanatory", inline=False)
            embed.add_field(name="solo", value="NSFW solo image", inline=False)
            embed.add_field(name="kemonomimi", value="Kemonomimi pictures", inline=False)
            embed.add_field(name="kuni", value="Kuni gifs (not jifs)", inline=False)
            embed.add_field(name="nsfw_avatar", value="It's a new avatar for you, Horny McGee", inline=False)
            embed.set_footer(text = "Run tn? help [command] for flavour text and command usage format")

        elif page == "3":
            embed = discord.Embed(title = "The helpful help list (NSFW weeb commands) Page 3/3", colour = PrePrep.colRan())
            embed.add_field(name="anal", value="Anal pics", inline=False)
            embed.add_field(name="hentai", value="Self-explanatory enough", inline=False)
            embed.add_field(name="erofeet", value="Enhanced feet pics", inline=False)
            embed.add_field(name="pussy", value="Pussy pics... bleurgh.", inline=False)
            embed.add_field(name="tits", value="Go figure", inline=False)
            embed.add_field(name="boobs", value="Do you really need me to explain this", inline=False)
            embed.set_footer(text = "Run tn? help [command] for flavour text and command usage format")

    #       =====   Generic help    =====

    elif specifier.lower() == "delet":
        embed = discord.Embed(title = "tn? delet [integer]", description = "Deletes a specified number of messages from the channel the command \
was issued in. Does not include the command as a message. Defaults to 1 if a number is not specified.\n`Restricted Access`", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "help":
        embed = discord.Embed(title = "tn? help", description = "Well no shit it shows the helpful \
help list what do you think?", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "terminate":
        embed = discord.Embed(title = "tn? terminate", description = "An alternative way to stop the bot after VC issues, now redundant \
due to VC commands being unavailable.\n`Restricted Access`", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "ping":
        embed = discord.Embed(title = "tn? ping", description = "A simple ping command to chcek if Tanta is still actively listening \
for commands.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "toggle":
        embed = discord.Embed(title = "tn? toggle <command> <enable|disable>", description = "Enable or disable a specified command, \
still somewhat unstable.\n`Restricted Access`", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    #       =====   Image help  =====

    elif specifier.lower() == "clown":
        embed = discord.Embed(title = "tn? clown [user]", description = "Show someone what they really are: not a clown.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "siegeop":
        embed = discord.Embed(title = "tn? siegeop", description = "Randomly select a Rainbow Six Siege operator to display. Yes, \
Recruit is included. Yes, old Tachanka is included.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "goose":
        embed = discord.Embed(title = "tn? goose", description = "Look, a goose.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "lizard":
        embed = discord.Embed(title = "tn? lizard", description = "Look, a lizard.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "meowpic":
        embed = discord.Embed(title = "tn? meowpic", description = "A picture with cats in it.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "meowgif":
        embed = discord.Embed(title = "tn? meowgif", description = "A GIF (not JIF) with cats in it.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "meowfact":
        embed = discord.Embed(title = "tn? meowfact", description = "A fact about cats, because you can't spell \"Fact\" without \
the letters of \"cat\".", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    #       =====   VC help =====

    elif specifier.lower() == "altplay":
        embed = discord.Embed(title = "tn? altplay", description = "Due to ytdl being funny, this cheap workaround method is now \
used to play a pre-selected track.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "curb":
        embed = discord.Embed(title = "tn? curb", description = "Play the universal \"Bruh Moment\" theme song.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "join":
        embed = discord.Embed(title = "tn? join", description = "If Tanta is not already in your VC, she will connect to it upon \
issuing this command.\n`Restricted Access`", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "leave":
        embed = discord.Embed(title = "tn? leave", description = "If Tanta is in your VC, she will disconnect upon issuing this \
command.\n`Restrictedd Access`", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "pause":
        embed = discord.Embed(title = "tn? pause", description = "If Tanta is playing a track, she will temporarily stop playing \
it.\n`Restricted Access`", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "resume":
        embed = discord.Embed(title = "tn? resume", description = "If Tanta has paused the track she was playing, she will continue \
playing that track.\n`Restricted Access`", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "skip":
        embed = discord.Embed(title = "tn? skip", description = "Forcefully skips the currently playing track.\
\n`Restricted Access`", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    #       =====   Humour help   =====

    elif specifier.lower() == "gaymeter":
        embed = discord.Embed(title = "tn? gaymeter [user]", description = "Issue this command to find out how gay you are.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "identify":
        embed = discord.Embed(title = "tn? identify [user]", description = "People keep coming up with new pronouns to identify as, \
so today you shall find out what you identify as.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "iqcheck":
        embed = discord.Embed(title = "tn? iqcheck [user]", description = "Issue this command to find out your IQ.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "psize":
        embed = discord.Embed(title = "tn? psize [user]", description = "Issue this command to find out your pp length.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "likely":
        embed = discord.Embed(title = "tn? likely <user> <user> <action>", description = "Tag 2 users and find out which of the \
2 users is more likely to perform a specified action.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "roulette":
        embed = discord.Embed(title = "tn? roulette [user]", description = "Risk yor life and spin the revolver to play \
Russian Roulette.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "rsstrivia":
        embed = discord.Embed(title = "tn? rsstrivia", description = "Some Rainbow Six Trivia trivia stuff you may or \
may not know.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "trivt":
        embed = discord.Embed(title = "tn? trivt [question id]", description = "Request a random trivia question to answer \
within 14 seconds. Questions are heavily based on developer interests. Entering a number will display the question \
with that specific ID, if it exists.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    #       =====   Interaction help   =====

    elif specifier.lower() == "baka":
        embed = discord.Embed(title = "tn? baka <user>", description = "Show someone how big of a fool they are for not knowing \
about your 70 alternative accounts.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "cuddle":
        embed = discord.Embed(title = "tn? cuddle <user>", description = "Cuddle someone to make someone feel better or awkward. \
Wasn't it obvious?", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "feed":
        embed = discord.Embed(title = "tn? feed <user>", description = "Feed someone as you would feed a young catgirl. Fantasies \
have no boundaries.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")
    
    elif specifier.lower() == "gasm":
        embed = discord.Embed(title = "tn? gasm <user>", description = "I have no words for this one.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "hug":
        embed = discord.Embed(title = "tn? hug <user>", description = "Awkward hug. Wholesome hug. Viral hug.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "kiss":
        embed = discord.Embed(title = "tn? kiss <user>", description = "Fortunately for you, mutual consent is not required for \
this command.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "pat":
        embed = discord.Embed(title = "tn? pat <user>", description = "Headpats. Pat pat pat.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "poke":
        embed = discord.Embed(title = "tn? poke <user>", description = "Poke someone with an arbitrarily decided amount of strength.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "slap":
        embed = discord.Embed(title = "tn? slap <user>", description = "DON'T MAKE ME SLAP YOU AGAIN! DON'T MAKE ME SLAP YOU.\n(Bonus \
cookie if you got the reference)", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "smug":
        embed = discord.Embed(title = "tn? smug <user>", description = "Idk just roll with it", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "spank":
        embed = discord.Embed(title = "tn? spank <user>", description = "Spank someone like that scene from Tom and Jerry, \
but different.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "tickle":
        embed = discord.Embed(title = "tn? tickle <user>", description = "The tickle command allows you to tickle someone. \
I know, crazy, right? Who would've though that the tickle command tickles someone?", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    #       =====   Weeb help   =====

    elif specifier.lower() == "waifu":
        embed = discord.Embed(title = "tn? waifu", description = "A waifu for you, if that's what you really desire.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "morewaifu":
        embed = discord.Embed(title = "tn? morewaifu", description = "Expended the waifu library already? I knew it. Have more with this \
command, I guess.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "neko":
        embed = discord.Embed(title = "tn? neko", description = "Catgirls, how adorable.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "moreneko":
        embed = discord.Embed(title = "tn? moreneko", description = "A second collection of catgirls. I have a feeling that the \
first library isn't going to be enough. And just for fun...", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "nekogif":
        embed = discord.Embed(title = "tn? nekogif", description = "These catgirls can move, because they are in the Graphics \
(not Jraphics) Interchange Format.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "morenekogif":
        embed = discord.Embed(title = "tn? mormenekogif", description = "Even more catgirl GIFs (not JIFs). Admittedly, this \
will probably get emptied out very quickly.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "gecg":
        embed = discord.Embed(title = "tn? gecg", description = "A pre-formatted image talking about genetically-engineered \
catgirls, though that's not why you run this command, I presume.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "foxgirl":
        embed = discord.Embed(title = "tn? foxgirl", description = "Introducing variation while retaining similarity. \
Have a foxgirl.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "randem":
        embed = discord.Embed(title = "tn? randem", description = "What image will this command give you? Ha ha, I have \
no idea!\n(Bonus cookie if you get the reference)", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "avatar":
        embed = discord.Embed(title = "tn? avatar", description = "For those who want an avatar but are too lazy to go \
find one.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "quotes":
        embed = discord.Embed(title = "tn? quotes", description = "Some random quote from a random character from a random \
anime. Sigh...", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    #       =====   NSFW help   =====

    elif specifier.lower() == "feet":
        embed = discord.Embed(title = "tn? feet", description = "Feet pics for you foot fetish freaks.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "yuri":
        embed = discord.Embed(title = "tn? yuri", description = "Dev note: I'd much rather Yuri from Modern Warfare 3", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "trap":
        embed = discord.Embed(title = "tn? trap", description = "No, these are not mouse traps, if that's what you're wondering.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "futanari":
        embed = discord.Embed(title = "tn? futanari", description = "If you know, you know.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "hololewd":
        embed = discord.Embed(title = "tn? hololewd", description = "Hmm I forgot what this is for.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "lewdkemo":
        embed = discord.Embed(title = "tn? ", description = " Lewd kemo images for you horny weirdos.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "cum":
        embed = discord.Embed(title = "tn? cum", description = "I do believe elaboration isn't neecessary.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "erokemo":
        embed = discord.Embed(title = "tn? erokemo", description = "Erotic kemo images. What, you trying to fail NNN?", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "les":
        embed = discord.Embed(title = "tn? les", description = "My knowledge on this is rather narrow. I can't tell you much.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "wallpaper":
        embed = discord.Embed(title = "tn? wallpaper", description = "Very self-explanatory. Comes in both 4:3 and 9:16 \
screen ratios for computers and mobile phones, respectively.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "lewdk":
        embed = discord.Embed(title = "tn? lewdk", description = "Idk this came along with the rest so just roll with it", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "lewd":
        embed = discord.Embed(title = "tn? lewd", description = "Lewd images. What were you expecting?", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "eroyuri":
        embed = discord.Embed(title = "tn? eroyuri", description = "Yuri images, but erotic...?", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "eron":
        embed = discord.Embed(title = "tn? eron", description = "I have no idea what I'm doing just know that this is an NSFW command", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "bj":
        embed = discord.Embed(title = "tn? bj", description = "No, it's not about Blackjack, if you were wondering.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "nsfw_neko_gif":
        embed = discord.Embed(title = "tn? nsfw_neko_gif", description = "The command says it all, doesn't it.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "solo":
        embed = discord.Embed(title = "tn? solo", description = "An NSFW solo image, I think? Idk I just took the original \
description.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "kemonomimi":
        embed = discord.Embed(title = "tn? kemonomimi", description = "Approved by TR High Command. This is a pleasant one.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "kuni":
        embed = discord.Embed(title = "tn? kuni", description = "Kuni GIFs (not JIFs). Don't believe me? See for yourself.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "nsfw_avatar":
        embed = discord.Embed(title = "tn? nsfw_avatar", description = "For those who want a spicier avatar but are too \
lazy or embarassed to find one themselves.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "anal":
        embed = discord.Embed(title = "tn? anal", description = "You, uh... I doubt I need to tell you what this is.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "hentai":
        embed = discord.Embed(title = "tn? hentai", description = "Going straight for \"hentai\"? I really have nothing to \
say.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "erofeet":
        embed = discord.Embed(title = "tn? erofeet", description = "Erotic feet pics, since the normal ones (foot fetish, \
normal?) weren't good enough for you, apparently.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "pussy":
        embed = discord.Embed(title = "tn? pussy", description = "You know. I have no words for you.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "tits":
        embed = discord.Embed(title = "tn? tits", description = "You searched for help on this? Are you serious? The command \
name says it all.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "boobs":
        embed = discord.Embed(title = "tn? boobs", description = "The command name isn't clear enough?", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    await ctx.send(embed = embed)
    print(f"Command pull: tn? help {specifier} {page} requested by {user}.")
    

@client.command()
async def ping(ctx):
    user = ctx.message.author
    latency = round(client.latency * 1000)
    if ctx.author.id in PrePrep.cmdWhitelist:
        reply = "**Affirmative ☭**"
        greeting = "Pleasant evening"
    else:
        reply = "**Loud and clear**"
        greeting = "Good day"
    weapon = random.choice(PrePrep.planetguns)
    embed = discord.Embed(title = reply, description = f"Latency:  `{latency}ms`\nFeatured infantry weapon:  `{weapon}`", colour = PrePrep.colRan())
    embed.set_footer(text=f"{greeting}, {user}.")
    await ctx.send(embed = embed)
    print(f"Command pull: tn? ping requested by {user}")


@client.command()
async def delet(ctx, amount = 1):
    if ctx.author.id in PrePrep.cmdWhitelist:
        user = ctx.message.author
        await ctx.channel.purge(limit=amount + 1)
        print(f"Requested by {user}: Deleted {amount}+1 messages.")
    else:
        await ctx.send("Request could not be processed. Please check that you have requested the required permissions to run \
this command and try again.")
        print(f"Command pull: tn? delet requested by {ctx.message.author}. Failed.")


@client.command()
async def toggle(ctx, cmd = None, toggler = None):
    if ctx.author.id in PrePrep.cmdWhitelist:
        if cmd is None:
            await ctx.send("Specify a command to toggle.")
        elif toggler is None:
            await ctx.send("Run it again, but this time specify if you want to `enable` or `disable`.")
        elif toggler == "disable":
            command = client.get_command(cmd)
            command.update(enabled=False)
            await ctx.send("`{}` has been disabled.".format(cmd))
        elif toggler == "enable":
            command = client.get_command(cmd)
            command.update(enabled=True)
            await ctx.send("`{}` has been enabled.".format(cmd))
    else:
        await ctx.send("No, you can't toggle commands.")
    

@client.command()
async def terminate(ctx):
    if ctx.author.id in PrePrep.cmdWhitelist:
        await ctx.send("Running `exit()`...")
        if os.path.isfile('song.mp3'):
            os.remove("song.mp3")
        exit()
    else:
        await ctx.send("Stop trying to kill me >:( you're hurting my feelings")


@client.command()
async def link(ctx):
    await ctx.send("https://discord.com/api/oauth2/authorize?client_id=860093850226786315&permissions=1165312&scope=bot")


@client.command()
async def custom(ctx, user: discord.Member = None, *args):
    if user is None:
        await ctx.send("How about actually mentioning someone for me to dm?")
    elif args is None or args == "":
        await ctx.send("I won't send an empty DM, dummy.")
    else:
        await ctx.channel.purge(limit=1)
        sender = ctx.message.author
        sender = sender.mention
        await user.send(" ".join(args[:]))
        print("Custom DM sent.")


@client.command()
async def findav(ctx, user: discord.Member = None):
    if user is None:
        await ctx.send("Mention a user or specify their ID.")
    else:
        pfp = user.avatar_url
        embed = discord.Embed(title = f"Retrieving avatar for {str(user)}", url = f"{pfp}", colour = PrePrep.colRan())
        embed.set_image(url = f"{pfp}")
        embed.set_footer(text=f"Pleasant evening, {str(ctx.message.author)}")
        await ctx.send(embed=embed)

        
@client.command()
# async def findbn(ctx, user: discord.Member = None):
#     if user is None:
#         await ctx.send("Mention a user or specify their ID.")
#     else:
#         pfp = user.banner.url
#         embed = discord.Embed(title = f"Retrieving avatar for {str(user)}", url = f"{pfp}", colour = PrePrep.colRan())
#         embed.set_image(url = f"{pfp}")
#         embed.set_footer(text=f"Pleasant evening, {str(ctx.message.author)}")
#         await ctx.send(embed=embed)
async def banner(ctx, user:discord.Member = None):
    if user == None:
        user = ctx.author
    req = await client.http.request(discord.http.Route("GET", "/users/{uid}", uid=user.id))
    banner_id = req["banner"]
    # If statement because the user may not have a banner
    if banner_id:
        banner_url = f"https://cdn.discordapp.com/banners/{user.id}/{banner_id}?size=1024"
        await ctx.send(f"{banner_url}")




# ==============================     humour commands     ==============================


@client.command()
async def trivt(ctx, id = None):
    wrongList = [
        "Nein, incorrect.",
        "No, no no.",
        "Wrong answer identified.",
        "Not the right answer, unfortunately.",
        "Nyet, no bueno.",
        "Wrong option mate.",
        "Err, no, that's incorrect.",
    ]
    rightList = [
        "That is indeed the answer.",
        "Right on. Did you just guess?",
        "Smartass.",
        "Well, that's correct.",
        "You're right, though it feels like you guessed.",
        "Usually I'd say you're incorrect, but this time, you're correct.",
        "Yep, that's right.",
    ]
    afkList = [
        "do reply next time.",
        "were you AFK?",
        "how rude of you to ignore me.",
        "too busy reading the question?",
        "did you pretend to run out of time?",
        "are you still there?",
        "you're gonna have to answer on time.",
    ]
    user = ctx.author.mention
    newDict = list(PrePrep.trivt_list.keys())
    var = newDict[-2]
    if id is None:
        randomiser = random.randint(1,var)
    elif id == "id":
        if str(ctx.author) in PrePrep.cmdWhitelist:
            await ctx.send(f"Trivia question IDs currently span from `1` to `{str(var)}`.")
        else:
            await ctx.send("Return error. Missing permissions.")
        return
    else:
        randomiser = int(id)
        if randomiser not in PrePrep.trivt_list:
            await ctx.send("No trivia questions with that ID exist.")
            return
    question = PrePrep.trivt_list[randomiser]["question"]
    answer = PrePrep.trivt_list[randomiser]["answer"]
    ans1 = PrePrep.trivt_list[randomiser]["ans1"]
    ans2 = PrePrep.trivt_list[randomiser]["ans2"]
    ans3 = PrePrep.trivt_list[randomiser]["ans3"]
    ans4 = PrePrep.trivt_list[randomiser]["ans4"]
    ansformat = PrePrep.trivt_list[randomiser][f"ans{answer}"]

    body = (f"{question} {user}\n\n`1. {ans1}`\n`2. {ans2}`\n`3. {ans3}`\n`4. {ans4}`\n\nEnter `1`, `2`, `3`, or `4`.")
    embed = discord.Embed(title=f"Trivia question for {ctx.message.author}", description=body, colour = PrePrep.colRan())
    embed.set_footer(text="You have 14 seconds to answer.")
    await ctx.send(embed = embed)

    def check(m: discord.Message):
        return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id
    
    try:
        message = await client.wait_for(event = "message", check = check, timeout = 14)
        if message.content == answer:
            await ctx.send(random.choice(rightList))
            print(f"Command pull: tn? trivt requested by {ctx.message.author}. ID: {randomiser}. Correct. ") # Logging purposes
        else:
            await ctx.send(f"{random.choice(wrongList)} The correct answer was `{ansformat}`.")
            print(f"Command pull: tn? trivt requested by {ctx.message.author}. ID: {randomiser}. Incorrect. ") # Logging purposes
    except asyncio.TimeoutError:
        await ctx.send(f"Hey {user}, {random.choice(afkList)} The answer was `{ansformat}`.")
        print(f"Command pull: tn? trivt requested by {ctx.message.author}. ID: {randomiser}. Did not answer. ") # Logging purposes
        return


@client.command()
async def psize(ctx, user: discord.Member = None):
    if user is None:
        user = ctx.message.author
    pSize = random.randint(1, 10)
    list = [
        "pre-processed sausage",
        "schlong",
        "pickle",
        "*Wienerschnitzel*",
        "meat flopper",
        "piranah bait",
        "piss hose",
        "battering ram",
    ]
    noun = random.choice(list)
    if str(user) in PrePrep.cmdWhitelist:
        await ctx.send("No, this is not how you're supposed to play the game.")
    else:
        user = user.mention
        if pSize == 1:
            embed = discord.Embed(title = f"Your {noun} is **1** inch", description = f"This is an absolute maximum \
funny moment. {user}", colour = PrePrep.colRan())

        elif pSize == 2 or pSize == 3:
            embed = discord.Embed(title = f"Your {noun} is **{pSize}** inches", description = f"Neither impreessive\
nor impressive. {user}", colour = PrePrep.colRan())

        elif pSize >= 4 and pSize <= 6:
            embed = discord.Embed(title = f"Your {noun} is **{pSize}** inches.", description = f"Now that's something. {user}", colour = PrePrep.colRan())

        elif pSize == 7 or pSize == 8:
            embed = discord.Embed(title = f"Your {noun} is **{pSize}** inches.", description = f"Quite an achievemenet. {user}", colour = PrePrep.colRan())

        else:
            embed = discord.Embed(title = f"Your {noun} is **{pSize}** inches.", description = f"The ruler's verdict \
must be incorrect, that's hacking. {user}", colour = PrePrep.colRan())
        
        await ctx.send(embed = embed)


@client.command()
async def iqcheck(ctx, user: discord.Member = None):
    if user is None:
        user = ctx.message.author
    if str(user) in PrePrep.cmdWhitelist:
        await ctx.send("Good question.")
    else:
        iq = random.randint(-50, 200)
        user = user.mention
        if iq <0:
            embed = discord.Embed(title = f"You have **{iq}** IQ", description = f"A negative value! At least you \
still have a higher IQ than flat-earthers and anti-vaxxers. {user}", colour = PrePrep.colRan())
        
        elif iq >= 0 and iq < 69:
            embed = discord.Embed(title = f"You have **{iq}** IQ", description = f"That's an \"Extremely Low\" on the \
Wechsler Adult Intelligence Scale. Seems like your brain could use a software update. {user}", colour = PrePrep.colRan())

        elif iq >= 70 and iq <= 79:
            embed = discord.Embed(title = f"You have **{iq}** IQ", description = f"The Wechsler Adult Intelligence Scale \
classifies that as \"Borderline\". That's a yikes. {user}", colour = PrePrep.colRan())

        elif iq >= 80 and iq <= 89:
            embed = discord.Embed(title = f"You have **{iq}** IQ", description = f"\"Low Average\" says the Wechsler Adult\
Intelligence Scale. Come on, you're not that dull. {user}", colour = PrePrep.colRan())

        elif iq >= 90 and iq < 110:
            embed = discord.Embed(title = f"You have **{iq}** IQ", description = f"So you're \"Average\". Or, at least\
that's what the Wechsler Adult Intelligence Scale says. Ever wanted to become smarter? {user}", colour = PrePrep.colRan())

        elif iq >= 110 and iq <120:
            embed = discord.Embed(title = f"You have **{iq}** IQ", description = f"You have been classified as \"High Average\" \
by the Wechsler Adult Intelligence Scale. Just don't go around asserting your dominance. {user}", colour = PrePrep.colRan())

        elif iq >= 120 and iq < 130:
            embed = discord.Embed(title = f"You have **{iq}** IQ", description = f"Wechsler Adult Intelligence Scale \
classification: \"Superior\". We call this Intellectual Superiority. {user}", colour = PrePrep.colRan())
            embed.set_footer(text = "Bonus 10 IQ and a cookie if you understood the reference.")

        else:
            embed = discord.Embed(title = f"You have **{iq}** IQ", description = f"You are, in the eyes of the Wechsler Adult \
Intelligence Scale, \"Very Superior\". Now do us proud and pull off some 300 IQ plays. {user}", colour = PrePrep.colRan())

    await ctx.send(embed = embed)


@client.command()
async def gaymeter(ctx, user: discord.Member = None):
    if user is None:
        user = ctx.message.author
    gayFactor = random.randint(0, 101)
    user = user.mention
    if str(user) in PrePrep.cmdWhitelist:
        embed = discord.Embed(title = "Gaymeter verdict", description = f"{user} has a gay rating of **{0}%**", colour = PrePrep.colRan())
        await ctx.send(embed = embed)
    else:
        if gayFactor == 101:
            embed = discord.Embed(title = "Gaymeter verdict", description = f"{user} has a gay rating of **{gayFactor}%**", colour = PrePrep.colRan())
            embed.set_footer(text = "Margin of error: 1%")
        else:
            embed = discord.Embed(title = "Gaymeter verdict", description = f"{user} has a gay rating of **{gayFactor}%**", colour = PrePrep.colRan())
        await ctx.send(embed = embed)


@client.command()
async def identify(ctx, user: discord.Member = None):
    if user is None:
        user = ctx.message.author
    user = user.mention
    if user == "<@!521293177315917850>":
        await ctx.send("<@!521293177315917850> is a **PlanetMan**. Also one of my degenerate ass weeb developers.")
    elif user == "<@!591074600411070502>":
        await ctx.send("<@!591074600411070502> is the **Goose King**. Also one of my degenerate ass weeb developers.")
    else:
        variable = ["Microsoft Xbox 360 Video Game Console",
                    "Boeing AH-64 Apache Attack Helicopter",
                    "Ford Mustang 1985 GT Hatchback",
                    "Lockheed Martin AC-130 Gunship",
                    "McDonnell Douglas AV-8B Harrier II Jump Jet",
                    "Sikorsky MH-53 Pave Low Helicopter",
                    "Hamilton Beach Electric Panini Press Grill",
                    "Nerf Modulus Longstrike",
                    "Catgirl",
                    "Subway Chicken & Bacon Ranch Melt Sandwich",
                    "Run Down McDonald's Ice Cream Machine",
                    "Block of Redstone",
                    "A330-743L Airbus BelugaXL",
                    "NYPD Police Pursuit Vehicle",
                    "Vanu Proton II Pulsed Particle Accelerator (PPA)",
                    "Ukrainian SSR Antonov An-225 Mriya Airlifter",
                    "Northrop Grumman B-2 Spirit Stealth Bomber",
                    "Krupp Bagger 288 Bucket-wheel Excavator",
                    "Bede BD-5 Micro Single-seat Homebuilt Aircraft",
                    "Bottle of Gordon Ramsay's Unfound Lamb Sauce",
                    "HVM Twin Barrel MEP Rocket Launcher",
                    "3/8\" Polyvinyl Chloride Pipe",
                    "G52-Tactical Shield",
                    "Solution of 0.2mol/dm3 Potassium Permanganate",
                    "male",
                    "female",
                    "non-binary",
        ]
        await ctx.send("{} is a **{}**.".format(user, random.choice(variable)))


@client.command()
async def likely(ctx, user: discord.Member = None, user1: discord.Member = None, *args):
    if user is None or user1 is None:
        await ctx.send("You need to mention two users and specify what they would do, dummy."
                       "\n\nExample: `tn? likely @Joe @Yuri eat a cockroach`")
    else:
        user = user.mention
        user1 = user1.mention
        factor = random.randint(0, 1)
        await ctx.send("In response to: " + "`" + " ".join(args[:]) + "`")
        time.sleep(1.3)
        if factor == 0:
            await ctx.send("{} would be more likely to do that.".format(user1))
        elif factor == 1:
            await ctx.send("{} would be more likely to do that.".format(user))


@client.command()
async def roulette(ctx, user: discord.Member = None):
    bullet = random.randint(1, 6)
    if user is None:
        user = ctx.message.author
        
    if (user.mention == "<@!521293177315917850>" and ctx.author.id == 521293177315917850) or (user.mention == \
"<@!591074600411070502>" and ctx.author.id == 591074600411070502):
        embed = discord.Embed(title=f'{user} has **SURVIVED**.', description = f'Why did you try to kill yourself?')
        await ctx.send(embed=embed)

    elif user.mention == "<@!521293177315917850>" or user.mention == "<@!591074600411070502>":
        embed1 = discord.Embed(title=f'{user} has **SURVIVED**.', description = f'Under Line 34 of the Law of the \
Statements, developers like {user.mention} are exempt from the roulette.')
        await ctx.send(embed=embed1)
    
    else:        
        if bullet < 6:
            embed = discord.Embed(title=f'{user} has been shot and **DIED**.', description=f'I offer my Sincerest Contrafibularities.')
            await ctx.send(embed=embed)
        elif bullet == 6: 
            embed2 = discord.Embed(title=f'{user} has **SURVIVED**.', description=f'Nice one buddy, you almost killed yourself.')
            await ctx.send(embed=embed2)
        else: 
            await ctx.send("Something is Wrong")


# ==============================     beta currency commands     ==============================


@client.command()
@commands.cooldown(rate= 1, per=60, type=BucketType.user)
async def income(ctx):
    user = ctx.message.author
    userFormat = user.mention
    var = shelve.open("TantaMons")
    cashIn = random.randint(20, 100)
    user = str(user)
    if user in var:
        var[user] += cashIn
    elif user not in var:
        var[user] = cashIn
    var.close()
    await ctx.send(f"Received {cashIn}☭ {userFormat}")

@income.error
async def income_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(title="Spamming too fast?", description=f"Try running it again after `{round(error.retry_after)}` seconds.", colour = PrePrep.colRan())
        embed.set_footer(text="Income cooldown is 60 seconds.")
        await ctx.send(embed=embed)


@client.command()
async def leftover(ctx, user: discord.Member = None):
    if user is None:
        user = ctx.message.author
    userFormat = user.mention
    var = shelve.open("TantaMons")
    user = str(user)
    if user not in var:
        var[user] = 0
    balance = var[user]
    await ctx.send(f"{userFormat} currently has {balance}☭.")
    var.close()


@client.command()
async def spend(ctx, spent = None):
    user = str(ctx.message.author)
    userFormat = ctx.author.mention
    var = shelve.open("TantaMons")
    if spent is None:
        await ctx.send("Specify an amount to spend")
    else:
        spent = int(spent)
        balance = var[user]
        if spent > balance:
            await ctx.send("Spending too much.")
        elif spent <= 0:
            await ctx.send("Spend *something*.")
        else:
            var[user] -= spent
            balance = var[user]
            await ctx.send(f"Spent {spent}☭. You now have {balance}☭. {userFormat}")
    var.close()


@client.command()
async def strip(ctx, user: discord.Member = None):
    var = shelve.open("TantaMons")
    userFormat = user.mention
    if user is None:
        user = str(ctx.message.author)
    if str(user) not in var:
        await ctx.send("No such user with the specified ID.")
    else:
        user = str(user)
        await ctx.send(f"Eject {userFormat} from the currency system? Reply `y` within 10 seconds to confirm. Reply with anything else to cancel.")

        def check(m: discord.Message):
            return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id
        
        try:
            message = await client.wait_for(event = "message", check = check, timeout = 10)
            MessageContent = message.content
            if MessageContent.lower() == "y":
                var.pop(user)
                await ctx.send("User has been ejected.")
            else:
                await ctx.send("Procedure terminated")
        except asyncio.TimeoutError:
            await ctx.send("Reply not received. Procedure terminated.")
            return  
    var.close()


@client.command()
async def setcash(ctx, amount = None, user: discord.Member = None):
    try:
        if user is None:
            user = ctx.message.author
        if str(ctx.message.author) != "Krygswyrfer#8394":
            await ctx.send("Missing permissions.")
        elif int(amount) < 0:
            await ctx.send("Set *something*.")
        else:
            var = shelve.open("TantaMons")
            var[str(user)] = int(amount)
            await ctx.send(f"Set {user}'s currency to {amount}☭.")
    except:
        await ctx.send("Command format error. Check member and amount to set.")
    

# ==============================     vc commands     ==============================


@client.command(pass_context=True)
async def join(ctx):
    if ctx.author.id not in PrePrep.cmdWhitelist:
        await ctx.send("Nah, would rather not let you handle this command.")
    else:
        if ctx.author.voice:
            channel = ctx.message.author.voice.channel
            voice = await channel.connect()
        else:
            await ctx.send("Tanta can't join you if you're not in a VC, dummy.")


@client.command()
async def play(ctx, url):
    try:
        if ctx.author.voice:
            channel = ctx.message.author.voice.channel
            voice = await channel.connect()
        else:
            await ctx.send("Tanta can't join you if you're not in a VC, dummy.")
    except:
        print("Placeholder message. Proceeding as normal.")
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
    FFMPEG_OPTIONS = {
        'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    voice = get(client.voice_clients, guild=ctx.guild)

    if not voice.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['url']
        music = FFmpegPCMAudio(URL, **FFMPEG_OPTIONS)
        try:
            voice.play(music, after=lambda x=None: check_queue(ctx, ctx.message.guild.id))
            voice.is_playing()
            await ctx.send(f'Track has been loaded and should hopefully be playing.')
        except:
            await ctx.send("Seems like an error occured.")

    else:
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['url']
        music = FFmpegPCMAudio(URL, **FFMPEG_OPTIONS)
        guild_id = ctx.message.guild.id
        if guild_id in queues:
            queues[guild_id].append(music)
        else:
            queues[guild_id] = [music]
        await ctx.send("Track has been queued.")
        return


@client.command(pass_context=True)
async def leave(ctx):
    if ctx.author.id not in PrePrep.cmdWhitelist:
        await ctx.send("Nah, would rather not let you handle this command.")
    else:
        if (ctx.voice_client):
            await ctx.guild.voice_client.disconnect()
            if os.path.isfile('song.mp3'):
                os.remove("song.mp3")
            await ctx.message.delete()
        else:
            await ctx.send("Tanta can't leave a VC she wasn't even in, doofus.")


@client.command(pass_context=True)
async def pause(ctx):
    if ctx.author.id not in PrePrep.cmdWhitelist:
        await ctx.send("Nah, would rather not let you handle this command.")
    else:
        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
        if voice.is_playing():
            voice.pause()
        else:
            await ctx.send("The what?")


@client.command(pass_context=True)
async def resume(ctx):
    if ctx.author.id not in PrePrep.cmdWhitelist:
        await ctx.send("Nah, would rather not let you handle this command.")
    else:
        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
        if voice.is_paused():
            voice.resume()
        else:
            await ctx.send("The what?")


@client.command(pass_context=True)
async def skip(ctx):
    if ctx.author.id not in PrePrep.cmdWhitelist:
        await ctx.send("Nah, would rather not let you handle this command.")
    else:
        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
        voice.stop()
        await ctx.send("Skipping track.")


@client.command(pass_context=True)
async def altplay(ctx):
    try:
        if ctx.author.voice:
            channel = ctx.message.author.voice.channel
            voice = await channel.connect()
        else:
            await ctx.send("Tanta can't join you if you're not in a VC, dummy.")
    except:
        print("Placeholder message. Proceeding as normal.")
    file = "I Stand Alone"
    track = f"C:/Users/jayth/Desktop/Extra Audio/{file}.mp3"
    source = FFmpegPCMAudio(track)
    voice = get(client.voice_clients, guild=ctx.guild)

    if not voice.is_playing():
        voice.play(source)
        voice.is_playing()
        print("Loaded.")
    else:
        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
        voice.stop()
        voice.play(source)
        voice.is_playing()
        print("Restarting.")
        return
        

@client.command()
async def begging(ctx):
    if ctx.author.voice:
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        track = "C:/Users/jayth/Desktop/Extra Audio/xu_zhi_begs-1.mp3"
        source = FFmpegPCMAudio(track)
        player = voice.play(source)
        time.sleep(4.3)
        track = "C:/Users/jayth/Desktop/Extra Audio/xu_zhi_begs-2.mp3"
        source = FFmpegPCMAudio(track)
        player = voice.play(source)
        time.sleep(14.3)
        track = "C:/Users/jayth/Desktop/Extra Audio/xu_zhi_begs-3.mp3"
        source = FFmpegPCMAudio(track)
        player = voice.play(source)


@client.command()
async def wrellerman(ctx, showLyrics = None):
    if showLyrics is None:
        try:
            if ctx.author.voice:
                channel = ctx.message.author.voice.channel
                voice = await channel.connect()
            else:
                await ctx.send("Tanta can't join you if you're not in a VC, dummy.")
        except:
            print("Placeholder message. Proceeding as normal.")
        source = FFmpegPCMAudio("C:/Users/jayth/Desktop/Extra Audio/Wrellerman_mixdown.mp3")
        voice = get(client.voice_clients, guild=ctx.guild)

        if not voice.is_playing():
            
            voice.play(source)
            voice.is_playing()
            await ctx.send("Wrel's Sea Shanty, The Wrellerman.")

        else:
            await ctx.send("Hush, Wrel is singing.")
            return
    elif showLyrics.lower() == "lyrics":
        title = "Lyrics: The Wrellerman"
        body = "There once was a game that put to sea \
        \nThe game PlanetSide was Play for Free \
        \nThe Devs stepped up, when the pop was down \
        \nGo go, my PlanetMen, go \
        \n\
        \n(Chorus) \
        \nSoon may the Wrellerman come \
        \nTo bring us Oshur and sea and guns \
        \nOne day, when the gaming is done \
        \nWe'll take our Certs and go \
        \n\
        \nBeen no Dev Stream for a year or more \
        \nWhen down on the base a sky whale bore \
        \nThe PL called all hands and swore \
        \nHe'd take that whale in tow \
        \n\
        \n(Chorus) \
        \nSoon may the Wrellerman come \
        \nTo bring us Oshur and sea and guns \
        \nOne day, when the gaming is done \
        \nWe'll take our Certs and go \
        \n\
        \nBefore the Valk had hit the water \
        \nThe whale's tail came up and caught her \
        \nAll guns to the side, Strikers fought her \
        \nWhen she dived down low \
        \n\
        \n(Music) \
        \n\
        \nNo lattice was cut, no territory freed \
        \nThe PL's mind was not of greed \
        \nAnd he belonged to the PlanetMan's creed \
        \nThey locked that continent down \
        \n\
        \n(Chorus) \
        \nSoon may the Wrellerman come \
        \nTo bring us Oshur and sea and guns \
        \nOne day, when the gaming is done \
        \nWe'll take our Certs and go \
        \n\
        \nFor forty hours or even more \
        \nThe game was played, couldn't leave the door \
        \nAll continents locked, there were only four \
        \nUntil to Oshur we'd go \
        \n\
        \n(Chorus) \
        \nSoon may the Wrellerman come \
        \nTo bring us Oshur and sea and guns \
        \nOne day, when the gaming is done \
        \nWe'll take our Certs and go \
        \n\
        \nAs far as I've heard, the fight's still on \
        \nThe servers are up, and the Devs not gone \
        \nThe Wrellerman makes his Twitter call \
        \nTo encourage the PLs out \
        \n\
        \n(Chorus) \
        \nSoon may the Wrellerman come \
        \nTo bring us Oshur and sea and guns \
        \nOne day, when the gaming is done \
        \nWe'll take our Certs and go \
        \n\
        \n*Alright, well, thank you all.*"
        embed = discord.Embed(title = title, description = body, colour = PrePrep.colRan())
        embed.set_footer(text='"The Wrellerman" Sang by Wrel. Lyrics by JudokaNC. Audio rendition by Ansicone.n')
        await ctx.send(embed=embed)
        

# ==============================     anime commands     ==============================


@client.command(help = "More waifu if you're not satisfied")
async def morewaifu(ctx):
    await ctx.message.delete()
    async with aiohttp.ClientSession().get("https://api.waifu.pics/sfw/waifu") as response:
        waifus = (await response.json())["url"]
        user = ctx.message.author
        embed = discord.Embed(description=f'Here\'s a waifu for you, {user}', image=f'{waifus}', colour=0x400180)
        embed.set_image(url=waifus)
        await ctx.send(embed=embed)


@client.command(help = "Random Anime Quotes")
async def quotes(ctx):
    async with aiohttp.ClientSession().get("https://animechan.vercel.app/api/random") as response:
        anime = (await response.json())["anime"]
        character = (await response.json())["character"]
        quote = (await response.json())["quote"]
        embed = discord.Embed(title=f'Random Anime Quote From: {anime} by {character}', description=f'Quote: {quote}', colour = PrePrep.colRan())
        await ctx.send(embed=embed)


@client.command(help = "Random contextually irrelevant images and gifs (not jifs)")
async def randem(ctx):
    var = ["/background/img",
    "/bite/gif",
    "/blush/gif",
    "/cry/gif",
    "/cuddle/gif",
    "/dance/gif",
    "/eevee/gif",
    "/feed/gif",
    "/fluff/gif",
    "/holo/img",
    "/hug/gif",
    "/icon/img",
    "/kiss/gif",
    "/kitsune/img",
    "/lick/gif",
    "/neko/img",
    "/okami/img",
    "/pat/gif",
    "/poke/gif",
    "/senko/img",
    "/slap/gif",
    "/smile/gif",
    "/tail/gif",
    "/tickle/gif",]
    formatter = random.choice(var)
    user = ctx.message.author
    randomimg = requests.get(f"https://purrbot.site/api/img/sfw{formatter}")
    if randomimg.status_code == 200:
        img = (randomimg.json()["link"])
        embed = discord.Embed(description = f"Enjoy a random image/gif (not jif), {user}", image = f"{img}", colour = PrePrep.colRan())
        embed.set_image(url = img)
        await ctx.send(embed = embed)
    else:
        await ctx.send("An unexpected error has occured")
    


@client.command(help = "Self explanatory command")
async def nekogif(ctx):
    nekoGif = requests.get("https://nekos.life/api/v2/img/ngif")
    if nekoGif.status_code == 200:
        gif = (nekoGif.json()["url"])
        embed = discord.Embed(description = "Here, have a neko", image = f"{gif}", colour = PrePrep.colRan())
        embed.set_image(url = gif)
        await ctx.send(embed = embed)
    else:
        await ctx.send("An unexpected error has occured")


@client.command(help = "More neko gifs if you're not satisfied")
async def morenekogif(ctx):
    nekopic = requests.get("https://purrbot.site/api/img/sfw/neko/gif")
    if nekopic.status_code == 200:
        gif = (nekopic.json()["link"])
        embed = discord.Embed(description = "Have a neko", image = f"{gif}", colour = PrePrep.colRan())
        embed.set_image(url = gif)
        await ctx.send(embed = embed)
    else:
        await ctx.send("An unexpected error has occured")


@client.command(help = "More neko if you're not satisfied")
async def moreneko(ctx):
    nekopic = requests.get("https://neko-love.xyz/api/v1/neko")
    if ctx.author.id == 591074600411070502:
        toggle = 1
    else:
        toggle = random.randint(1,100)
    if toggle != 3:
        if nekopic.status_code == 200:
            image = (nekopic.json()["url"])
            embed = discord.Embed(description = "Have a neko", image = f"{image}", colour = PrePrep.colRan())
            embed.set_image(url = image)
            await ctx.send(embed = embed)
        else: 
            await ctx.send("An unexpected error has occured")
    else:
        embed = discord.Embed(title = "Here, behold our Lord and Saviour Tachanka", colour = PrePrep.colRan())
        embed.set_image(url = "https://www.dexerto.com/wp-content/uploads/2020/02/tachanka-rework-rainbow-six-siege-year-5.jpg")
        embed.set_footer(text = "There is a 1 in 100 chance that an image of Tachanka is sent instead. Here he is.")
        await ctx.send(embed = embed)


@client.command(help = "Self-explanatory command")
async def meowfact(ctx):
    async with aiohttp.ClientSession().get("https://catfact.ninja/fact") as response:
        fact = (await response.json())["fact"]
        length = (await response.json())["length"]
        embed = discord.Embed(title=f'Random Cat Fact Number: {length}', description=f'Cat Fact: {fact}', colour = PrePrep.colRan())
        embed.set_footer(text="")
        await ctx.send(embed=embed)


# Returns a link to a random cat gif
@client.command(help = "Self-explanatory command")
async def meowgif(ctx):
    catGif = requests.get('http://thecatapi.com/api/images/get?format=src&type=gif')
    if catGif.status_code == 200:
        catGif = catGif.url
        await ctx.send(catGif)

    else:
        await ctx.send('Error 404. Website may be down.')


@client.command(help = "Self-explanatory command")
async def meowpic(ctx):
    catPicture = requests.get('http://thecatapi.com/api/images/get.php')
    if catPicture.status_code == 200:
        catPicture = catPicture.url
        embed = discord.Embed(title="Meow", colour=PrePrep.colRan())
        embed.set_image(url=catPicture)
        await ctx.send(embed=embed)

    else:
        await ctx.send('Error 404. Website may be down.')


@client.command(help = "Tom Clancy's Rainbow Six Siege")
async def siegeop(ctx):
    variable = [
        "https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/6eIdbZWLBIdtCygNAu9uue/1cdeaf7628eab3e130ba6bb2204c6669/r6-operators-list-sledge.png",
        "https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/5QGPM6l25ybaINnaIaLgvm/0018bcb286bf45237e24772682464ad3/r6-operators-list-thatcher.png",
        "https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/2Tm9rzdq6j9cpdW9qjnnrw/10d42d14755002e1056d1a940841482c/r6-operators-list-smoke.png",
        "https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/4BWoDVmdDsgrI071YJwqyF/266f79c579e41c660136c5c7489c9597/r6-operators-list-mute.png",
        "https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/QOEBDfqjtUxVBc31l8L9f/ae4d2c218c71e8916c234c4aa28b91b8/r6-operators-list-ash_317253.png",
        "https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/3NQW8lJVslVSaYSiBlAleU/c16307a0bfab56cbcd067459bacc2925/r6-operators-list-thermite.png",
        "https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/1ETv9XcrmgbAdYWDJ2ZIh0/0e2204fef335624d570fbaf8d87ae346/r6-operators-list-castle.png",
        "https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/1YQb5phSD3uYbWrqhCBJRU/779944671024b586c8c228f6c510672f/r6-operators-list-pulse.png",
        "https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/1hxlGxmToB93urkgbIzUvW/4cd06e8f753fde3eebe284fd3d75540f/r6-operators-list-montagne.png",
        "https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/Z9R1Anc8MHwbG5iyPoOf2/572951f9f57de72baef8076a27d89dd1/r6-operators-list-twitch.png",
        "https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/2sCxLIpS9I19PKRz44Phj9/704fe9644efbcb5bdf054918a0d95dda/r6-operators-list-doc.png",
        "https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/1aFTx0BJYAKAnS1vyNA7w6/ce86f077eb0ae81aa8ce66a7ab8a4224/r6-operators-list-rook.png",
        "https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/4NZvCtXwtcCq1s65H7mK5y/c510f2332362543648e032b2768b4311/r6-operators-list-blitz.png",
        "https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/3lP88YKPk0boUyisZD0LT7/199929a0aa20e45ccbac22b55cf7d129/r6-operators-list-iq.png",
        "https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/2cFHG0Xk93uoGrm5nTjDPE/1eb109b1866e0b428a6583033a3af011/r6-operators-list-bandit.png",
        "https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/4kMW2lcoewGifRWbvQVjKy/8f974b5d26db81dc823ea602e31d6273/r6-operators-list-jager.png",
        "https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/6R6uQlUmkh7KYoFYeeGpvj/3f5630cc8a0f924eeef770dc086b614e/r6-operators-list-glaz.png",
        "https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/BsiNYFp7htro1mOEgiKf1/7e06bc63e1c0abc324fe3e8e2f957266/r6-operators-list-fuze.png",
        "https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/7MofnDHeL1uwsenBVjxplQ/2276e05f082a8730f3d0d0ae92a1dd50/r6-operators-list-kapkan.png",
        "https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/5P9kGyOrnsu7lRyr9xC71t/6477a644eefdf20888ebf33b472f2980/r6s-operators-list-tachanka.png",
        "https://upload.wikimedia.org/wikipedia/commons/9/9f/Tachanka9876.png",
        "https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/3k68pZu62GPbCAFOSCej9a/7099b4338501aefd8940980727cb5909/r6-operators-list-buck.png",
        "https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/33qvDwvWy7y9VGw9k1RYWi/3a0db2fa0e2e09d05d344cf20222ec56/r6-operators-list-frost.png",
        "https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/5u6Ak7dkTb4yOjaP1hlGuT/04852813209ff21d6b08304aa557c235/r6-operators-list-blackbeard.png",
        "https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/7xN3HJXPLVEmWA9PDnQzTV/613b19a897503161f2cf6fe7bbe3408e/r6-operators-list-valkyrie.png",
        "https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/3AZlhNFA21aKL2MdAIEwa8/7a70e885cf5421c9bafe8e8388ec5ce2/r6-operators-list-capitao.png",
        "https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/4RZ2Vwk7HozKMCtS5gFMp7/ca92abcb99e7cd9a6c415193858653d9/r6-operators-list-caveira.png",
        "https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/7mAs4mz2zA4wjPZsNg6tys/5e607795f95200f83b3d4be2f7cc4bba/r6-operators-list-hibana.png",
        "https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/7MdVMpafww11MfSVMEzyTK/4d4c5d92585c7cf11a28cbf9456e3d9e/r6-operators-list-echo.png",
        "https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/kbyJly2JDRxFrjFSrptiy/a593cd31f9fc15d3d427373ddd980ba1/r6-operators-list-jackal.png",
        "https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/2Q9Y4UXzkQfECOw5fX3QrI/bfd6532c840cb06a22e0196f2acfc462/r6-operators-list-mira.png",
        "https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/36BxtuVTQFrNh2OPyJ2px3/f3fff37452213c118bcaa2a4f45e3b98/r6-operators-list-ying.png",
        "https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/3woPDn0yMuXfkr2RYoymFj/964dfe9277e5299b0125c33b39e165d1/r6-operators-list-lesion.png",
        "https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/z60t1OJxJoHqm2zp0t5dL/4acc0904444f43b12a17f6a578322cf9/r6-operators-list-zofia.png",
        "https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/6110n4X8KghHzBtPrksrKD/a4c5863ab9d796b6fd28359d3ff57839/r6-operators-list-ela.png",
        "https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/7fjUupLXClpcdTyqdvPv24/e4492917c18682ef09f9b0445176b2f2/r6-operators-list-dokkaebi.png",
        "https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/48ebOPwZWlyktdhawglqlI/0c5d9cbcb7d105b4ddc860185084ed93/r6-operators-list-vigil.png",
        "https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/6VkZ60XV4HWhbQaoMpfjnw/35d70415fc67d237fc9f95f5686f51b1/r6-operators-list-finka.png",
        "https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/4wYSIOO4AKq0nw1GbulGns/bbb46af215a91b43e0ab6a4913364874/r6-operators-list-lion.png",
        "https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/6QNXf9qRkqzOdsprj2SWgI/09333f2c3dc138a19fc39e61361c730a/r6-operators-list-maestro.png",
        "https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/11nzEgSwdAXLow3kPl0wom/1f42fb228e1db59f389756e8e38ad54b/r6-operators-list-alibi.png",
        "https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/1MmaEupq7KOe6it1trqIWP/93730f7c3b2b7de5591243a9d5276dcf/r6-operators-list-maverick.png",
        "https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/3tTgRbA9GdeLTmI1mPObsp/c3b843c71a0409d23fbe18a67f4c1c27/r6-operators-list-clash.png",
        "https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/3VHhiyMOUkBOW1u1Zh5eGH/32b7a527bad166279973cf4ae79089dd/r6-operators-list-nomad.png",
        "https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/9ATWPlasUTzxyJMNlV9SM/054ac149f92639747d341a435a4f9f96/r6-operators-list-kaid.png",
        "https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/27gUsHtPmP86NRs4cPug1o/bd7936c0239481ee6fa031dc074e5ef7/r6-operators-list-gridlock.png",
        "https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/5NwXzotdPIQuvWugaam4JA/37163d87e9b6462b82c057f512f0031a/r6-operators-list-mozzie_343537.png",
        "https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/VeXso9iKMqBDrSmuJ2kBx/9d1b1ebd7a83d468e626d1418cfa1776/r6-operators-list-nokk.png",
        "https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/72pEJEYxwPGoW221XvdmAJ/e83bf913ad3cb01e20ab5f8b89c4463e/r6-operators-list-warden.png",
        "https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/5jumFHxGXFA7HehPNn0uGD/9327bbc2a052bfa8997e37ff729768d9/r6-operators-list-amaru.png",
        "https://liquipedia.net/commons/images/thumb/e/e6/Goyo_R6S.png/294px-Goyo_R6S.png",
        "https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/41NACeIbkdnIWgnwq0HzD4/bbc58450e36ab60e693f5f98a00c1f38/r6-operators-list-kali_358317.png",
        "https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/2ZSUcKWczIo1w2WwzNan5B/6d4462a573312f88657c4dc8b54061c2/r6-operators-list-wamai_358318.png",
        "https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/6vES8lEllMwW9OaBYRT7YX/4415eea2ab9d0abf871ffe05ee53205a/r6s-operator-list-iana.png",
        "https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/3JBOp3MXgGeuEwyoYrkuMi/301813efd3d4cc57aa726a942e74e8e7/r6s-operator-list-oryx.png",
        "https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/5snW47tH4a5VuPhidr61sm/4bee3d218c40a6aeeedb97afbcea82cb/r6s-operator-list-ace.png",
        "https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/1yoVAGw5rEQ8zPPHoQSDJb/521229de345f961d46b2c6b8bf630e39/r6s-operator-list-melusi.png",
        "https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/24jDQIfDdVMLX5K54pKNe5/6cb9e711c1f6c1684dd49a68ce165ead/r6s-operator-list-zero.png",
        "https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/4yfuWCW8O4ja2VqR9tXqaE/cdcf3b07203d3d5cb322295cf2ab99d5/r6s-operators-list-aruni.png",
        "https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/3hXRjYHsrlFOocJjyxyYZY/29eb8f1ad9eab150518a053b775c336f/r6s-operators-list-flores.png",
        "https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/3gadEIZqtSfsHstfPMe3bz/424c7e4c21276e99f41a8c75478aa5e5/r6s-operators-list-thunderbird.png",
        "https://liquipedia.net/commons/images/8/82/Recruit_R6S.png"
    ]
    operator = random.choice(variable)
    embed = discord.Embed(title = "Here's a Siege operator.", image = operator, colour = PrePrep.colRan())
    embed.set_image(url = operator)
    embed.set_footer(text = "Do you know their name?")
    await ctx.send(embed = embed)


@client.command(help = "Clown someone")
async def clown(ctx, user: discord.Member = None):
    if user is None:
        user = ctx.message.author
    
    user = user.mention
    if user in PrePrep.cmdWhitelist:
        await ctx.send(f"This is the definition of {user}:")
        await ctx.send("https://i2.wp.com/www.chesterbugle.co.uk/wp-content/uploads/2018/02/rick-astley.jpg?fit=654%2C372")
        time.sleep(0.6)
        var = [
            "lol get rekt rolled",
            "rekt lolpog",
            "now that's a handsome chap, also rick trolled",
            "get nae nae'd",
            "rick astley says hi",
        ]
        await ctx.send(random.choice(var))
    else:
        await ctx.send(f"This is the definition of {user}:")
        await ctx.send("https://static.vecteezy.com/system/resources/previews/000/271/726/original/vector-vintage-circus-poster-with-big-top.jpg")


@client.command(help = "Get to the NSFW chopper")
async def chopper(ctx):
    await ctx.send("**You hear that sound?**\n\n")
    await ctx.send("https://media.discordapp.net/attachments/680928395399266314/836674111932465202/image0.gif")
    await ctx.send("**\n\nGit to zer Choppa.**")


# ==============================     custom server specific commands: hsc 2020 robo alumni     ==============================


@client.command(help = "sex")
async def sex(ctx, limit=None):
    channel = client.get_channel(795158728739389462)
    if limit is None:
        limit = 1
    elif float(limit) < 1:
        limit = 1
    elif float(limit) > 20:
        limit = 20
    loop = 1
    while loop <= float(limit):
        await channel.send("sex")
        loop += 1
        time.sleep(1.8)


@client.command(help = "Read my book!")
async def plug(ctx, limit=None):
    await ctx.send("@everyone This is Xu Zhi (<@!535799567732703232>) speaking, please read my book. Thanks!")
    await ctx.send("https://docs.google.com/document/d/1aRG-7D1ZiGPOnEg4sj8aRoouYQJLgQwlxq5EOkor1A4/edit?usp=sharing"
    "\nhttps://docs.google.com/document/d/1QT3yORfJVuiu5bhKwCKZQSykQlV9EKiDNJcx0VJjBVM/edit?usp=sharing"
    "\nhttps://docs.google.com/document/d/15vVqBsmhakNhHdGSBl7eLyOHhyxXo0J369DDhfyzRec/edit?usp=sharing"
    "\nhttps://docs.google.com/document/d/15zIJDgAw2nmrHlNZ4dlTTjBYCgE5mQNrc0JM6mdMqbs/edit?usp=sharing"
    "\nhttps://docs.google.com/document/d/1GwwmeXD-34-PgyXBaxTL01pN5I1r20QDGv0RRv3pfKM/edit?usp=sharing")

@client.command(help = "A less efficient way to quote someone")
async def quote(ctx, user: discord.Member = None, *args):
    channel = client.get_channel(794600190626758716)
    if user is None:
        await ctx.send("Who the hell are you quoting?")
    else:
        user = user.mention
        await channel.send("\"" + " ".join(args[:]) + "\""
                           "\n- {}".format(user))


#=========================================================================Help Commands=========================================================================
"""@client.command()
async def nekohelp(ctx,*, reason=None):
    author = ctx.message.author
    helpembed= discord.Embed(colour=discord.Color.green())
    helpembed.set_author(name="Options")
    if nsfw_enabled == True:
        helpembed.add_field(name="+help nsfw", value = "available nsfw commands")
        helpembed.add_field(name="+help more nsfw", value = "more available nsfw\
                commands")
    if reason == "nsfw" and nsfw_enabled == True:
        await help_nsfw(ctx)
        return
    if reason == "more nsfw" and nsfw_enabled == True:
        await help_more_nsfw(ctx)
        return
    await ctx.author.send(embed=helpembed)

###help commands
@client.command()
async def help_nsfw(ctx):
    embed = discord.Embed(colour=discord.Color.blurple())
    embed.set_author(name="Available NSFW commands")
    embed.add_field(name="feet", value='NSFW feet pics', inline=False)
    embed.add_field(name="yuri", value='NSFW yuri pics', inline=False)
    embed.add_field(name="trap", value='NSFW trap pics', inline=False)
    embed.add_field(name="futanari",value='NSFW futanari pics', inline=False)
    embed.add_field(name="hololewd",value='NSFW hololewd pics', inline=False)
    embed.add_field(name="lewdkemo",value='NSFW lewdkemo pics', inline=False)
    embed.add_field(name="cum",value='NSFW cum on catgirls \
            pics', inline=False)
    embed.add_field(name="erokemo", value='NSFW erokemo pics', inline=False)
    embed.add_field(name="les", value='NSFW les pics', inline=False)
    embed.add_field(name="wallpaper", value='cute wallpapers', inline=False)
    embed.add_field(name="lewdk", value='NSFW lewdk pics', inline=False)
    embed.add_field(name="neko_gif",value='cute neko pics \
      #      :flushed:', inline=False)                               
    embed.add_field(name="lewd",value='lewd catgirls', inline=False)
    embed.add_field(name="gecg",value='genetically engineered catgirl\
            memes', inline=False)
    embed.add_field(name="eroyuri",value='NSFW eroyuri', inline=False)
    embed.add_field(name="eron",value='NSFW eron', inline=False)
    embed.add_field(name="bj",value='NSFW bj', inline=False)
    embed.add_field(name="nsfw_neko_gif",value='NSFW neko gif', inline=False)
    embed.add_field(name="solo",value='NSFW solo pic', inline=False)
    embed.add_field(name="kemonomimi",value="kemonomimi", inline =False)
    embed.add_field(name="kuni",value="random kuni gif", inline =False)
    await ctx.send(embed=embed)

@client.command()
async def help_more_nsfw(ctx):
    author = ctx.message.author
    embed2 = discord.Embed(colour=discord.Color.blurple())
    embed2.set_author(name="More NSFW")
    embed2.add_field(name="+nsfw_avatar", value='NSFW avatar pic for u\
            horny virgins',inline=False)
    embed2.add_field(name="+anal", value='NSFW anal pic', inline=False)
    embed2.add_field(name="+hentai", value='NSFW hentai pic', inline=False)
    embed2.add_field(name="+avatar",value='generates a dope avatar\
            pic', inline=False)
    embed2.add_field(name="+erofeet", value='NSFW erofeet', inline=False)
    embed2.add_field(name="+pussy", value='NSFW pussy', inline=False)
    embed2.add_field(name="+tits", value='NSFW tits', inline=False)
    embed2.add_field(name="+waifu",value='waifu. self explanatory\
            you weeb', inline=False)
    embed2.add_field(name="+boobs", value='boobs', inline=False)
    #embed2.add_field(name="+smallboobs", value='small boobies', inline=False)
    embed2.add_field(name="+fox_girl", value='fox girl pics', inline=False)
    embed2.add_field(name="+neko", value='neko pics', inline=False)
    await ctx.author.send(embed=embed2)"""


#=========================================================================NSFW Commands=========================================================================


@client.command()
async def feet(ctx):
    await nsfwimgfetchfuncs(ctx,"feet","","")

# print(Fore.WHITE + "["+ Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA+ f"{ctx.author.name} executed command !feet result: {feet}   time:{round(client.latency * 1000)}ms")

# YURI, good ol yuri
@client.command()
async def yuri(ctx):
    await nsfwimgfetchfuncs(ctx,"yuri","","")


# traps (yaoi but worse)
@client.command()
async def trap(ctx):
    await nsfwimgfetchfuncs(ctx,"trap","","")

# futanari (Pei ze hates this shit)
@client.command()
async def futanari(ctx):
    await nsfwimgfetchfuncs(ctx,"futanari","","")

# hololewd {hololive lewds... probably}
@client.command()
async def hololewd(ctx):
    await nsfwimgfetchfuncs(ctx,"hololewd","","")


@client.command()
async def lewdkemo(ctx):
    await nsfwimgfetchfuncs(ctx,"lewdkemo","","")


@client.command()
async def cum(ctx):
    await nsfwimgfetchfuncs(ctx,"cum","","")

@client.command()
async def erokemo(ctx):
    await nsfwimgfetchfuncs(ctx,"erokemo","","")


@client.command()
async def les(ctx):
    await nsfwimgfetchfuncs(ctx,"les","","")

@client.command()
async def wallpaper(ctx):
    await nsfwimgfetchfuncs(ctx,"wallpaper","","")

@client.command()
async def lewdk(ctx):
    await nsfwimgfetchfuncs(ctx,"lewdk","","")


@client.command()
async def kuni(ctx):
    await nsfwimgfetchfuncs(ctx,"kuni","","")

@client.command()
async def baka(ctx, member: discord.Member, *, reason=""):
    await socialfuncs(ctx, "baka", "doesnt think much of", member, reason)

@client.command()
async def tickle(ctx, member: discord.Member, *, reason=""):
    await socialfuncs(ctx, "tickle", "tickled", member, reason)


@client.command()
async def lewd(ctx):
    await nsfwimgfetchfuncs(ctx, "lewd", "","")


@client.command()
async def feed(ctx, member: discord.Member, *, reason=""):
    await socialfuncs(ctx, "feed", "fed", member, reason)


@client.command()
async def gecg(ctx):
    await imgfetchfuncs(ctx,"gecg","","")

@client.command()
async def goose(ctx):
    await imgfetchfuncs(ctx,"goose","","")

@client.command()
async def lizard(ctx):
    await imgfetchfuncs(ctx,"lizard","","")

@client.command()
async def eroyuri(ctx):
    await nsfwimgfetchfuncs(ctx,"eroyuri", "", "")


@client.command()
async def eron(ctx):
    await nsfwimgfetchfuncs(ctx,"eron", "", "")


@client.command()
async def bj(ctx):
    await nsfwimgfetchfuncs(ctx,"bj", "", "")


@client.command()
async def nsfw_neko_gif(ctx):
    await nsfwimgfetchfuncs(ctx,"nsfw_neko_gif", "", "")


@client.command()
async def solo(ctx):
    await nsfwimgfetchfuncs(ctx,"solo", "", "")


@client.command()
async def kemonomimi(ctx):
    await imgfetchfuncs(ctx,"kemonomimi", "Awww, a catgirl", "")

@client.command()
async def gasm(ctx, member: discord.Member, *, reason=""):
    await socialfuncs(ctx, "gasm", "is in awe with", member, reason)

@client.command()
async def nsfw_avatar(ctx):
    await nsfwimgfetchfuncs(ctx, "nsfw_avatar", "", "")


@client.command()
async def poke(ctx, member: discord.Member, *, reason=""):
    await socialfuncs(ctx, "poke", "poked",  member, reason)

@client.command()
async def anal(ctx):
    await nsfwimgfetchfuncs(ctx, "anal", "", "")


@client.command()
async def slap(ctx, member: discord.Member, *, reason=""):
    await socialfuncs(ctx, "slap", "slapped", member, reason)


@client.command()
async def hentai(ctx):
    await nsfwimgfetchfuncs(ctx,"hentai","","")


@client.command()
async def avatar(ctx):
    await imgfetchfuncs(ctx,"avatar","","")


@client.command()
async def erofeet(ctx):
    await nsfwimgfetchfuncs(ctx,"erofeet","","")


@client.command()
async def pussy(ctx):
    await nsfwimgfetchfuncs(ctx,"pussy","","")


@client.command()
async def tits(ctx):
    await nsfwimgfetchfuncs(ctx,"tits","","")


@client.command()
async def waifu(ctx):
    await ctx.message.delete()
    await imgfetchfuncs(ctx,"waifu","Here, have a waifu","")


@client.command()
async def boobs(ctx):
        await nsfwimgfetchfuncs(ctx,"boobs","","")


"""@client.command()
async def smallboobs(ctx):
    await nsfwimgfetchfuncs(ctx,"smallboobs","","")"""


@client.command()
async def pat(ctx, member: discord.Member, *, reason=""):
    await socialfuncs(ctx,"pat","patted", member, reason)


@client.command(pass_context=True)
async def kiss(ctx, member: discord.Member, *, reason=""):
    await socialfuncs(ctx,"kiss","kissed", member, reason)


@client.command()
async def spank(ctx, member: discord.Member, *, reason=""):
    await socialfuncs(ctx,"spank","spanked", member, reason)


@client.command()
async def cuddle(ctx, member: discord.Member, *, reason=""):
    await socialfuncs(ctx,"cuddle","is cuddling with", member, reason)


@client.command()
async def hug(ctx, member: discord.Member, *, reason=""):
    await socialfuncs(ctx,"hug","hugged", member, reason)


@client.command()
async def foxgirl(ctx):
    await imgfetchfuncs(ctx, "fox_girl", "", "fox girls > all")



@client.command()
async def contribute(ctx):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(
        title='contribution',
        description='contribution to the project is always welcome, feel free to contribute, edit, clean up, document and improve the source code at: https://github.com/Eddy-Arch/hentai-discord-bot',
        colour=discord.Colour.from_rgb(r, g, b)
    )
    neko = nekos.img("neko")

    embed.set_image(url=neko)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command !neko result: {neko}   time:{round(client.latency * 1000)}ms")

# 2b2t alterations
@client.command()
async def queuepeak(ctx,*, reason=None):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    embed = discord.Embed(
        colour=discord.Color.from_rgb(r, g, b)
    )
    r = requests.get('https://rebane2001.com/queuepeek/data.json')
    embed.set_author(name="2B2T queue status")
    embed.add_field(name='in queue right now:', value=r.json()['queuepos'], inline=False)
    embed.add_field(name='time to wait', value=r.json()['queueest'], inline=False)
    if reason == "players":
        embed.add_field(name='fart', value=r.json()['players'][0]['name'][0:220], inline=False)
    await ctx.send(embed=embed)


 # image fetch style commands
@client.command()
async def neko(ctx):
    await imgfetchfuncs(ctx, "neko", "", "Have a neko")

@client.command()
async def smug(ctx):
    await imgfetchfuncs(ctx, "smug", "smug", "smug doe")

async def imgfetchfuncs(ctx, img_endpoint, title, description):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(
        title=title,
        description=description,
        colour=discord.Color.from_rgb(r, g, b)
    )
    img = nekos.img(img_endpoint)

    embed.set_image(url=img)

    await ctx.send(embed=embed)
    print(f"{ctx.author.name} executed command {conf_bot_prefix}{img_endpoint} result: {img}   time:{round(client.latency * 1000)}ms")

async def nsfwimgfetchfuncs(ctx,img_endpoint,title,description):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(
        title=title,
        description=description,
        colour=discord.Colour.from_rgb(r, g, b)
        )
    img = nekos.img(img_endpoint)

    embed.set_image(url=img)

    await ctx.send(embed=embed)
    print(f"{ctx.author.name} executed command {conf_bot_prefix}{img_endpoint} result: {img}   time:{round(client.latency * 1000)}ms")
    
    """if not nsfw_enabled == True:
        return
    if not ctx.channel.is_nsfw():
        error_embed = discord.Embed(
            colour=discord.Colour.red()
        )
        error_embed.add_field(name="Error", value="You tried running an __**NSFW**__ channel only command in a non __**NSFW**__ channel.\nsorry for the inconvience this might have caused, have a neko.")
        error_img = nekos.img("neko")
        error_embed.set_image(url=error_img)
        await ctx.author.send(embed=error_embed)
        await ctx.message.delete()
        sys.stderr = object
    if ctx.channel.is_nsfw():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(
            title=title,
            description=description,
            colour=discord.Colour.from_rgb(r, g, b)
        )
    img = nekos.img(img_endpoint)

    embed.set_image(url=img)

    await ctx.send(embed=embed)
    print(
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command {conf_bot_prefix}{img_endpoint} result: {img}   time:{round(client.latency * 1000)}ms")"""

async def socialfuncs(ctx,img_endpoint, action, member, arg=""):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    await ctx.message.delete()
    if arg != "":
        embed = discord.Embed(
            title=f"{ctx.message.author} {action} {member.name}",
            description=f'{ctx.message.author.name}: {arg}',
            colour=discord.Colour.from_rgb(r, g, b)
        )
    else:
        embed = discord.Embed(
            title=f"{ctx.message.author} {action} {member.name} {arg}",
            description='',
            colour=discord.Colour.from_rgb(r, g, b)
        )

    img = nekos.img(img_endpoint)

    embed.set_image(url=img)

    await ctx.send(embed=embed)
    print(f"{ctx.author.name} executed command {conf_bot_prefix}{img_endpoint} result: {img}   time:{round(client.latency * 1000)}ms")


# ============================     token     ============================


client.run(keykeeper.token)