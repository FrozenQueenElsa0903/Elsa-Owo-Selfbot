import base64
import requests
from signal import signal, SIGINT
from colorama import init
from requests import get,post
init()
import os
from os import execl, name, system
from sys import executable, argv
from time import sleep, strftime, localtime, time
#from solvecaptchalink import solvecaptchalink
import atexit
import random

from re import findall, sub
from base64 import b64encode
import json
from menu import UI
from color import color
from data import data
import threading


try:
    from playsound import playsound
    from twocaptcha import TwoCaptcha
    from inputimeout import inputimeout, TimeoutOccurred
    from discum import *
    from discum.utils.slash import SlashCommander
    from discord_webhook import DiscordWebhook
except:
	from setup import install
	install()
	from discum import *
	from discum.utils.slash import SlashCommander

wbm = [13, 16]
ui = UI()
client = data()
#Enter API 2Capcha	
if client.api.lower()!='none' or client.api.lower()!='no':
    api_key = os.getenv('APIKEY_2CAPTCHA', client.api)
    solver = TwoCaptcha(api_key, defaultTimeout=100, pollingInterval=5)
failtime=0
codefail=''      
def signal_handler(sig: object, frame: object):
	sleep(0.5)
	ui.slowPrinting(f"\n{color.fail}[INFO] {color.reset}Detected Ctrl + C, Stopping...")
	raise KeyboardInterrupt

