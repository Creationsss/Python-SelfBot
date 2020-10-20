import subprocess, requests, colorama, os, platform, json, discord, random, datetime, sys, win32gui, win32console, win32api, win32con, logging, re, time
from discord.ext import commands, tasks
from colorama import Fore, Style, init
from infi.systray import SysTrayIcon
from playsound import playsound

init()

global config
global prefix
global token
global messageLOG
global notifymessages
global names
global notfiymessagesSOUND
global start_time
global UserBot

config = json.load(open('config.json'))
prefix = config.get('prefix')
token = config.get('token')
messageLOG = config.get('messagelogs')
notifymessages = config.get('notifymessages')
names = config.get("notifymessageWORDS")
notfiymessagesSOUND = config.get("notfiymessagesSOUND")
start_time = datetime.datetime.utcnow()
UserBot = commands.Bot( command_prefix=prefix, help_command=None, self_bot=True )

if messageLOG == "True":
	MessageLogEN = "Enabled"
else:
	MMessageLogEN = "Disabled"

if notifymessages == "True":
	notifymessagesEN = "Enabled"
else:
	notifymessagesEN = "Disabled"

def Setup():
	os.system('mode con: cols=60 lines=20')
	if platform.system() == "Windows":
		os.system('cls')
	else:
		os.system('clear')


def help():
	colors = [ Fore.RED, Fore.CYAN, Fore.BLUE, Fore.GREEN ]
	os.system('mode con: cols=75 lines=21')
	os.system("title Zerp / Command Help")
	print(f"{Fore.MAGENTA}> {Fore.RED}Zerp {Fore.CYAN}User Commands / Credits\n\n\n")
	print(f"{Fore.RED}> {random.choice(colors)}(clearlog) [logs]:{random.choice(colors)} Cleares The log file of Message logs.")
	print(f"{Fore.RED}> {random.choice(colors)}(hidecon) [hide]:{random.choice(colors)} Hides the current command prompt. see (showcon)")
	print(f"{Fore.RED}> {random.choice(colors)}(showcon) [show]:{random.choice(colors)} Shows the current command prompt. see (hidecon)")
	print(f"{Fore.RED}> {random.choice(colors)}(sendlog) [getlog]:{random.choice(colors)} Send The current file of message logs.")
	print(f"{Fore.RED}> {random.choice(colors)}(emoji) [eurl]:{random.choice(colors)} Gets the current emoji link.")
	print(f"{Fore.RED}> {random.choice(colors)}(ghostping) [gping]:{random.choice(colors)} You ping the user and we delete the message!")
	print(f"{Fore.RED}> {random.choice(colors)}(avitar) [av, pfp]:{random.choice(colors)} gets the mentioned user avitar.")
	print(f"{Fore.RED}> {random.choice(colors)}(lookup) [ip, geoip]:{random.choice(colors)} Prints out information about the given IP.")
	print(f"{Fore.RED}> {random.choice(colors)}(webdestroy) [wspam]:{random.choice(colors)} Uses another console where you can spam a webhook.")
	print(f"{Fore.RED}> {random.choice(colors)}(uptime) [usertime]:{random.choice(colors)} Prints out the Uptime of the userbot.")
	print(f"{Fore.RED}> {random.choice(colors)}(logout) [exit]:{random.choice(colors)} Exits the current User Bot.")
	print(f"\n{Fore.RED}> {random.choice(colors)}(Creation's#0001) {random.choice(colors)}[Credit: ALL]")

def HideCON(systray):
	hide = win32console.GetConsoleWindow()
	win32gui.ShowWindow(hide, win32con.SW_HIDE)

def ShowCON(systray):
	show = win32console.GetConsoleWindow()
	win32gui.ShowWindow(show, win32con.SW_SHOW)

