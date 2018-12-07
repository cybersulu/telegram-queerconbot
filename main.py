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
# source https://www.factretriever.com/cat-facts
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
    "(20) A cat can travel at a top speed of approximately 31 mph (49 km) over a short distance.",
    "(21) A cat rubs against people not only to be affectionate but also to mark out its territory with scent glands around its face. The tail area and paws also carry the cat’s scent.",
    "(22) Researchers are unsure exactly how a cat purrs. Most veterinarians believe that a cat purrs by vibrating vocal folds deep in the throat. To do this, a muscle in the larynx opens and closes the air passage about 25 times per second.",
    "(23) When a family cat died in ancient Egypt, family members would mourn by shaving off their eyebrows. They also held elaborate funerals during which they drank wine and beat their breasts. The cat was embalmed with a sculpted wooden mask and the tiny mummy was placed in the family tomb or in a pet cemetery with tiny mummies of mice.",
    "(24) In 1888, more than 300,000 mummified cats were found an Egyptian cemetery. They were stripped of their wrappings and carted off to be used by farmers in England and the U.S. for fertilizer.",
    "(25) Most cats give birth to a litter of between one and nine kittens. The largest known litter ever produced was 19 kittens, of which 15 survived.",
    "(26) Smuggling a cat out of ancient Egypt was punishable by death. Phoenician traders eventually succeeded in smuggling felines, which they sold to rich people in Athens and other important cities.",
    "(27) The earliest ancestor of the modern cat lived about 30 million years ago. Scientists called it the Proailurus, which means “first cat” in Greek. The group of animals that pet cats belong to emerged around 12 million years ago.",
    "(28) The biggest wildcat today is the Siberian Tiger. It can be more than 12 feet (3.6 m) long (about the size of a small car) and weigh up to 700 pounds (317 kg).",
    "(29) A cat’s brain is biologically more similar to a human brain than it is to a dog’s. Both humans and cats have identical regions in their brains that are responsible for emotions.",
    "(30) Many Egyptians worshipped the goddess Bast, who had a woman’s body and a cat’s head.",
    "(31) Mohammed loved cats and reportedly his favorite cat, Muezza, was a tabby. Legend says that tabby cats have an “M” for Mohammed on top of their heads because Mohammad would often rest his hand on the cat’s head.",
    "(32) While many parts of Europe and North America consider the black cat a sign of bad luck, in Britain and Australia, black cats are considered lucky.",
    "(33) The most popular pedigreed cat is the Persian cat, followed by the Maine Coon cat and the Siamese cat.",
    "(34) The smallest pedigreed cat is a Singapura, which can weigh just 4 lbs (1.8 kg), or about five large cans of cat food. The largest pedigreed cats are Maine Coon cats, which can weigh 25 lbs (11.3 kg), or nearly twice as much as an average cat weighs.",
    "(35) Some cats have survived falls of over 65 feet (20 meters), due largely to their “righting reflex.” The eyes and balance organs in the inner ear tell it where it is in space so the cat can land on its feet. Even cats without a tail have this ability.",
    "(36) Some Siamese cats appear cross-eyed because the nerves from the left side of the brain go to mostly the right eye and the nerves from the right side of the brain go mostly to the left eye. This causes some double vision, which the cat tries to correct by “crossing” its eyes.",
    "(37) Researchers believe the word “tabby” comes from Attabiyah, a neighborhood in Baghdad, Iraq. Tabbies got their name because their striped coats resembled the famous wavy patterns in the silk produced in this city.",
    "(38) A cat can jump up to five times its own height in a single bound.",
    "(39) Cats hate the water because their fur does not insulate well when it’s wet. The Turkish Van, however, is one cat that likes swimming. Bred in central Asia, its coat has a unique texture that makes it water resistant.",
    "(40) The Egyptian Mau is probably the oldest breed of cat. In fact, the breed is so ancient that its name is the Egyptian word for “cat.”",
    "(41) The first commercially cloned pet was a cat named “Little Nicky”. He cost his owner $50,000, making him one of the most expensive cats ever.",
    "(42) A cat usually has about 12 whiskers on each side of its face.",
    "(43) A cat’s eyesight is both better and worse than humans. It is better because cats can see in much dimmer light and they have a wider peripheral view. It’s worse because they don’t see color as well as humans do. Scientists believe grass appears red to cats.",
    "(44) Spanish-Jewish folklore recounts that Adam’s first wife, Lilith, became a black vampire cat, sucking the blood from sleeping babies. This may be the root of the superstition that a cat will smother a sleeping baby or suck out the child’s breath.",
    "(45) Perhaps the most famous comic cat is the Cheshire Cat in Lewis Carroll’s Alice in Wonderland. With the ability to disappear, this mysterious character embodies the magic and sorcery historically associated with cats.",
    "(46) The smallest wildcat today is the Black-footed cat. The females are less than 20 inches (50 cm) long and can weigh as little as 2.5 lbs (1.2 kg).",
    "(47) On average, cats spend 2/3 of every day sleeping. That means a nine-year-old cat has been awake for only three years of its life.",
    "(48) In the original Italian version of Cinderella, the benevolent fairy godmother figure was a cat.",
    "(49) The little tufts of hair in a cat’s ear that help keep out dirt direct sounds into the ear, and insulate the ears are called “ear furnishings.”",
    "(50) The ability of a cat to find its way home is called “psi-traveling.” Experts think cats either use the angle of the sunlight to find their way or that cats have magnetized cells in their brains that act as compasses."]

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
