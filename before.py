#
#
#
from instabot import Bot

bot = Bot()

bot.login(username="", password="")

followers = bot.get_user_followers("moisty_meme_bros")

i=0
for user in followers[20:]:
    username = bot.get_username_from_user_id(user)
    print("Attempting to follow:", username)
    if bot.follow(username):
        i += 1
        print("Followed! -", username)
    else :
        print("Not Followed! - ", username)
    if i > 20:
        break