def FixCON(systray):
	Setup()
	print(f'{Fore.MAGENTA}> {Fore.YELLOW}User Name: {UserBot.user.name}#{UserBot.user.discriminator}\n{Fore.MAGENTA}> {Fore.GREEN}User ID: {UserBot.user.id}\n{Fore.MAGENTA}> {Fore.CYAN}Servers: {str(len(UserBot.guilds))} \n{Fore.MAGENTA}> {Fore.WHITE}Bot Prefix: {prefix} \n{Fore.MAGENTA}> {Fore.BLUE}Message Logger: {MessageLogEN}\n{Fore.MAGENTA}> '+ '\033[20m' + f'Message Notifier: {notifymessagesEN}\n\n')

def on_quit(systray):
	try:
		systray.shutdown()
		sys.exit(0)
	except Exception as e:
		Setup()
		os.system("title Zerp / Exit")
		show = win32console.GetConsoleWindow()
		win32gui.ShowWindow(show, win32con.SW_SHOW)
		print( Fore.MAGENTA + "> " + Fore.RED + "User Bot" + Fore.YELLOW + " Has Been Closed," + Fore.BLUE + " Please Close this window.")

def tray():
	try:
		options = ("Fix Console", None, FixCON), ("Show Console", None, ShowCON), ("Hide Console", None, HideCON)
		systray = SysTrayIcon("indexes/extra/icon.ico", "Zerp / Tray Application", options, on_quit = on_quit)
		systray.start()
	except Exception as e:
		pass