signal(SIGINT, signal_handler)
bot = discum.Client(token=client.token, log=False, build_num=0, x_fingerprint="None", user_agent=[
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36/PAsMWa7l-11',
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 YaBrowser/20.8.3.115 Yowser/2.5 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.7.2) Gecko/20100101 / Firefox/60.7.2'])




while True:
	system('cls' if name == 'nt' else 'clear')
	ui.logo()
	ui.start()
	try:
		print(f"{color.okcyan}Automatically Pick Option [1] In 10 Seconds.")
		choice = inputimeout(prompt=f'{color.okcyan}Enter Your Choice: {color.okgreen}', timeout=10)
	except TimeoutOccurred:
		choice = "1"
	if choice == "1":
		if client.api.lower()=='none' or client.api.lower()=='no':			
			try:
				print('===========================================================')
				print(f"{color.okcyan}Which version do you prefer to solve captcha? Version [1] 1.0.4 or [2] 1.0.5 . Version 1.0.4 solve captcha not good")
				print(f"{color.okcyan}Automatically Pick Option [2] 1.0.5 In 10 Seconds.")
				version_choice = inputimeout(prompt=f'{color.okgreen}Enter Your Choice [1/2]: {color.okgreen}', timeout=15)
			except TimeoutOccurred:
				version_choice = "2"
			# version_choice = "2" #Toggle 1.0.5

			if version_choice == "1":
				captchaver='104'
				#print(f"{color.yellow}Chức năng đang debug! Xin vui lòng thử lại sau! Vẫn sử dụng 1.0.5 nhé =))  {color.reset}")
				#capchaver = 105
			elif version_choice == "2":
				captchaver = '105'
			else:
				print(f'{color.fail} !! [ERROR] !! {color.reset} Wrong input!')
				sleep(1)
				os.system('python "mainvip.py"')
				#execl(executable, executable, *argv)
		else:
			captchaver='vip'
		
	

  
		if client.casinom.lower() == "yes":
			try:
				print('')
				print(f'{color.okcyan}Do you want to auto Casino in this Auto [1:YES/2:NO]? {color.okgreen}')
				print(f'{color.okcyan}Automatically Pick Option [1:Yes] In 10 Seconds.{color.okgreen}')
				casino_choice = inputimeout(prompt=f'{color.okgreen}Enter Your Choice [1/2]: {color.okgreen}', timeout=10)
			except TimeoutOccurred:
				casino_choice = '1'
		else:
			print(f"{color.yellow}Bạn đang không mở auto CoinFlip in BOT{color.reset}")
			casino_choice = '2'
		if casino_choice == '2' or casino_choice.lower() == 'no':
			client.casinom = "no"
		# if casino_choice == '1' or casino_choice.lower()=='yes':
		# client.cfm="yes"
		# print(f"{color.yellow}Chức năng đang debug! Xin vui lòng thử lại sau! =))  {color.reset}")
		# sleep(3)
		# client.cfm = "no"
		if casino_choice != '2' and casino_choice.lower() != 'no' and casino_choice != '1' and casino_choice.lower() != 'yes':
			print(f'{color.fail} !! [ERROR] !! {color.reset} Wrong input!')
			sleep(1)
			os.system('python "mainvip.py"')
			#(executable, executable, *argv)
		
		# Thoát vòng chọn menu
		break


	elif choice == "2":
		from newdata import main

		main()
	elif choice == "3":
		ui.info()
		continue
	else:
		print(f'{color.fail} !! [ERROR] !! {color.reset} Wrong input!')
		sleep(1)
		os.system('python "mainvip.py"')
		#execl(executable, executable, *argv)


def at():
	return f'\033[0;43m{strftime("%d %b %Y %H:%M:%S", localtime())}\033[0;21m'


if False in bot.checkToken(client.token):
	print(f"{color.fail}[ERROR]{color.reset} Invalid Token")
	sleep(5)
	raise SystemExit


@bot.gateway.command
def on_ready(resp):
	if resp.event.ready_supplemental:  # ready_supplemental is sent after ready
		user = bot.gateway.session.user
		client.username = user['username']
		client.userid = user['id']
		print('')
		ui.slowPrinting(f"Logged in as {color.yellow}{user['username']}#{user['discriminator']}{color.reset}")
		sleep(1)
		print('═' * 25)
		print('')
		print(f"{color.purple}Settings: {color.reset}")
		print(f"{color.purple}Channel: {client.channel}{color.reset}")
		print(f"{color.purple}----------------------------------{color.reset}")
		print(f"{color.purple}Hunt Mode: {client.rhunt}{color.reset}")		
		print(f"{color.purple}Battle Mode: {client.rbattle}{color.reset}")
		print(f"{color.purple}Say Owo Mode: {client.rowo}{color.reset}")
		print(f"{color.purple}Buy Ring Mode: {client.rbuyring}{color.reset}")  
		print(f"{color.purple}Open Lootbox: {client.lbox}{color.reset}")
		print(f"{color.purple}Open Weapon Crate: {client.wcrate}{color.reset}")
		print(f"{color.purple}Use Gem Method: {client.usegem}{color.reset}")
		print(f"{color.purple}Sleep Mode: {client.sm}{color.reset}")
		print(f"{color.purple}Pray/Curse Mode: {client.pm}{color.reset}")
		print(f"{color.purple}Pray/Cure for ID: {client.prayid}{color.reset}")
		print(f"{color.purple}EXP Mode: {client.em}{color.reset}")
		print(f"{color.purple}Daily Mode: {client.daily}{color.reset}")
		print(f"{color.purple}{'Stop After (Seconds)' if client.stop.isdigit() else 'Stop Mode'}: {client.stop}{color.reset}")
		print(f"{color.purple}Sell Mode: {client.sell}{color.reset}")
		print(f"{color.purple}----------------------------------{color.reset}")
		print(f"{color.purple}Selfbot Commands Prefix: '{client.prefix}'{color.reset}")
		print(f"{color.purple}Selfbot Commands Allowedid: {client.allowedid}{color.reset}")
		print(f"{color.purple}Webhook: {'YES' if client.webhook != 'None' else 'NO'}{color.reset}")
		print(f"{color.purple}Webhook Ping: {client.webhookping}{color.reset}")
		print(f"{color.purple}Solve Captcha Mode: {client.solve}{color.reset}")
		print(f"{color.purple}----------------------------------{color.reset}")
		print(f"{color.purple}Auto Casinom: {client.casinom}{color.reset}")
		if client.casinom.lower()=='yes':
			print(f"{color.purple}Auto CoinFlip: {client.cfm}{color.reset}")
			print(f"{color.purple}Min Bet of Coinflip: {client.cfbet}{color.reset}")
			print(f"{color.purple}Rate Multiple of Coinflip: {client.cfrate}{color.reset}")
			print(f"{color.purple}Auto Owo Slot: {client.osm}{color.reset}")
			print(f"{color.purple}Min Bet of Coinflip: {client.osbet}{color.reset}")
			print(f"{color.purple}Rate Multiple of Coinflip: {client.osrate}{color.reset}")
			print(f"{color.purple}Max Bet Method: {client.maxbet}{color.reset}")
		print(f"{color.purple}----------------------------------{color.reset}")
		print(f"{color.purple}Sound: {client.sound}{color.reset}")
		print('═' * 25)


def webhookPing(message):
	if client.webhook != 'None':
		webhook = DiscordWebhook(url=client.webhook, content=message)
		webhook = webhook.execute()

def captchamusic():
	if client.sound == 'yes':
		playsound('KhueMocLang.mp3')
     #playsound('Captcha.mp3')
      

def solvedmusic():
	if client.sound == 'yes':
		playsound('Solved.mp3')
		#playsound('KhueMocLang.mp3')

def kiepdoden():
	if client.sound=='yes':
		playsound("KiepDoDen.mp3")

@bot.gateway.command
def security(resp):
	threadcaptchamusic = threading.Thread(name="captchamusic", target=captchamusic)
	threadsolvedmusic = threading.Thread(name="solvedmusic", target=solvedmusic)
	if issuechecker(resp) == "solved":	
		if client.casinom.lower() == 'yes' :
			webhookPing(f"<@{client.webhookping}> [SUCCESS] I have solved the captcha succesfully in Channel: <#{client.channel}> or <#{client.channelocf}> . User: {client.username} ")  			
		else:
			webhookPing(f"<@{client.webhookping}> [SUCCESS] I have solved the captcha succesfully in Channel: <#{client.channel}> . User: {client.username} ") 
		if captchaver =='vip':
			webhookPing(f'2Captcha Balance: {solver.balance()} $')
		webhookPing("===========================================================================================")
		#threadsolvedmusic.start()
		sleep(3)
		print(f'{color.okcyan}[INFO] {color.reset}Captcha Solved. Started To Run Again')
		os.system('python "mainvip.py"')
		#execl(executable, executable, *argv)
	if issuechecker(resp) == "captcha":
		client.stopped = True
		webhookping()
		threadcaptchamusic.start()
		bot.switchAccount(client.token[:-4] + 'FvBw')

#@bot.gateway.command
#def checkrepOWO(resp):
#	if client.stopped != True:
#		oworep=False
#		if resp.event.message:
#			msgs = bot.getMessages(str(client.channel), num=10)
#			msgs = msgs.json()
#			for i in range(len(msgs)):
#				if msgs[i]['author']['id'] == client.OwOID and client.username in msgs[i]['content']:
#					oworep=True
#			if oworep==False:
#				print(f'{color.warning} [WARNING] {color.okcyan}Maybe OWO doesnt respone our message. {color.fail}Check! {color.reset}')
#				sleep(5)


# Ping Webhook moded
def webhookping():
	if client.webhookping != 'None':
		if client.casinom.lower() == 'yes' :
			webhookPing(f"<@{client.webhookping}> I Found A Captcha In Channel: <#{client.channel}> or <#{client.channelocf}> . User: {client.username} <@{client.userid}>")			
		else:
			webhookPing(f"<@{client.webhookping}> I Found A Captcha In Channel: <#{client.channel}>  . User: {client.username} <@{client.userid}>")

	else:
		if client.casinom.lower() == 'yes' :
			webhookPing(f"<@{client.userid}> <@{client.allowedid}> I Found A Captcha In Channel: <#{client.channel}>  or <#{client.channelocf}> . User: {client.username} <@{client.userid}>")
		else:
			webhookPing(f"<@{client.userid}> <@{client.allowedid}> I Found A Captcha In Channel: <#{client.channel}>. User: {client.username} <@{client.userid}>")



    


@bot.gateway.command
def issuechecker(resp):
    
	def getAnswer(img,lenghth,code):
		count=0
		timeanswer=time()
		while True:
			if time() - timeanswer < 300 :
				count+=1
				r = solver.normal(img,numeric=2,minLen=lenghth,maxLen=lenghth,phrase=0,caseSensitive=0,calc=0,lang='en',textinstructions=code,)
		
				if r['code'].isalpha():
					if len(r['code'])==lenghth:
						print('Check result 2 captcha')
						return r
					else:
						solver.report(r['captchaId'], False) 
						print(f'Time: {count}. The length of result {r["code"]} is not right.Try again')
						
				else:
					solver.report(r['captchaId'], False) 
					print(f'Time: {count}. The result {r["code"]} contants number.Try again')
			else:
				print(f'TIME OUT 5 MINUTES for SOLVE')
				return 'captcha'
	try:
		user = bot.gateway.session.user

		def dms():
			i = 0
			length = len(bot.gateway.session.DMIDs)
			while i < length:
				if client.OwOID in bot.gateway.session.DMs[bot.gateway.session.DMIDs[i]]['recipients']:
					return bot.gateway.session.DMIDs[i]
				else:
					i += 1

		dmsid = dms()
	except:
		dmsid = None

	def solve(image_url, msgs):
		threadcaptcha = threading.Thread(name="captchamusic", target=captchamusic)
		try:
			if captchaver == '105' or captchaver == 'vip':
				if captchaver=='105':
					client.stopped = True
					from api import CAPI
					api = CAPI(user['id'])
					encoded_string = b64encode(get(image_url).content).decode('utf-8')
					r = api.solve(Json={'data': encoded_string, 'len': msgs[msgs.find("letter word") - 2]})
					if r:
						ui.slowPrinting(f"{color.okcyan}[INFO] {color.reset}Solved Captcha [Code: {r['code']}]")
						bot.sendMessage(dmsid, r['code'])
						sleep(10)
						msgs = bot.getMessages(dmsid)
						try:
							msgs = json.loads(msgs.text[1:-1]) if type(msgs.json()) is list else {'author': {'id': '0'}}
						except:
							webhookping()
									
							threadcaptcha.start()
							ui.slowPrinting(f"{color.okcyan}[INFO] {color.reset}There's An Issue With Rerunner")
							sleep(2)
							return "captcha"
						if msgs['author']['id'] == client.OwOID and "verified" in msgs['content']:
							api.report(Json={'captchaId': r['captchaId'], 'correct': 'True'})
							return "solved"
						else:
							webhookping()
							threadcaptcha.start()
							ui.slowPrinting(f"{color.okcyan}[INFO] {color.reset}Selfbot Stopped As The Captcha Code Is Wrong")
							api.report(Json={'captchaId': r['captchaId'], 'correct': 'False'})
							return "captcha"
					elif r == False:
						webhookping()
						threadcaptcha.start()
						ui.slowPrinting(f"{color.okcyan}[INFO] {color.reset}You Haven't Registered To Our Captcha Solving API!")
						ui.slowPrinting("To Register Join Our Discord Server: https://discord.gg/9uZ6eXFPHD And Send \"bot register\" in bot command channel")
						return "captcha"
					else:
						webhookping()
						threadcaptcha.start()
						ui.slowPrinting(f"{color.okcyan}[INFO] {color.reset}Captcha Solver API Is Having An Issue...")
						return "captcha"
 			
				if captchaver=='vip':
					client.stopped = True	
					encoded_string = b64encode(get(image_url).content).decode('utf-8')		
					countlen=int(msgs[msgs.find("letter word") - 2])
     
					#Check balance of 2Captcha
					captchabalance = solver.balance()    
					if captchabalance==0:
						ui.slowPrinting(f'Balance 2CAPCHA : {captchabalance} $ Out of money')
						webhookPing(f"<@{client.webhookping}> [FAIL]Out of money . User: {client.username} <@{client.userid}>")
						webhookPing(f"=========================================================================================")
						return "captcha"

					#Solve by 2Captcha
					code=""
					r = getAnswer(encoded_string,countlen,code)
					try:
						if r=='captcha':
							return 'captcha'
					except:
						pass
					captchabalance = solver.balance()
					ui.slowPrinting(f'Balance 2CAPCHA : {captchabalance} $')
					ui.slowPrinting(f"{color.okcyan}[INFO] {color.reset}Solving Captcha at 1st chance: [Code: {r['code']}]")
					bot.sendMessage(dmsid, r['code'])
					sleep(5)
				
					msgs = bot.getMessages(dmsid)
					try:
						msgs = json.loads(msgs.text[1:-1]) if type(msgs.json()) is list else {'author': {'id': '0'}}
					except:
						ui.slowPrinting(f"{color.okcyan}[INFO] {color.reset}There's An Issue With Rerunner")
						webhookPing(f"=========================================================================================")
						sleep(2)
						return "captcha"					
					if msgs['author']['id'] == client.OwOID and "verified" in msgs['content']:	
						solver.report(r['captchaId'], True)
						return "solved"
					if msgs['author']['id'] == client.OwOID and "Wrong verification code" in msgs['content']:
						webhookping()
						webhookPing(f"<@{client.webhookping}> [FAIL]I have solved the captcha fail in the 1st chance. Wait me at the 2nd chance. Sorry . User: {client.username} <@{client.userid}>")
						solver.report(r['captchaId'], False)  #Báo kết quả sai 
						textand='and'
						textwrong='IS WRONG'
						textjoin=[r['code'],textwrong]
						texthint=' '.join(textjoin)
						code=texthint
						r2 = getAnswer(encoded_string,countlen,code)
						try:
							if r=='captcha':
								return 'captcha'
						except:
							pass
						ui.slowPrinting(f"{color.okcyan}[INFO] {color.reset}Solving Captcha at 2nd chance: [Code: {r2['code']}]")   
						bot.sendMessage(dmsid, r2['code'])						
						captchabalance = solver.balance()
						ui.slowPrinting(f'Balance 2CAPCHA : {captchabalance} $')
						sleep(3)
						msgs = bot.getMessages(dmsid)      
						try:
							msgs = json.loads(msgs.text[1:-1]) if type(msgs.json()) is list else {'author': {'id': '0'}}
						except:
							webhookping()
							threadcaptcha.start()
							ui.slowPrinting(f"{color.okcyan}[INFO] {color.reset}There's An Issue With Rerunner")
							webhookPing(f"=========================================================================================")
							sleep(2)
							return "captcha"      
						if msgs['author']['id'] == client.OwOID and "verified" in msgs['content']:		
							solver.report(r2['captchaId'], True)
							return "solved"
						if msgs['author']['id'] == client.OwOID and "Wrong verification code" in msgs['content']:
							solver.report(r2['captchaId'], False) 
							textjoin=[r2["code"],textand,textjoin,"ARE WRONG"]
							texthint=' '.join(textjoin)
							code=texthint
							r3 = getAnswer(encoded_string,countlen,code)
							try:
								if r=='captcha':
									return 'captcha'
							except:
								pass
							ui.slowPrinting(f"{color.okcyan}[INFO] {color.reset}Solving Captcha at 3rd chance: [Code: {r3['code']}]") 
							bot.sendMessage(dmsid, r3['code'])  
							captchabalance = solver.balance()
							ui.slowPrinting(f'Balance 2CAPCHA : {captchabalance} $')
							sleep(3)
							msgs = bot.getMessages(dmsid)      
							try:
								msgs = json.loads(msgs.text[1:-1]) if type(msgs.json()) is list else {'author': {'id': '0'}}
							except:
								webhookping()
								threadcaptcha.start()
								ui.slowPrinting(f"{color.okcyan}[INFO] {color.reset}There's An Issue With Rerunner")
								webhookPing(f"=========================================================================================")
								sleep(2)
								return "captcha"      
							if msgs['author']['id'] == client.OwOID and "verified" in msgs['content']:		
								solver.report(r3['captchaId'], True)
								return "solved"
							if msgs['author']['id'] == client.OwOID and "Wrong verification code" in msgs['content']:	       
								solver.report(r3['captchaId'], False) 
								threadcaptcha.start()
								webhookPing(f"<@{client.webhookping}> [FAIL]I have solved the captcha fail in the 3rd chance. Sorry very much. Please solve the captcha by yourself in the last chance. Carefully. Good Luck . User: {client.username} <@{client.userid}>")
								return 'captcha'	
							return 'captcha'	
						return 'captcha'	
					return 'captcha'	
       
       

							
					
      
                
			if captchaver == '104':
				img_data = requests.get(image_url).content
				with open('captcha.png', 'wb') as handler:
					handler.write(img_data)
				with open('captcha.png', "rb") as image_file:
					encoded_string = base64.b64encode(image_file.read())
				userid = random.choice(['hoanghaianh', 'ahihiyou20'])
				data = {'userid': userid,'apikey': '5JzPnvYKF7iyHGIBYBXG' if userid == 'hoanghaianh' else 'EylMgbLUe0v4Jxi69fTN','data': str(encoded_string)[2:-1],'case': 'mixed'}
				r = requests.post(url='https://api.apitruecaptcha.org/one/gettext', json=data)
				j = json.loads(r.text)
				print(f"{color.okcyan}[INFO] {color.reset}Solved Captcha [Code: {j['result']}]")
				return "captcha"
		except:
			webhookping()
			threadcaptcha.start()
			return "captcha" 
 
 
            
     
	def solvelink():
		if client.api.lower() != 'none' or client.api.lower() !='no':	
			api=client.api
			token =client.token

			from selenium import webdriver
			from selenium.webdriver.common.by import By
			from selenium.webdriver.support.ui import WebDriverWait
			from selenium.webdriver.support import expected_conditions as EC
			from selenium.webdriver.chrome.options import Options
			import undetected_chromedriver as uc

					#Setting Chrom extension
			chrome_options = uc.ChromeOptions()
			chrome_options.add_extension('TwoCaptchaAutoSolve.crx')

			driver = uc.Chrome(options=chrome_options)



					#Setting key 2Captcha Solver
			driver.get('chrome-extension://ifibfemgeogfhoebkmokieepdoobkbpo/options/options.html')
			inputkey = driver.find_element(By.CSS_SELECTOR, value='body > div > div.content > table > tbody > tr:nth-child(1) > td:nth-child(2) > input[type=text]')
			driver.execute_script("document.getElementsByName('apiKey')[0].value=arguments[0]",api)


					#click Login
			loginbutton=driver.find_element(By.CSS_SELECTOR, "#connect")
			driver.execute_script("arguments[0].click();", loginbutton)




					#Tắt Alert
			WebDriverWait(driver, 10).until(EC.alert_is_present())
			driver.switch_to.alert.accept()

					#Test Web 2Captcha Demo
					#driver.get('https://2captcha.com/demo/hcaptcha?difficulty=hard')


					#OWO

			driver.get('https://owobot.com/captcha')

			js = 'function login(token) {setInterval(() => {document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`}, 50);setTimeout(() => {location.reload();}, 500);}'
			WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#app > div.v-dialog__content.v-dialog__content--active > div > div > div.v-card__actions.actions > button')))
			driver.find_element(By.CSS_SELECTOR, value='#app > div.v-dialog__content.v-dialog__content--active > div > div > div.v-card__actions.actions > button').click()

			driver.execute_script(js + f'login("{token}")')

			WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[class="button-f2h6uQ lookFilled-yCfaCM colorBrand-I6CyqQ sizeMedium-2bFIHr grow-2sR_-F"]')))
			driver.find_element(By.CSS_SELECTOR, value='button[class="button-f2h6uQ lookFilled-yCfaCM colorBrand-I6CyqQ sizeMedium-2bFIHr grow-2sR_-F"]').click()





					#Dợi extension solver hiện rồi f5 vì để ko bị lỗi sitekey
			WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "captcha-solver")))
			driver.refresh()
			WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "captcha-solver")))
			solvebutton=driver.find_element(By.CLASS_NAME, "captcha-solver")
			sleep(3)
			driver.execute_script("arguments[0].click();", solvebutton)			
				#Wait 
			if WebDriverWait(driver, 200).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#app > div > main > div > div > div > div:nth-child(2) > div > div.v-card__actions.mb-3.welcome-text > div"), "I have verified that you're a human")):
				print('Solve Captcha Succesfully')		
				webhookPing(f"Solve Captcha link successfully")
				driver.quit()		
				return "solved"
			else:	
				return "captcha"
			


	if resp.event.message:
		threadcaptcha = threading.Thread(name="captchamusic", target=captchamusic)
		m = resp.parsed.auto()
		if m['channel_id'] == client.channel or m['channel_id'] == client.channelocf or m['channel_id'] == dmsid and not client.stopped:
			if m['author']['id'] == client.OwOID or m['author']['username'] == 'OwO' or m['author']['discriminator'] == '8456' and not client.stopped:
				if client.username in m['content'] and 'banned' in m['content'].lower() and not client.stopped:
					client.stopped =True
					ui.slowPrinting(f'{at()}{color.fail} !!! [BANNED] !!! {color.reset} Your Account Have Been Banned From OwO Bot Please Open An Issue On The Support Discord server')
					return "captcha"
				if client.username in m['content'] and any(captcha in m['content'].lower() for captcha in ['(1/5)', '(2/5)', '(3/5)', '(4/5)','(5/5)']) and not client.stopped:
					msgs = bot.getMessages(dmsid)
					msgs = msgs.json()
					if type(msgs) is dict:
						client.stopped =True
						ui.slowPrinting(f'{at()}{color.warning} !! [CAPTCHA] !! {color.reset} ACTION REQUİRED')
						return "captcha"
					if client.username in m['content'] and msgs[0]['author']['id'] == client.OwOID and '⚠' in msgs[0]['content'] and msgs[0]['attachments'] and not client.stopped:
						ui.slowPrinting(f'{at()}{color.warning} !! [CAPTCHA] !! {color.reset} ACTION REQUİRED')
						if client.solve.lower() != "no" and not client.stopped:
							return solve(msgs[0]['attachments'][0]['url'], msgs[0]['content'])
						client.stopped =True
						return "captcha"
					elif msgs[0]['author']['id'] == client.OwOID and 'link' in msgs[0]['content'].lower() and not client.stopped:
						client.stopped =True
						webhookPing(f"<@{client.webhookping}> [WARNIG] CAPTCHA LINK. User: {client.username} <@{client.userid}>")						
						threadcaptcha.start()			
						client.stopped=True						
						return solvelink()			
						return "captcha"
					msgs = bot.getMessages(str(client.channel), num=10)
					msgs = msgs.json()
					for i in range(len(msgs)):
						if client.username in m['content'] and msgs[i]['author']['id'] == client.OwOID and 'solving the captcha' in msgs[i]['content'].lower() and not client.stopped:
							ui.slowPrinting(f'{at()}{color.warning} !! [CAPTCHA] !! {color.reset} ACTION REQUİRED')
							if client.solve.lower() != "no" and not client.stopped:
								return solve(msgs[i]['attachments'][0]['url'], msgs[0]['content'])
							client.stopped =True
							return "captcha"
						else:
							if i == len(msgs) - 1:
								client.stopped =True
								return "captcha"
				if client.username in m['content'] and '⚠' in m['content'].lower() and not client.stopped:
					if client.solve.lower() != "no" and m['attachments'] and not client.stopped:
						client.stopped =True
						ui.slowPrinting(f'{at()}{color.warning} !! [CAPTCHA] !! {color.reset} ACTION REQUİRED')
						return solve(m['attachments'][0]['url'], m['content'])
					client.stopped =True
					ui.slowPrinting(f'{at()}{color.warning} !! [CAPTCHA] !! {color.reset} ACTION REQUİRED')
					return "captcha"


					
