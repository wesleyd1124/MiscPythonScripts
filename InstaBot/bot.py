from instapy import InstaPy
from instapy import comment_util
from instapy import like_util
from instapy import unfollow_util
from instapy import commenters_util
import random
import time
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

loginInfo = config['LOGIN']
botConfig = config['BOT']
users = botConfig['BottingUsers'].split(",")
postLink = botConfig['PostLink']

password = loginInfo['Password']
username = loginInfo['Username']
bot = InstaPy(username=username, password=password)
bot.login()
blacklist = {'enabled':'false'}
likeClusters = 4
while True:
	for user in users:
		try:
			links = like_util.get_links_for_username(bot.browser, user, 4, bot.logger)
			for i, link in enumerate(links):
				likers = commenters_util.users_liked(bot.browser, link, amount=100)
				bot.browser.get(postLink)
				for _ in range(likeClusters):
					time.sleep(6)
					random.shuffle(likers)
					comment = ""
					for y in range(5):
						comment = comment + "@" + likers[y] + " "
					comment_util.comment_image(bot.browser, username, [comment], blacklist, bot.logger, bot.logfolder)
		except:
			pass