def Main():
	Setup()
	tray()

	@UserBot.event
	async def on_connect():
		os.system("title Zerp / Main")
		print(f'{Fore.MAGENTA}> {Fore.YELLOW}User Name: {UserBot.user.name}#{UserBot.user.discriminator}\n{Fore.MAGENTA}> {Fore.GREEN}User ID: {UserBot.user.id}\n{Fore.MAGENTA}> {Fore.CYAN}Servers: {str(len(UserBot.guilds))} \n{Fore.MAGENTA}> {Fore.WHITE}Bot Prefix: {prefix} \n{Fore.MAGENTA}> {Fore.BLUE}Message Logger: {MessageLogEN}\n{Fore.MAGENTA}> '+ '\033[20m' + f'Message Notifier: {notifymessagesEN}\n\n')

	@UserBot.event
	async def on_message(message):
		for word in names:
			if word in message.content:
				if notifymessages == "True":
					print( f"{Fore.MAGENTA}> {Fore.RED}{word}{Fore.YELLOW} Was Said!{Fore.MAGENTA} /{Fore.BLUE} [{str(message.guild)}]{Fore.CYAN} [{str(message.channel)}]")			
					try:
						playsound(notfiymessagesSOUND)
					except Exception as e:
						pass
		if (message.author.bot):
			return
		if UserBot.user.mentioned_in(message):
			file = open("indexes/logs.txt", "a+", encoding='utf-8')
			file.write( "!!--------------------------!!\n[" + datetime.datetime.now().strftime("%H:%M:%S") +  f"]\n[User] {str(message.author)} \n[Guild] {str(message.guild)} \n[Channel] {str(message.channel)} \n[Mentioned] {str(message.content)}\n!!--------------------------!!\n")
			file.close()
		else:
			file = open("indexes/logs.txt", "a+", encoding='utf-8')
			file.write( "------------------------------\n[" + datetime.datetime.now().strftime("%H:%M:%S") +  f"]\n[User] {str(message.author)} \n[Guild] {str(message.guild)} \n[Channel] {str(message.channel)} \n[Message] {str(message.content)}\n------------------------------\n")
			file.close()
		await UserBot.process_commands(message)

	@UserBot.event
	async def on_message_edit(before, after):
		await UserBot.process_commands(after)

	@UserBot.event
	async def on_command_error(ctx, error):
		if isinstance(error, commands.CommandNotFound):
			await ctx.message.delete()
			print( Fore.MAGENTA + "> " + Fore.RED + "ERROR" + Fore.YELLOW + " Invalid Command!")

	class UserBotCMD(commands.Cog):
		def __init__(self, client):
			self.client = client

		@commands.command(aliases=['logs'])
		async def clearlog(self, ctx):
			await ctx.message.delete()
			open('indexes/logs.txt', 'w').close()
			print( Fore.MAGENTA + "> " + Fore.CYAN + "Successfully Cleared The" + Fore.RED + " log file" + Fore.YELLOW + "!")

		@commands.command(aliases=['hide'])
		async def hidecon(self, ctx):
			await ctx.message.delete()
			hide = win32console.GetConsoleWindow()
			win32gui.ShowWindow(hide, win32con.SW_HIDE)

		@commands.command(aliases=['show'])
		async def showcon(self, ctx):
			await ctx.message.delete()
			show = win32console.GetConsoleWindow()
			win32gui.ShowWindow(show, win32con.SW_SHOW)

		@commands.command(aliases=['getlog'])
		async def sendlog(self, ctx):
			await ctx.message.delete()
			try:
				with open("indexes/logs.txt", "rb") as file:
					await ctx.send(file=discord.File(file,'logs.txt'))
			except Exception as e:
				print(Fore.MAGENTA + "> " + Fore.RED + "Error " + Fore.BLUE + "Sending Message Logs" + Fore.YELLOW + "!")

		@commands.command()
		async def help(self, ctx):
			await ctx.message.delete()
			help()
			try:
				show = win32console.GetConsoleWindow()
				win32gui.ShowWindow(show , win32con.SW_SHOW)
				input(Fore.BLUE + "\n\nPlease press" + Fore.YELLOW + " ENTER " + Fore.BLUE + "to close ")
				Setup()
				os.system("title Zerp / Main")
				print(f'{Fore.MAGENTA}> {Fore.YELLOW}User Name: {UserBot.user.name}#{UserBot.user.discriminator}\n{Fore.MAGENTA}> {Fore.GREEN}User ID: {UserBot.user.id}\n{Fore.MAGENTA}> {Fore.CYAN}Servers: {str(len(UserBot.guilds))} \n{Fore.MAGENTA}> {Fore.WHITE}Bot Prefix: {prefix} \n{Fore.MAGENTA}> {Fore.BLUE}Message Logger: {MessageLogEN}\n{Fore.MAGENTA}> '+ '\033[20m' + f'Message Notifier: {notifymessagesEN}\n\n')
			except KeyboardInterrupt:
				quit()

		@commands.command(aliases=['wspam'])
		async def webdestroy(self, ctx):
			await ctx.message.delete()
			os.system('start cmd /c "python indexes/python/spammer.py" ')

		@commands.command(aliases=['usertime'])
		async def uptime(self, ctx):
			await ctx.message.delete()
			uptime = datetime.datetime.utcnow() - start_time
			uptime = str(uptime).split('.')[0]
			print(f'{Fore.MAGENTA}>{Fore.BLUE} Current UserBot{Fore.RED} Uptime:{Fore.YELLOW} {uptime}')

		@commands.command(aliases=['exit'])
		async def logout(self, ctx):
			await ctx.message.delete()
			Setup()
			os.system("title Zerp / Logout")
			os.system('mode con: cols=32 lines=5')
			print(f'{Fore.MAGENTA}>{Fore.BLUE} Current UserBot{Fore.RED} Was{Fore.YELLOW} CLOSED!')
			await UserBot.close()

		#stupid fucking emoji command jesus fuck i hate this command 
		@commands.command(aliases=['eurl', 'emote'])
		async def emoji(self, ctx, emoji: discord.Emoji):
			await ctx.message.delete()
			await ctx.send( emoji.url)

		@emoji.error
		async def emoji_error(self, ctx, error):
			if isinstance(error, commands.BadArgument):	
				await ctx.message.delete()
				print( Fore.MAGENTA + "> " + Fore.RED + "ERROR" + Fore.YELLOW + " Invalid Emoji!")

		@commands.command() #super cool frog lmao
		async def frog(self, ctx):
			await ctx.message.delete()
			try:
				with open("indexes/extra/frog.png", "rb") as file:
					await ctx.send(file=discord.File(file,'frog.png'))
			except Exception as e:
				print( Fore.MAGENTA + "> " + Fore.RED + "ERROR" + Fore.YELLOW + " Posting the FROG!")


		@commands.command(aliases=['gping'])
		async def ghostping(self, ctx):
			await ctx.message.delete()

		@commands.command(aliases=['av', 'pfp']) 
		async def avitar(self, ctx, *,  avamember : discord.Member=None):
			await ctx.message.delete()
			if not avamember:
				userAvatarUrl = ctx.message.author.avatar_url
				await ctx.send(userAvatarUrl)
			else:
				userAvatarUrl = avamember.avatar_url
				await ctx.send(userAvatarUrl)

		@commands.command(aliases=['ip', 'geopip'])
		async def lookup(self, ctx, *, ip: str = ''):
			os.system("title Zerp / IP Lookup")
			await ctx.message.delete()
			try:
				lookup = requests.get(f'http://ip-api.com/json/{ip}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query').json()
				colors = [ Fore.RED, Fore.CYAN, Fore.BLUE, Fore.GREEN ]
				fields = [
	            			{'name': 'IP', 'value': lookup['query']},
	            			{'name': 'Status', 'value': lookup['status']},
	            			{'name': 'Continent', 'value': lookup['continent']},
	            			{'name': 'Continent Code', 'value': lookup['continentCode']},
	            			{'name': 'Country Code', 'value': lookup['countryCode']},
	            			{'name': 'Region', 'value': lookup['region']},
	            			{'name': 'Region Name', 'value': lookup['regionName']},
	            			{'name': 'City', 'value': lookup['city']},
	            			{'name': 'District', 'value': lookup['district']},
	            			{'name': 'Zip', 'value': lookup['zip']},
	            			{'name': 'Timezone', 'value': lookup['timezone']},
	            			{'name': 'Currency', 'value': lookup['currency']},
	            			{'name': 'Isp', 'value': lookup['isp']},
	            			{'name': 'Org', 'value': lookup['org']},
	            			{'name': 'As', 'value': lookup['as']},
	            			{'name': 'Asname', 'value': lookup['asname']},
	            			{'name': 'Reverse', 'value': lookup['reverse']},
        				]
				for field in fields:
					if field['value']:
						print(Fore.BLUE + "> " + random.choice(colors) + field['name'] + " : " + field['value'])
				try:
					show = win32console.GetConsoleWindow()
					win32gui.ShowWindow(show , win32con.SW_SHOW)
					input(Fore.BLUE + "\n\nPlease press" + Fore.YELLOW + " ENTER " + Fore.BLUE + "to close\n")
					Setup()
					os.system("title Zerp / Main")
					print(f'{Fore.MAGENTA}> {Fore.YELLOW}User Name: {UserBot.user.name}#{UserBot.user.discriminator}\n{Fore.MAGENTA}> {Fore.GREEN}User ID: {UserBot.user.id}\n{Fore.MAGENTA}> {Fore.CYAN}Servers: {str(len(UserBot.guilds))} \n{Fore.MAGENTA}> {Fore.WHITE}Bot Prefix: {prefix} \n{Fore.MAGENTA}> {Fore.BLUE}Message Logger: {MessageLogEN}\n{Fore.MAGENTA}> '+ '\033[20m' + f'Message Notifier: {notifymessagesEN}\n\n')
				except KeyboardInterrupt:
					quit()
			except Exception as e:
				print(Fore.MAGENTA + "> " + Fore.RED + "Invalid IP Adress" + Fore.YELLOW + "!")

	UserBot.add_cog(UserBotCMD(UserBot))


	if token == "UserToken":
		Setup()
		os.system("title Zerp / ERROR")
		print(Style.BRIGHT + Fore.RED + "[" + Fore.GREEN + 'X' + Fore.RED + "]" + Fore.MAGENTA + " No user token provided.")
	else:
		try:
			UserBot.run(token, bot=False)
		except discord.errors.LoginFailure as e:
			print(Style.BRIGHT + Fore.RED + "[" + Fore.GREEN + 'X' + Fore.RED + "]" + Fore.MAGENTA + " Improper user token.")

Main()