def changeChannel() -> str:
		channel2 = []
		guildspamID = bot.getChannel(client.channelspambackup).json()['guild_id']
		channels = bot.gateway.session.guild(guildspamID).channels
		for i in channels:
			if channels[i]['type'] == "guild_text":
				channel2.append(i)
		channel2 = random.choice(channel2)
		return channel2, channels[channel2]['name']


@bot.gateway.command	
def checkballance(resp):
	if client.cfm.lower() == 'yes' and client.checknocash == False and client.stopped != True:
		if resp.event.message:
			m = resp.parsed.auto()
			if m['channel_id'] == client.channelocf and client.stopped == False:
				if m['author']['id'] == client.OwOID and client.username in m['content'] and 'you currently have' in m['content']:
					client.cash = findall('[0-9]+', m['content'])
					print("{}You currently have: {} Cowoncy! {}".format(color.warning, ','.join(client.cash[1::]),color.reset))
			if client.username in m['content'] and 'You don\'t have enough cowoncy!' in m['content']:
				print(f"{color.fail} [ERROR] Not Enough Cowoncy To Continue! {color.reset}")
				client.checknocash = True


# Gems
@bot.gateway.command
def checkgem(resp):
	if client.gm.lower() == 'yes' and client.stopped != True:
		if resp.event.message:
			m = resp.parsed.auto()
			if m['channel_id'] == client.channel and client.stopped != True:
				if m['author']['id'] == client.OwOID:
					if client.username in m['content'] and "**🌱" in m['content']:
						print(f'{at()}{color.warning} !! [CHECK HUNT] !! {color.reset} ')
					if client.username in m['content'] and  "and caught" in m['content'] and client.checknogem == False:
						print(f'{at()}{color.warning} !! [CHECK GEM] checknogem = {client.checknogem}!! {color.reset} ')
						# Gems.useGems()
						useGem()


