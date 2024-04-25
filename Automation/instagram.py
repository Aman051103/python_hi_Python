from instabot import Bot
bot= Bot() # creating instance of Bot
bot.login(username="", password="") # to login into your account
bot.upload_photo("abc.jpg", caption="")  # to post a picture
bot.follow("username") # to follow someone
bot.send_message("message",['reciever_1','reciever_n']) # to send message to someone
follower= bot.get_followers() # to get following list of current account
followers= bot.get_user_followers("username") # to get following list of someone specific
for i in followers:
    print(bot.get_user_info(i))
# bot.unfollow_everyone() #to unfollow everyone
