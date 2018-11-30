import os
import telegram

bot = telegram.Bot(token=os.environ["TELEGRAM_TOKEN"])


def webhook(request):
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        chat_id = update.message.chat.id
        messagetext = update.message.text
        # Reply with the same message
        # bot.sendMessage(chat_id=chat_id, text=update.message.text)
        if messagetext.lower() == "backpack":
        	bot.sendMessage(chat_id=chat_id, text="https://media1.tenor.com/images/3862340576b167181f07a120e11a400b/tenor.gif?itemid=8722064")
        if messagetext.lower() == "chika" or messagetext.lower() == "chikalicious":
            bot.sendMessage(chat_id=chat_id, text="https://media1.tenor.com/images/38b0f21d0e76dec2ff58d19e37fcc716/tenor.gif?itemid=4484736")
    return "ok"