def useGem():
	if client.gm.lower() == 'yes' and client.stopped != True:
		bot.typingAction(str(client.channel))
		sleep(1.5)
		bot.sendMessage(str(client.channel), "owo inv")
		print(f"{at()}{color.okcyan} User: {client.username}{color.okgreen} [SENT] {color.reset} owo inv")
		client.totalcmd += 1
		sleep(4)
		msgs = bot.getMessages(str(client.channel), num=10)
		msgs = msgs.json()
		inv = ""
		for i in range(len(msgs)):
			if msgs[i]['author']['id'] == client.OwOID and 'Inventory' in msgs[i]['content']:
				inv = findall(r'`(.*?)`', msgs[i]['content'])
		if not inv:
			sleep(2)
			client.totalcmd -= 1
			useGem()
		else:
			if '050' in inv:
				if client.lbox.lower() == "yes" and client.stopped != True:
					bot.sendMessage(str(client.channel), "owo lb all")
					print(f"{at()}{color.okcyan} User: {client.username}{color.okgreen} [SENT] {color.reset} owo lb all")
					sleep(12)

			if '100' in inv:
				if client.wcrate.lower() == "yes" and client.stopped != True:
					bot.sendMessage(str(client.channel), "owo crate all")
					print(f"{at()}{color.okcyan} User: {client.username}{color.okgreen} [SENT] {color.reset} owo crate all")

					sleep(2)
			for item in inv:
				try:
					if int(item) >= 100 or int(item) <= 50:
						inv.pop(inv.index(item))  # weapons
				except:  # backgounds etc
					inv.pop(inv.index(item))
			tier = [[], [], []]
			countGem = [0, 0, 0, 0, 0, 0, 0]
			print(f"{at()}{color.reset} ===========")

			print(f"{at()}{color.okblue} [INFO] {color.reset} Found {len(inv)} Gems Inventory")
			available = []
			for gem in inv:
				gem = sub(r"[^a-zA-Z0-9]", "", gem)
				gem = int(gem)
				for i in range(0, 6, 1):
					if gem == 51 + i or gem == 65 + i or gem == 72 + i:
						countGem[i] += 1

			print(f"{at()}{color.reset} ===========")

			print(f"{at()}{color.okgreen} [INFO] {color.okcyan}\n")
			print(f" 		     Gem C: {countGem[0]} loại\n")
			print(f" 		     Gem U: {countGem[1]} loại\n")
			print(f" 		     Gem R: {countGem[2]} loại\n")
			print(f"		     Gem E: {countGem[3]} loại\n")
			print(f" 		     Gem M: {countGem[4]} loại\n")
			print(f" 		     Gem L: {countGem[5]} loại\n")
			print(f" 		     Gem F: {countGem[6]} loại {color.reset}")
			print(f"{at()}{color.reset} ===========")
			sleep(1)
			nogem = False
			if client.usegem.lower() == 'min':
				for i in range(0, 5, 1):  # i=4 => Gem Mythic
					if use3gem(i + 1, countGem[i]):
						nogem = False
						break
					else:
						nogem = True
			if client.usegem.lower() == 'max':
				for i in range(4, -1, -1):  # i=4 => Gem Mythic
					if use3gem(i + 1, countGem[i]):
						nogem = False
						break
					else:
						nogem = True
			if nogem:
				client.checknogem = True
				#print(f"{at()}{color.fail} [INFO] {color.reset} {client.checknogem}")
				print(f"{at()}{color.fail} [INFO] {color.reset} Ko có bộ 3 GEM giống nhau . Ko sử dụng GEM nhé")


