import os
import telegram
import random

bot = telegram.Bot(token=os.environ["TELEGRAM_TOKEN"])

# list of backpack images and random text
backpack = ["https://media1.tenor.com/images/3862340576b167181f07a120e11a400b/tenor.gif?itemid=8722064",
    "Mmm... yeah... the pack for the back.",
    "I like turtles.",
    "I like pie.",
    "Das ist ein rucksack auf Deutsch!",
    "Oh, and remember, next Friday is Swedish luggage day, so, you know, if you want to, go ahead and wear a bäckpäck."]

# list of diabetus images
diabetus = ["https://media1.tenor.com/images/38b0f21d0e76dec2ff58d19e37fcc716/tenor.gif?itemid=4484736",
    "https://1funny.com/wp-content/uploads/2009/07/diabeetus-cat.jpg",
    "http://rs367.pbsrc.com/albums/oo112/Aim_fire/sdgfasfdgd.jpg~c200",
    "https://c1.staticflickr.com/3/2254/2334517660_c5a9522dbd.jpg"]

# list of catfacts
catfacts = ["(1) Unlike dogs, cats do not have a sweet tooth. Scientists believe this is due to a mutation in a key taste receptor.",
    "(2) When a cat chases its prey, it keeps its head level. Dogs and humans bob their heads up and down.",
    "(3) The technical term for a cat’s hairball is a “bezoar”.",
    "(4) A group of cats is called a “clowder”.",
    "(5) A cat can’t climb head first down a tree because every claw on a cat’s paw points the same way. To get down from a tree, a cat must back down.",
    "(6) Cats make about 100 different sounds. Dogs make only about 10.",
    "(7) Every year, nearly four million cats are eaten in Asia.",
    "(8) There are more than 500 million domestic cats in the world, with approximately 40 recognized breeds.",
    "(9) Approximately 24 cat skins can make a coat.",
    "(10) While it is commonly thought that the ancient Egyptians were the first to domesticate cats, the oldest known pet cat was recently found in a 9,500-year-old grave on the Mediterranean island of Cyprus. This grave predates early Egyptian art depicting cats by 4,000 years or more.",
    "(11) During the time of the Spanish Inquisition, Pope Innocent VIII condemned cats as evil and thousands of cats were burned. Unfortunately, the widespread killing of cats led to an explosion of the rat population, which exacerbated the effects of the Black Death.",
    "(12) During the Middle Ages, cats were associated with withcraft, and on St. John’s Day, people all over Europe would stuff them into sacks and toss the cats into bonfires. On holy days, people celebrated by tossing cats from church towers.",
    "(13) The first cat in space was a French cat named Felicette (a.k.a. “Astrocat”) In 1963, France blasted the cat into outer space. Electrodes implanted in her brains sent neurological signals back to Earth. She survived the trip.",
    "(14) The group of words associated with cat (catt, cath, chat, katze) stem from the Latin catus, meaning domestic cat, as opposed to feles, or wild cat.",
    "(15) The term “puss” is the root of the principal word for “cat” in the Romanian term pisica and the root of secondary words in Lithuanian (puz) and Low German puus. Some scholars suggest that “puss” could be imitative of the hissing sound used to get a cat’s attention. As a slang word for the female pudenda, it could be associated with the connotation of a cat being soft, warm, and fuzzy.",
    "(16) Approximately 40,000 people are bitten by cats in the U.S. annually.",
    "(17) Cats are North America’s most popular pets: there are 73 million cats compared to 63 million dogs. Over 30% of households in North America own a cat.",
    "(18) According to Hebrew legend, Noah prayed to God for help protecting all the food he stored on the ark from being eaten by rats. In reply, God made the lion sneeze, and out popped a cat.",
    "(19) A cat’s hearing is better than a dog’s. And a cat can hear high-frequency sounds up to two octaves higher than a human.",
    "(20) A cat can travel at a top speed of approximately 31 mph (49 km) over a short distance."]

def webhook(request):
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        chat_id = update.effective_message.chat.id
        messagetext = update.effective_message.text
        try:
            if "backpack" in messagetext.lower():
                replytext = random.choice(backpack)
                bot.sendMessage(chat_id=chat_id, text=replytext)
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
