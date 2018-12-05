import os
import telegram
import random

bot = telegram.Bot(token=os.environ["TELEGRAM_TOKEN"])

# list of diabetus images
diabetus = ["https://media1.tenor.com/images/38b0f21d0e76dec2ff58d19e37fcc716/tenor.gif?itemid=4484736",
    "https://1funny.com/wp-content/uploads/2009/07/diabeetus-cat.jpg",
    "http://rs367.pbsrc.com/albums/oo112/Aim_fire/sdgfasfdgd.jpg~c200",
    "https://c1.staticflickr.com/3/2254/2334517660_c5a9522dbd.jpg"]

#list of catfacts
catfacts = ["1. Unlike dogs, cats do not have a sweet tooth. Scientists believe this is due to a mutation in a key taste receptor.",
    "2. When a cat chases its prey, it keeps its head level. Dogs and humans bob their heads up and down.",
    "3. The technical term for a cat’s hairball is a “bezoar”.",
    "4. A group of cats is called a “clowder”.",
    "5. A cat can’t climb head first down a tree because every claw on a cat’s paw points the same way. To get down from a tree, a cat must back down.",
    "6. Cats make about 100 different sounds. Dogs make only about 10.",
    "7. Every year, nearly four million cats are eaten in Asia.",
    "8. There are more than 500 million domestic cats in the world, with approximately 40 recognized breeds.",
    "9. Approximately 24 cat skins can make a coat.",
    "10. While it is commonly thought that the ancient Egyptians were the first to domesticate cats, the oldest known pet cat was recently found in a 9,500-year-old grave on the Mediterranean island of Cyprus. This grave predates early Egyptian art depicting cats by 4,000 years or more."]

def webhook(request):
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        chat_id = update.effective_message.chat.id
        messagetext = update.effective_message.text
        try:
            if "backpack" in messagetext.lower():
                bot.sendMessage(chat_id=chat_id, text="https://media1.tenor.com/images/3862340576b167181f07a120e11a400b/tenor.gif?itemid=8722064")
        except AttributeError:
            pass
        try:
            if "chika" in messagetext.lower() or "chikalicious" in messagetext.lower():
                replytext = random.choice(diabetus)
                bot.sendMessage(chat_id=chat_id, text=replytext)
        except AttributeError:
            pass
        try:
            if "catfact" in messagetext.lower():
                replytext = random.choice(catfacts)
                bot.sendMessage(chat_id=chat_id, text=replytext)
        except AttributeError:
            pass
    return "ok"