def use3gem(level, count):
	if client.gm.lower() == 'yes' and client.stopped != True:
		a = 50
		b = 64
		c = 71
		# 1 51 65 72 Common
		# 2 52 66 73 Uncommon
		# 3 53 67 74 Rare
		# 4 54 68 75 Epic
		# 5 55 69 76 Mythic
		# 6 56 70 77 Legend
		# 7 57 71 78 Fabled
		a = a + level
		b = b + level
		c = c + level
		typegem = ""
		turngem = 0
		if level == 1:
			typegem = 'Common'.upper()
			turngem = 25
		if level == 2:
			typegem = 'UnCommon'.upper()
			turngem = 25
		if level == 3:
			typegem = 'Rare'.upper()
			turngem = 50
		if level == 4:
			typegem = 'Epic'.upper()
			turngem = 75
		if level == 5:
			typegem = 'Mythic'.upper()
			turngem = 75
		if level == 6:
			typegem = 'Legend'.upper()
			turngem = 100
		if level == 7:
			typegem = 'Fabled'.upper()
			turngem = 100

		if count == 3:
			sleep(2)
			bot.sendMessage(str(client.channel), "owo use {} {} {}".format(str(a), str(b), str(c)))
			print(f"{at()}{color.okcyan} User: {client.username}{color.okgreen} [SENT] {color.reset} owo use {a} {b} {c} [GEMS {color.purple}{typegem}{color.reset}][{color.cyan}{str(turngem)} turn{color.reset}]")
			client.checkusegem += 1
			print(f'{at()}{color.warning} [INFO] !! [USE GEM lần {client.checkusegem}] !! {color.reset} ')
			return True
		else:
			return False

@bot.gateway.command
def checkcf(resp):
	if client.cfm.lower() == 'yes' and client.checknocash == False and client.stopped != True:
		if resp.event.message_updated:
			m = resp.parsed.auto()
			try:
				if m['channel_id'] == client.channelocf:
					if m['author']['id'] == client.OwOID:
						if client.username in m['content'] and 'and chose' in m['content']:
							if 'and you won' in m['content']:
								print("{}[INFO WIN] {} OCF Won: {} Cowoncy/ {}Total Won: {} Cowoncy/ {}Total Lose: {} Cowoncy/ {}Last Benefit: {} Cowoncy. {} ".format(color.okgreen,client.username, client.current_cfbet, color.okcyan,client.totalwon + client.current_cfbet, color.pink, client.totallost,color.purple, client.totalwon + client.current_cfbet - client.totallost,color.reset))
								client.countcfmaxlost =0
								client.totalwon += client.current_cfbet
								if client.current_cfbet == 150000:
									bot.typingAction(str(client.channelocf))
									bot.sendMessage(str(client.channelocf), "owo cash")
								client.current_cfbet = client.cfbet
								sleep(1)
							if 'and you lost it all... :c' in m['content']:
								print("{}[INFO LOSE] {} OCF Lost: {} Cowoncy/ {}Total Won: {} Cowoncy/ {}Total Lose: {} Cowoncy/ {}Last Benefit: {} Cowoncy. {}  ".format(color.fail,client.username, client.current_cfbet, color.okcyan, client.totalwon, color.pink,client.totallost + client.current_cfbet, color.purple,client.totalwon - client.current_cfbet - client.totallost, color.reset))
								client.totallost += client.current_cfbet
								if client.current_cfbet == 150000:
									client.countcfmaxlost += 1
									if client.countcfmaxlost==1:
										threadkiepdoden = threading.Thread(name="kiepdoden", target=kiepdoden)
										threadkiepdoden.start()									
									print(f'{color.warning} [WARNING] {color.fail}Bạn đang thua sấp mặt. Hãy quay xe ngay. Người không chơi là người chiến thắng. {color.reset}')

									bot.sendMessage(str(client.channelocf), "owo cash")
									if client.maxbet.lower() == "allin":
										client.current_cfbet = 150000
									if client.maxbet.lower() == "reset":
										client.current_cfbet = client.cfbet
								client.current_cfbet *= client.cfrate
								if client.current_cfbet >= 150000:
									client.current_cfbet = 150000
								sleep(1)						
			except KeyError:
				pass

