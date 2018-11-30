import os
import telegram
import random

bot = telegram.Bot(token=os.environ["TELEGRAM_TOKEN"])

diabetus = ["https://media1.tenor.com/images/38b0f21d0e76dec2ff58d19e37fcc716/tenor.gif?itemid=4484736",
        "https://1funny.com/wp-content/uploads/2009/07/diabeetus-cat.jpg",
        "http://rs367.pbsrc.com/albums/oo112/Aim_fire/sdgfasfdgd.jpg~c200"]

def webhook(request):
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        chat_id = update.message.chat.id
        messagetext = update.message.text
        # Reply with the same message
        # bot.sendMessage(chat_id=chat_id, text=update.message.text)
        if "backpack" in messagetext.lower():
            bot.sendMessage(chat_id=chat_id, text="https://media1.tenor.com/images/3862340576b167181f07a120e11a400b/tenor.gif?itemid=8722064")
        if "chika" in messagetext.lower() or "chikalicious" in messagetext.lower():
            replytext = random.choice(diabetus)
            bot.sendMessage(chat_id=chat_id, text=replytext)
    return "ok"
