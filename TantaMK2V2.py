# ==============================     importing modules     ==============================


from discord.utils import get
import discord, asyncio, random
from discord import FFmpegPCMAudio
import time, requests, nekos, sys, os
from youtube_dl import YoutubeDL
import random
from discord.ext import commands
from colorama import Fore
from config import *
import aiohttp
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
async def help(ctx, specifier = None, page = None):  # Too lazy to implement a better help menu at the moment
    carbonMessage = "We do not hold exclusive rights to this command."
    user = ctx.message.author
    if page is None:
        page = "1"
    if specifier is None:
        embed = discord.Embed(title = "The helpful help list (Categories)", colour=PrePrep.colRan())
        embed.add_field(name="Generic", value='General utility commands\n`4 commands`', inline=False)
        embed.add_field(name="Images", value='Self explanatory image commands\n`5 commands`', inline=False)
        embed.add_field(name="VC", value='Rectified VC commands\n`6 commands`', inline=False)
        embed.add_field(name="Humour", value='Slightly humourous commands\n`4 commands`', inline=False)
        embed.add_field(name="Interaction", value='Commands for user-to-user interaction\n`12 commands`', inline=False)
        embed.add_field(name="Weeb", value='A neat collection of catgirl pictures and GIFs (not JIFs), plus other weeb stuff we deemed suitable\n`11 commands`', inline=False)
        embed.add_field(name="NSFWeeb", value='NSFW weeb images and gifs to further fuel your degeneracy\n`26 commands`', inline=False)
        embed.set_footer(text = "Run tn? help [category] for more information (Example: tn? help generic)")

    elif specifier.lower() == "generic":
        embed = discord.Embed(title = "The helpful help list (Generic commands)", colour = PrePrep.colRan())
        embed.add_field(name="delet", value='Banish messages to the Shadow Realm', inline=False)
        embed.add_field(name="help", value='Shows a helpful help list', inline=False)
        embed.add_field(name="ping", value='Used to check if Tanta is still functioning', inline=False)
        embed.add_field(name="findav", value="Pull a specified user's avatar", inline=False)
        embed.set_footer(text = "Run tn? help [command] for flavour text and command usage format")

    elif specifier.lower() == "images":
        embed = discord.Embed(title = "The helpful help list (Image commands)", colour = PrePrep.colRan())
        embed.add_field(name="clown", value='Clown someone (or yourself)', inline=False)
        embed.add_field(name="goose", value='A random goose image to laugh at', inline=False)
        embed.add_field(name="meowpic", value='A nice cat picture to admire', inline=False)
        embed.add_field(name="meowgif", value='A nice cat gif (not jif) to admire', inline=False)
        embed.add_field(name="mewofact", value='Not an image but a random cat fact', inline=False)
        embed.set_footer(text = "Run tn? help [command] for flavour text and command usage format")

    elif specifier.lower() == "vc":
        embed = discord.Embed(title = "The helpful help list (VC commands)", colour = PrePrep.colRan())
        embed.add_field(name="altplay", value='Play pre-determined music in a VC', inline=False)
        embed.add_field(name="join", value='Summon Tanta to the VC', inline=False)
        embed.add_field(name="leave", value='Unsummon Tanta from the VC', inline=False)
        embed.add_field(name="pause", value='Stoppeth thy musick', inline=False)
        embed.add_field(name="resume", value='Thou doth desire thy musick', inline=False)
        embed.add_field(name="skip", value='Track suck, skip.', inline=False)
        embed.set_footer(text = "Run tn? help [command] for flavour text and command usage format")

    elif specifier.lower() == "humour":
        embed = discord.Embed(title = "The helpful help list (Humour commands)", colour = PrePrep.colRan())
        embed.add_field(name="gaymeter", value='Measure your gay level', inline=False)
        embed.add_field(name="likely", value='Tag 2 users and find out which of those 2 is more likely to do something', inline=False)
        embed.add_field(name="roulette", value='Place your life on the line and play Russian Roulette', inline=False)
        embed.add_field(name="trivt", value='Play an un-fun trivia game', inline=False)
        embed.set_footer(text = "Run tn? help [command] for flavour text and command usage format")

    elif specifier.lower() == "interaction":
        if page == "1":
            embed = discord.Embed(title = f"The helpful help list (Interaction commands) Page 1/2", colour = PrePrep.colRan())
            embed.add_field(name="baka", value="Baka", inline=False)
            embed.add_field(name="cuddle", value="Cuddling", inline=False)
            embed.add_field(name="feed", value="Feeding", inline=False)
            embed.add_field(name="gasm", value="Orgasm in awe to someone", inline=False)
            embed.add_field(name="hug", value="Hugging", inline=False)
            embed.add_field(name="kiss", value="Kissing", inline=False)
            embed.add_field(name="pat", value="Headpats", inline=False)
            embed.add_field(name="poke", value="Poking", inline=False)
            embed.add_field(name="slap", value="Slapping", inline=False)
            embed.add_field(name="smug", value="I lost the original command description", inline=False)
            embed.set_footer(text = "Run tn? help [command] for some flavour text and command usage format")
        elif page == "2":
            embed = discord.Embed(title = "The helpful help list (Interaction commands) Page 2/2", colour = PrePrep.colRan())
            embed.add_field(name="spank", value="Spanking", inline=False)
            embed.add_field(name="tickle", value="Tickling", inline=False)
            embed.set_footer(text = "Run tn? help [command] for flavour text and command usage format")

    elif specifier.lower() == "weeb":
        if page == "1":
            embed = discord.Embed(title = "The helpful help list (Weeb commands) Page 1/2", colour = PrePrep.colRan())
            embed.add_field(name="waifu", value="Have a waifu", inline=False)
            embed.add_field(name="morewaifu", value="Have another waifu", inline=False)
            embed.add_field(name="neko", value="Have a catgirl", inline=False)
            embed.add_field(name="moreneko", value="Have another catgirl. Or...", inline=False)
            embed.add_field(name="nekogif", value="Have a neko GIF (not JIF)", inline=False)
            embed.add_field(name="morenekogif", value="Have another neko GIF (not JIF)", inline=False)
            embed.add_field(name="gecg", value="Genetically engineered catgirls", inline=False)
            embed.add_field(name="foxgirl", value="Have a foxgirl", inline=False)
            embed.add_field(name="randem", value="View a contextually irrelevant and random image", inline=False)
            embed.add_field(name="avatar", value="Have an avatar", inline=False)
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
            embed.add_field(name="eroyuri", value="Eroyuri pics.", inline=False)
            embed.add_field(name="eron", value="Eron pics", inline=False)
            embed.add_field(name="bj", value="BJ pics", inline=False)
            embed.add_field(name="nsfw_neko_gif", value="Pretty self-explanatory", inline=False)
            embed.add_field(name="solo", value="NSFW solo image", inline=False)
            embed.add_field(name="kemonomimi", value="Kemonomimi pictures", inline=False)
            embed.add_field(name="kuni", value="Kuni gifs (not jifs)", inline=False)
            embed.add_field(name="nsfw_avatar", value="NSFW avatars", inline=False)
            embed.set_footer(text = "Run tn? help [command] for flavour text and command usage format")

        elif page == "3":
            embed = discord.Embed(title = "The helpful help list (NSFW weeb commands) Page 3/3", colour = PrePrep.colRan())
            embed.add_field(name="anal", value="Anal pics", inline=False)
            embed.add_field(name="hentai", value="Self-explanatory", inline=False)
            embed.add_field(name="erofeet", value="Erofeet pics", inline=False)
            embed.add_field(name="pussy", value="Pussy pics", inline=False)
            embed.add_field(name="tits", value="Go figure", inline=False)
            embed.add_field(name="boobs", value="Go figure", inline=False)
            embed.set_footer(text = "Run tn? help [command] for flavour text and command usage format")

    #       =====   Generic help    =====

    elif specifier.lower() == "delet":
        embed = discord.Embed(title = "tn? delet [integer]", description = "Deletes a specified number of messages from the channel the command was issued in. Does not include the command as a message. Defaults to 1 if a number is not specified.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "help":
        embed = discord.Embed(title = "tn? help", description = "Well no shit it shows the helpful help list what do you think?", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "ping":
        embed = discord.Embed(title = "tn? ping", description = "A simple ping command to chcek if Tanta is still actively listening for commands.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    #       =====   Image help  =====

    elif specifier.lower() == "clown":
        embed = discord.Embed(title = "tn? clown [user]", description = "Show someone what they really are: not a clown.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "goose":
        embed = discord.Embed(title = "tn? goose", description = "Look, a goose.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "meowpic":
        embed = discord.Embed(title = "tn? meowpic", description = "A picture with cats in it.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "meowgif":
        embed = discord.Embed(title = "tn? meowgif", description = "A GIF (not JIF) with cats in it.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "meowfact":
        embed = discord.Embed(title = "tn? meowfact", description = "A fact about cats, because you can't spell \"Fact\" without the letters of \"cat\".", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    #       =====   VC help =====

    elif specifier.lower() == "altplay":
        embed = discord.Embed(title = "tn? altplay", description = "Due to ytdl being funny, this cheap workaround method is now used to play a pre-selected track.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "join":
        embed = discord.Embed(title = "tn? join", description = "If Tanta is not already in your VC, she will connect to it upon issuing this command.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "leave":
        embed = discord.Embed(title = "tn? leave", description = "If Tanta is in your VC, she will disconnect upon issuing this command.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "pause":
        embed = discord.Embed(title = "tn? pause", description = "If Tanta is playing a track, she will temporarily stop playing it.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "resume":
        embed = discord.Embed(title = "tn? resume", description = "If Tanta has paused the track she was playing, she will continue playing that track.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "skip":
        embed = discord.Embed(title = "tn? skip", description = "Forcefully skips the currently playing track.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    #       =====   Humour help   =====

    elif specifier.lower() == "gaymeter":
        embed = discord.Embed(title = "tn? gaymeter [user]", description = "Issue this command to find out how gay you are. Not intended as a serious confused gender test.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "likely":
        embed = discord.Embed(title = "tn? likely <user> <user> <action>", description = "Tag 2 users and find out which of the 2 users is more likely to perform a specified action.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "roulette":
        embed = discord.Embed(title = "tn? roulette [user]", description = "Risk yor life and spin the revolver to play Russian Roulette.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "trivt":
        embed = discord.Embed(title = "tn? trivt [question id]", description = "Request a random trivia question to answer within 14 seconds. Questions are heavily based on developer interests. Entering a number will display the question with that specific ID, if it exists.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    #       =====   Interaction help   =====

    elif specifier.lower() == "baka":
        embed = discord.Embed(title = "tn? baka <user>", description = carbonMessage, colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "cuddle":
        embed = discord.Embed(title = "tn? cuddle <user>", description = carbonMessage, colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "feed":
        embed = discord.Embed(title = "tn? feed <user>", description = carbonMessage, colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")
    
    elif specifier.lower() == "gasm":
        embed = discord.Embed(title = "tn? gasm <user>", description = carbonMessage, colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "hug":
        embed = discord.Embed(title = "tn? hug <user>", description = carbonMessage, colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "kiss":
        embed = discord.Embed(title = "tn? kiss <user>", description = carbonMessage, colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "pat":
        embed = discord.Embed(title = "tn? pat <user>", description = carbonMessage, colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "poke":
        embed = discord.Embed(title = "tn? poke <user>", description = carbonMessage, colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "slap":
        embed = discord.Embed(title = "tn? slap <user>", description = carbonMessage, colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "smug":
        embed = discord.Embed(title = "tn? smug <user>", description = carbonMessage, colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "spank":
        embed = discord.Embed(title = "tn? spank <user>", description = carbonMessage, colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "tickle":
        embed = discord.Embed(title = "tn? tickle <user>", description = carbonMessage, colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    #       =====   Weeb help   =====

    elif specifier.lower() == "waifu":
        embed = discord.Embed(title = "tn? waifu", description = carbonMessage, colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "morewaifu":
        embed = discord.Embed(title = "tn? morewaifu", description = "Extra waifu command that we claim partial originality for.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "neko":
        embed = discord.Embed(title = "tn? neko", description = carbonMessage, colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "moreneko":
        embed = discord.Embed(title = "tn? moreneko", description = "Extra neko command that we claim partial originality for. And just for fun...", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "nekogif":
        embed = discord.Embed(title = "tn? nekogif", description = carbonMessage, colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "morenekogif":
        embed = discord.Embed(title = "tn? mormenekogif", description = "Extra nekogif (not jif) command that we claim partial originality for.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "gecg":
        embed = discord.Embed(title = "tn? gecg", description = carbonMessage, colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "foxgirl":
        embed = discord.Embed(title = "tn? foxgirl", description = carbonMessage, colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "randem":
        embed = discord.Embed(title = "tn? randem", description = "What image will this command give you? Ha ha, I have no idea!\n(Bonus cookie if you get the reference)", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "avatar":
        embed = discord.Embed(title = "tn? avatar", description = carbonMessage, colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "quotes":
        embed = discord.Embed(title = "tn? quotes", description = "Some random quote from a random character from a random anime.", colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    #       =====   NSFW help   =====

    elif specifier.lower() == "feet":
        embed = discord.Embed(title = "tn? feet", description = carbonMessage, colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "yuri":
        embed = discord.Embed(title = "tn? yuri", description = carbonMessage, colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "trap":
        embed = discord.Embed(title = "tn? trap", description = carbonMessage, colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "futanari":
        embed = discord.Embed(title = "tn? futanari", description = carbonMessage, colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "hololewd":
        embed = discord.Embed(title = "tn? hololewd", description = carbonMessage, colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "lewdkemo":
        embed = discord.Embed(title = "tn? ", description = carbonMessage, colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "cum":
        embed = discord.Embed(title = "tn? cum", description = carbonMessage, colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "erokemo":
        embed = discord.Embed(title = "tn? erokemo", description = carbonMessage, colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "les":
        embed = discord.Embed(title = "tn? les", description = carbonMessage, colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "wallpaper":
        embed = discord.Embed(title = "tn? wallpaper", description = carbonMessage, colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "lewdk":
        embed = discord.Embed(title = "tn? lewdk", description = carbonMessage, colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "lewd":
        embed = discord.Embed(title = "tn? lewd", description = carbonMessage, colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "eroyuri":
        embed = discord.Embed(title = "tn? eroyuri", description = carbonMessage, colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "eron":
        embed = discord.Embed(title = "tn? eron", description = carbonMessage, colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "bj":
        embed = discord.Embed(title = "tn? bj", description = carbonMessage, colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "nsfw_neko_gif":
        embed = discord.Embed(title = "tn? nsfw_neko_gif", description = carbonMessage, colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "solo":
        embed = discord.Embed(title = "tn? solo", description = carbonMessage, colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "kemonomimi":
        embed = discord.Embed(title = "tn? kemonomimi", description = carbonMessage, colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "kuni":
        embed = discord.Embed(title = "tn? kuni", description = carbonMessage, colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "nsfw_avatar":
        embed = discord.Embed(title = "tn? nsfw_avatar", description = carbonMessage, colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "anal":
        embed = discord.Embed(title = "tn? anal", description = carbonMessage, colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "hentai":
        embed = discord.Embed(title = "tn? hentai", description = carbonMessage, colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "erofeet":
        embed = discord.Embed(title = "tn? erofeet", description = carbonMessage, colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "pussy":
        embed = discord.Embed(title = "tn? pussy", description = carbonMessage, colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "tits":
        embed = discord.Embed(title = "tn? tits", description = carbonMessage, colour = PrePrep.colRan())
        embed.set_footer(text = "Arguments in [square brackets] are optional. Arguments in <angular brackets> are required.")

    elif specifier.lower() == "boobs":
        embed = discord.Embed(title = "tn? boobs", description = carbonMessage, colour = PrePrep.colRan())
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
async def findav(ctx, user: discord.Member = None):
    if user is None:
        await ctx.send("Mention a user or specify their ID.")
    else:
        pfp = user.avatar_url
        embed = discord.Embed(title = f"Retrieving avatar for {str(user)}", url = f"{pfp}", colour = PrePrep.colRan())
        embed.set_image(url = f"{pfp}")
        embed.set_footer(text=f"Pleasant evening, {str(ctx.message.author)}")
        await ctx.send(embed=embed)


# ==============================     humour commands     ==============================


@client.command()
async def trivt(ctx, id = None):
    wrongList = [
        "Nein, incorrect.",
        "Yikes, no.",
        "Wrong answer identified.",
        "Not the right answer, unfortunately.",
        "Ahhhh, no, incorrect.",
        "Wrong option mate.",
        "Err, no, that's incorrect.",
    ]
    rightList = [
        "That is indeed the answer.",
        "Correct. Did you just guess?",
        "Hmm, that seems to be correct.",
        "Incorrect answ- ahem, no wait, your answer was correct. Apologies.",
        "You're right, though it feels like you guessed.",
        "Usually I'd say you're wrong, but this time, you're correct.",
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


#=========================================================== NSFW Commands =============================================================


@client.command()
async def feet(ctx):
    await nsfwimgfetchfuncs(ctx,"feet","","")


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
    # r = random.randint(0, 255)
    # g = random.randint(0, 255)
    # b = random.randint(0, 255)
    # embed = discord.Embed(
    #     title=title,
    #     description=description,
    #     colour=discord.Colour.from_rgb(r, g, b)
    #     )
    # img = nekos.img(img_endpoint)

    # embed.set_image(url=img)

    # await ctx.send(embed=embed)
    # print(f"{ctx.author.name} executed command {conf_bot_prefix}{img_endpoint} result: {img}   time:{round(client.latency * 1000)}ms")
    
    if not nsfw_enabled == True:
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
        Fore.WHITE + "[" + Fore.MAGENTA + '+' + Fore.WHITE + "]" + Fore.MAGENTA + f"{ctx.author.name} executed command {conf_bot_prefix}{img_endpoint} result: {img}   time:{round(client.latency * 1000)}ms")

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


# ============================     private commands     ============================


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


@client.command(help = "Get to the NSFW chopper")
async def chopper(ctx):
    await ctx.send("**You hear that sound?**\n\n")
    await ctx.send("https://media.discordapp.net/attachments/680928395399266314/836674111932465202/image0.gif")
    await ctx.send("**\n\nGit to zer Choppa.**")


@client.command(help = "A less efficient way to quote someone")
async def quote(ctx, user: discord.Member = None, *args):
    channel = client.get_channel(794600190626758716)
    if user is None:
        await ctx.send("Who the hell are you quoting?")
    else:
        user = user.mention
        await channel.send("\"" + " ".join(args[:]) + "\""
                           "\n- {}".format(user))


# ============================     token     ============================


client.run(keykeeper.token)