@bot.gateway.command
def checkos(resp):
	if client.osm.lower() == 'yes' and client.checknocash == False and client.stopped != True:
		if resp.event.message_updated:
			m = resp.parsed.auto()
			try:
				if m['channel_id'] == client.channelocf:
					if m['author']['id'] == client.OwOID:
						if client.username in m['content'] and 'bet' in m['content'] and '___SLOTS___' in m['content']:
							if 'and won <:cowoncy:416043450337853441>' in m['content']:
								if '<:eggplant:417475705719226369> <:eggplant:417475705719226369> <:eggplant:417475705719226369>' not in m['content'] and '<:cowoncy:417475705912426496> <:cowoncy:417475705912426496> <:cowoncy:417475705912426496>'not in m['content'] and '<:cherry:417475705178161162> <:cherry:417475705178161162> <:cherry:417475705178161162>'not in m['content'] and '<:o:417475705899843604 > <:w_:417475705920684053> <:o_:417475705899843604>'not in m['content']:
									print("{}[INFO WIN] {} OS Won: {} Cowoncy/ {}Total Won: {} Cowoncy/ {}Total Lose: {} Cowoncy/ {}Last Benefit: {} Cowoncy. {} ".format(color.okgreen,client.username, client.current_osbet, color.okcyan,client.totalwon + client.current_osbet, color.pink, client.totallost,color.purple, client.totalwon + client.current_osbet - client.totallost,color.reset))
									#client.countmaxlost =0
									client.totalwon += client.current_osbet
									if client.current_osbet == 150000:
										bot.typingAction(str(client.channelocf))
										bot.sendMessage(str(client.channelocf), "owo cash")
									client.current_osbet = client.osbet
									sleep(1)       
							if ' and won nothing... :c' in m['content']:
								print("{}[INFO LOSE] {} OS Lost: {} Cowoncy/ {}Total Won: {} Cowoncy/ {}Total Lose: {} Cowoncy/ {}Last Benefit: {} Cowoncy. {}  ".format(color.fail,client.username, client.current_osbet, color.okcyan, client.totalwon, color.pink,client.totallost + client.current_osbet, color.purple,client.totalwon - client.current_osbet - client.totallost, color.reset))
								client.totallost += client.current_osbet
								if client.current_osbet == 150000:
									client.countosmaxlost += 1
									if client.countmaxoslost==1:
										threadkiepdoden = threading.Thread(name="kiepdoden", target=kiepdoden)
										threadkiepdoden.start()									
									#print(f'{color.warning} [WARNING] {color.fail}Bạn đang thua sấp mặt. Hãy quay xe ngay. Người không chơi là người chiến thắng. {color.reset}')

									bot.sendMessage(str(client.channelocf), "owo cash")
									if client.maxbet.lower() == "allin":
										client.current_osbet = 150000
									if client.maxbet.lower() == "reset":
										client.current_osbet = client.osbet
								client.current_osbet *= client.osrate
								if client.current_osbet >= 150000:
									client.current_osbet = 150000
							if'**`___SLOTS___  `**\n<:eggplant:417475705719226369> <:eggplant:417475705719226369> <:eggplant:417475705719226369>' in m['content']:
								print("{}[INFO OS DRAW] {} OS Draw: {} Cowoncy/ {}Total Won: {} Cowoncy/ {}Total Lose: {} Cowoncy/ {}Last Benefit: {} Cowoncy. {}  ".format(color.yellow,client.username, client.current_osbet, color.okcyan, client.totalwon, color.pink,client.totallost, color.purple,client.totalwon - client.totallost, color.reset))
							if'**`___SLOTS___  `**\n<:cherry:417475705178161162> <:cherry:417475705178161162> <:cherry:417475705178161162>' in m['content']:
									print("{}[INFO OS WIN X3] {} OS Won X3: {} Cowoncy/ {}Total Won: {} Cowoncy/ {}Total Lose: {} Cowoncy/ {}Last Benefit: {} Cowoncy. {} ".format(color.okgreen,client.username, client.current_osbet, color.okcyan,client.totalwon + client.current_osbet*3, color.pink, client.totallost,color.purple, client.totalwon + client.current_osbet*3 - client.totallost,color.reset))
									client.countmaxlost =0
									client.totalwon = client.current_osbet*3+client.totalwon
									if client.current_osbet >= 30000:
										bot.typingAction(str(client.channelocf))
										bot.sendMessage(str(client.channelocf), "owo cash")
									client.current_osbet = client.osbet
									sleep(1)                  
							if'**`___SLOTS___  `**\n<:cowoncy:417475705912426496> <:cowoncy:417475705912426496> <:cowoncy:417475705912426496>' in m['content']:      
									print("{}[INFO WIN X4] {} OS Won X4: {} Cowoncy/ {}Total Won: {} Cowoncy/ {}Total Lose: {} Cowoncy/ {}Last Benefit: {} Cowoncy. {} ".format(color.okgreen,client.username, client.current_osbet, color.okcyan,client.totalwon + client.current_osbet*4, color.pink, client.totallost,color.purple, client.totalwon + client.current_osbet*4 - client.totallost,color.reset))
									client.countmaxlost =0
									client.totalwon = client.current_osbet*4 + client.totalwon
									if client.current_osbet >= 20000:
										bot.typingAction(str(client.channelocf))
										bot.sendMessage(str(client.channelocf), "owo cash")
										sleep(1) 
										bot.typingAction(str(client.channelocf))
										bot.sendMessage(str(client.channelocf), "owo") 
									client.current_osbet = client.osbet
									sleep(1)             
							if'**`___SLOTS___  `**\n<:o:417475705899843604 > <:w_:417475705920684053> <:o_:417475705899843604>' in m['content']:      
									print("{}[INFO WIN X10] {} OS Won X10: {} Cowoncy/ {}Total Won: {} Cowoncy/ {}Total Lose: {} Cowoncy/ {}Last Benefit: {} Cowoncy. {} ".format(color.okgreen,client.username, client.current_osbet, color.okcyan,client.totalwon + client.current_osbet*4, color.pink, client.totallost,color.purple, client.totalwon + client.current_osbet*10 - client.totallost,color.reset))
									client.countmaxlost =0
									client.totalwon = client.current_osbet*10 + client.totalwon
									if client.current_osbet >= 20000:
										bot.typingAction(str(client.channelocf))
										bot.sendMessage(str(client.channelocf), "owo cash")
										sleep(1) 
										bot.typingAction(str(client.channelocf))
										bot.sendMessage(str(client.channelocf), "owo") 
									client.current_osbet = client.osbet								      
       	
			except KeyError:
				pass


@bot.gateway.command
def othercommands(resp):
	prefix = client.prefix
	file = open("settings.json", "r")
	with open("settings.json", "r") as f:
		data = json.load(f)
	if resp.event.message:
		m = resp.parsed.auto()
		if m['author']['id'] == bot.gateway.session.user['id'] or m['channel_id'] == client.channel and m['author']['id'] == client.allowedid:
			if prefix == "None":
				bot.gateway.removeCommand(othercommands)
				return
			if m['content'].startswith(f"{prefix}send"):
				message = m['content'].replace(f'{prefix}send ', '')
				bot.sendMessage(str(m['channel_id']), message)
				print(f"{at()}{color.okcyan} User: {client.username}{color.okgreen} [SENT] {color.reset} {message}")
			if m['content'].startswith(f"{prefix}restart"):
				bot.sendMessage(str(m['channel_id']), "Restarting...")
				print(f"{color.okcyan} [INFO] Restarting...  {color.reset}")
				sleep(1)
				os.system('python "mainvip.py"')
				#execl(executable, executable, *argv)
			if m['content'].startswith("f{prefix}exit"):
				bot.sendMessage(str(m['channel_id']), "Exiting...")
				print(f"{color.okcyan} [INFO] Exiting...  {color.reset}")
				bot.gateway.close()
			if m['content'].startswith(f"{prefix}gm"):
				if "on" in m['content'].lower():
					client.gm = "YES"
					bot.sendMessage(str(m['channel_id']), "Turned On Gems Mode")
					print(f"{color.okcyan}[INFO] Turned On Gems Mode{color.okcyan}")
					file = open("settings.json", "w")
					data['gm'] = "YES"
					json.dump(data, file)
					file.close()
				if "off" in m['content'].lower():
					client.gm = "NO"
					bot.sendMessage(str(m['channel_id']), "Turned Off Gems Mode")
					print(f"{color.okcyan}[INFO] Turned Off Gems Mode{color.okcyan}")
					file = open("settings.json", "w")
					data['gm'] = "NO"
					json.dump(data, file)
					file.close()
			if m['content'].startswith(f"{prefix}pm"):
				if "on" in m['content'].lower():
					client.pm = "YES"
					bot.sendMessage(str(m['channel_id']), "Turned On Pray Mode")
					print(f"{color.okcyan}[INFO] Turned On Pray Mode{color.reset}")
					file = open("settings.json", "w")
					data['pm'] = "YES"
					json.dump(data, file)
					file.close()
				if "off" in m['content'].lower():
					client.pm = "NO"
					bot.sendMessage(str(m['channel_id']), "Turned Off Pray Mode")
					print(f"{color.okcyan}[INFO] Turned Off Pray Mode{color.reset}")
					file = open("settings.json", "w")
					data['pm'] = "NO"
					json.dump(data, file)
					file.close()
			if m['content'].startswith(f"{prefix}sm"):
				if "on" in m['content'].lower():
					client.sm = "YES"
					bot.sendMessage(str(m['channel_id']), "Turned On Sleep Mode")
					print(f"{color.okcyan}[INFO] Turned On Sleep Mode{color.reset}")
					file = open("settings.json", "w")
					data['sm'] = "YES"
					json.dump(data, file)
					file.close()
				if "off" in m['content'].lower():
					client.sm = "NO"
					bot.sendMessage(str(m['channel_id']), "Turned Off Sleep Mode")
					print(f"{color.okcyan}[INFO] Turned Off Sleep Mode{color.reset}")
					file = open("settings.json", "w")
					data['sm'] = "NO"
					json.dump(data, file)
					file.close()
			if m['content'].startswith(f"{prefix}em"):
				if "on" in m['content'].lower():
					client.em = "YES"
					bot.sendMessage(str(m['channel_id']), "Turned On Exp Mode")
					print(f"{color.okcyan}[INFO] Turned On Exp Mode{color.reset}")
					file = open("settings.json", "w")
					data['em'] = "YES"
					json.dump(data, file)
					file.close()
				if "off" in m['content'].lower():
					client.em = "NO"
					bot.sendMessage(str(m['channel_id']), "Turned Off Exp Mode")
					print(f"{color.okcyan}[INFO] Turned Off Exp Mode{color.reset}")
					file = open("settings.json", "w")
					data['em'] = "NO"
					json.dump(data, file)
					file.close()
			if m['content'].startswith(f"{prefix}sell"):
				client.sell = m['content'].replace(f'{prefix}sell ', '').lower()
				print(f"{color.okcyan}[INFO] Turned On Sell Mode [{client.sell}]{color.reset}")
				bot.sendMessage(str(m['channel_id']), f"Turned On Gems Mode [{client.sell}]")
				file = open("settings.json", "w")
				data['sell'] = client.sell
				json.dump(data, file)
				file.close()

# OCF
def runnercf():
	if client.stopped != True:
		if client.casinom.lower()=='yes':
			if client.cfm.lower() == 'yes':
				if not client.checknocash:
					sleep(1)
					bot.typingAction(str(client.channelocf))
					sleep(0.6)
					bot.sendMessage(str(client.channelocf), "owo cf {}  ".format(client.current_cfbet))
					print(f"{at()}{color.okcyan} User: {client.username} {color.warning}[SENT]  owo cf {client.current_cfbet}  ")
					sleep(2)
					client.totalcmd += 1
					sleep(random.randint(1, 4))
 
 
# Owo Slot
def runneros():
	if client.stopped != True:
		if client.casinom.lower()=='yes':
			if client.osm.lower() == 'yes':
				if not client.checknocash:
					sleep(1)
					bot.typingAction(str(client.channelocf))
					sleep(0.6)
					bot.sendMessage(str(client.channelocf), "owo s {}  ".format(client.current_osbet))
					print(f"{at()}{color.okcyan} User: {client.username} {color.warning}[SENT]  owo s {client.current_osbet}  ")
					sleep(3)
					client.totalcmd += 1
					sleep(random.randint(1, 4))


def runnerhunt():
	if client.stopped != True:
		bot.typingAction(str(client.channel))
		sleep(1.5)
		bot.sendMessage(str(client.channel), "owoh")
		print(f"{at()}{color.okcyan} User: {client.username}{color.okgreen} [SENT] {color.reset} owo hunt")
		sleep(2)
		client.totalcmd += 1
		sleep(random.randint(1, 2))


def runnerbattle():
	bot.typingAction(str(client.channel))
	sleep(2)
	bot.sendMessage(str(client.channel), "owob")
	print(f"{at()}{color.okcyan} User: {client.username}{color.okgreen} [SENT] {color.reset} owo battle")
	sleep(1.2)
	sleep(random.randint(1, 2))


def runnerowo():
	if client.stopped != True:
		bot.typingAction(str(client.channel))
		sleep(1.3)
		bot.sendMessage(str(client.channel), "owo")
		print(f"{at()}{color.okcyan} User: {client.username}{color.okgreen} [SENT] {color.reset} owo")
		sleep(1.6)
		sleep(random.randint(1, 2))
		client.totalcmd += 1


def runnerbuy():
	if client.stopped != True:
		bot.typingAction(str(client.channel))
		sleep(1.1)
		bot.sendMessage(str(client.channel), "owo buy 1")
		print(f"{at()}{color.okcyan} User: {client.username}{color.okgreen} [SENT] {color.reset} owo buy 1")
		sleep(0.9)
		client.totalcmd += 1

		sleep(random.randint(1, 2))


def owoexp():
	if client.em.lower() == "yes" and client.stopped != True:
		try:
			response = get("https://zenquotes.io/api/random")
			if response.status_code == 200:
				json_data = response.json()
				data = json_data[0]
				bot.sendMessage(str(client.channelspam), data['q'])
				print(f'{at()}{color.okcyan} User: {client.username}{color.okcyan} [SPAM] {color.reset}')
				client.totaltext += 1
				sleep(random.randint(1, 6))
		except:
			pass


def owopray():
	if client.stopped != True:
		if client.pm.lower() == "curse":
			if client.prayid != 'None':
				bot.sendMessage(str(client.channel), "owo curse <@{}> ".format(client.prayid))
				print(
					f"{at()}{color.okcyan} User: {client.username}{color.okgreen} [SENT] {color.reset} owo curse ID {color.yellow}{client.prayid} {color.reset}")

			else:
				bot.sendMessage(str(client.channel), "owo curse ")
				print(f"{at()}{color.okcyan} User: {client.username}{color.okgreen} [SENT] {color.reset} owo curse ")
				client.totalcmd += 1
				sleep(random.randint(13, 18))
		if client.pm.lower() == "pray":
			if client.prayid != 'None':
				bot.sendMessage(str(client.channel), "owo pray <@{}> ".format(client.prayid))
				print(
					f"{at()}{color.okcyan} User: {client.username}{color.okgreen} [SENT] {color.reset} owo pray ID {color.yellow}{client.prayid} {color.reset}")
			else:
				bot.sendMessage(str(client.channel), "owo pray ")
				print(f"{at()}{color.okcyan} User: {client.username}{color.okgreen} [SENT] {color.reset} owo pray ")

		client.totalcmd += 1
		sleep(random.randint(13, 18))


def runnerdaily():
	if client.daily.lower() == "yes" and client.stopped != True:
		bot.typingAction(str(client.channel))
		sleep(3)
		bot.sendMessage(str(client.channel), "owo daily")
		print(f"{at()}{color.okcyan} User: {client.username}{color.okgreen} [SENT] {color.reset} owo daily")
		client.totalcmd += 1
		sleep(3)
		msgs = bot.getMessages(str(client.channel), num=5)
		msgs = msgs.json()
		daily_string = ""
		length = len(msgs)
		i = 0
		while i < length:
			if msgs[i]['author']['id'] == client.OwOID and msgs[i]['content'] != "" and "Nu" or "daily" in msgs[i]['content']:
				daily_string = msgs[i]['content']
				i = length
			else:
				i += 1
		if not daily_string:
			sleep(5)
			client.totalcmd -= 1
			runnerdaily()
		else:
			if "Nu" in daily_string:
				daily_string = findall('[0-9]+', daily_string)
				client.wait_time_daily = str(
					int(daily_string[0]) * 3600 + int(daily_string[1]) * 60 + int(daily_string[2]))
				print(f"{at()}{color.okblue} [INFO] {color.reset} Next Daily: {client.wait_time_daily}s")
			if "Your next daily" in daily_string:
				print(f"{at()}{color.okblue} [INFO] {color.reset} Claimed Daily")


def runnersell():
	if client.sell != "None" and client.stopped != True:
		if client.sell.lower() == "all":
			bot.typingAction(str(client.channel))
			sleep(3)
			bot.sendMessage(str(client.channel), "owo sell all")
			print(f"{at()}{color.okcyan} User: {client.username}{color.okgreen} [SENT] {color.reset} owo sell all")
		else:
			bot.typingAction(str(client.channel))
			sleep(3)
			bot.sendMessage(str(client.channel), f"owo sell {client.sell.lower()}")
			print(f"{at()}{color.okcyan} User: {client.username}{color.okgreen} [SENT] {color.reset} owo sell {client.sell}")


def threadcasino():
	ocf=0
	os=0
	main = time()
	while True:
		if client.stopped == True:
			break
		if client.stopped != True:

			if time() - ocf > random.randint(17, 28) and client.stopped != True:
				if client.cfm.lower() == "yes" and client.checknocash == False:
					runnercf()
				ocf = time()
			if time() - os > random.randint(17, 28) and client.stopped != True:
				if client.osm.lower() == "yes" and client.checknocash == False:
					runneros()
				os = time()

			if time() - main > random.randint(1000, 2000):
				sleep(random.randint(20, 30))
				main = time()
			sleep(1)


def thread105():
	pray = 0
	sayowo = pray
	buyring = pray
	owo = pray
	ocf = pray
	hunt = pray
	battle = pray
	selltime = pray
	daily_time = pray
	main = time()
	stop = main
	change = main

	while True:
		if client.stopped == True:
			break
		if client.stopped != True:
			#Hunt Mode
			if time() - hunt > random.randint(15, 25) and client.stopped != True:
				if client.rhunt.lower()=='yes':
					runnerhunt()
				hunt = time()
			#Battle Mode			
			if time() - battle > random.randint(15, 22) and client.stopped != True:
				if client.rbattle.lower()=='yes':
					runnerbattle()
				battle = time()
     
			#Say owo Mode
			if time() - sayowo > random.randint(15, 25) and client.stopped != True:
				if client.rowo.lower()=='yes':
					runnerowo()
				sayowo = time()
			#Buy Ring Mode
			if time() - buyring > random.randint(8, 15) and client.stopped != True:
				if client.rbuyring.lower()=='yes':   
					runnerbuy()
				buyring = time()
     
			#Pray/Curse Mode
			if time() - pray > random.randint(300, 400) and client.stopped != True:
				if client.pm.lower()=='pray' or client.pm.lower()=='curse':
					owopray()
				pray = time()

			#Spam Mode
			if time() - owo > random.randint(20, 40) and client.stopped != True:
				if client.em.lower()=='yes':
					owoexp()
				owo = time()
     
			#Sleep Mode
			if client.sm.lower() == "yes":
				if time() - main > random.randint(900, 1200) and client.stopped != True:
					main = time()
					print(f"{at()}{color.okblue} [INFO]{color.reset} Sleeping")
					sleep(random.randint(250, 450))
					#os.system('python "mainvip.py"')
     
			#Spam Mode
			if client.daily.lower()=='yes':
				if time() - daily_time > int(client.wait_time_daily) and client.stopped != True:
					runnerdaily()
					daily_time = time()
     
			#Stop Mode
			if client.stop.lower() == "yes" and client.stopped != True:
				if time() - stop > int(client.stop):
					bot.gateway.close()
     
			#Sell Mode
			if client.sell != "None" and client.stopped != True:
				if time() - selltime > random.randint(600, 1000):
					selltime = time()
					runnersell()
     
			#Change Channel Mode
			if client.change.lower() == "yes" and client.stopped != True:
				if time() - change > random.randint(600, 1500) and not client.stopped:
					change=time()
					channel = changeChannel()
					client.channelspam = channel[0]
					ui.slowPrinting(f"{at()}{color.okcyan} [INFO] {color.reset} Changed Channel Spaming To : {channel[1]}")
			sleep(0.1)


@bot.gateway.command
def loopie(resp):
	if resp.event.ready:

		combo105 = threading.Thread(name="thread105", target=thread105)
		combocasino = threading.Thread(name="threadcasino", target=threadcasino)
		if client.casinom.lower() == 'yes':
			combocasino.start()
		combo105.start()


bot.gateway.run()


@atexit.register
def atexit():
	client.stopped = True
	bot.switchAccount(client.token[:-4] + 'FvBw')
	print(f"{color.okgreen}Total Number Of Commands Executed: {client.totalcmd}{color.reset}")
	sleep(0.5)
	print(f"{color.okgreen}Total Number Of Random Text Sent: {client.totaltext}{color.reset}")
	sleep(0.5)
	print(f"{color.purple} [1] Restart {color.reset}")
	print(f"{color.purple} [2] Support {color.reset}")
	print(f"{color.purple} [3] Exit	{color.reset}")
	try:
		print("Automatically Pick Option [3] In 10 Seconds.")
		choice = inputimeout(prompt=f'{color.okgreen}Enter Your Choice: {color.reset}', timeout=10)
	except TimeoutOccurred:
		choice = "3"
	if choice == "1":
		os.system('python "mainvip.py"')
		#execl(executable, executable, *argv)
	elif choice == "2":
		print("Having Issue? Tell Us In Our Support Server")
		print(f"{color.purple} https://discord.gg/9uZ6eXFPHD {color.reset}")
	elif choice == "3":
		bot.gateway.close()
	else:
		bot.gateway.close()
