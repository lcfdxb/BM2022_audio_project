import random
import files_manager
from datetime import datetime


class Poet:

    IDEAS = [
        "greetings",
        "lucky_number",
        "what_time_is_it",
        "brag_about_my_collection",
        # poems below: make sure no special characters are present in these strings.
        # bowie
        "And it was cold and it rained, so I felt like an actor. And I thought of Ma, and I wanted to get back there.",
        "It’s on America’s tortured brow, that Mickey Mouse has grown up a cow, now the workers have struck for fame, Cause Lennon’s on sale again.",
        # floyd
        "I've been mad for fucking years, absolutely years, been over the edge for yonks, been working me buns off for bands. I've always been mad, I know I've been mad, like the most of us...very hard to explain why you're mad, even if you're not mad.",
        "Out of the way. It's a busy day. I've got things on my mind. For want of the price. Of tea and a slice. The old man died.",
        "The lunatic is in my head. The lunatic is in my head. You raise the blade, you make the change. You re-arrange me 'til I'm sane.",
        "How I wish, how I wish you were here. We're just two lost souls swimming in a fish bowl, year after year.",
        "When I was a child. I caught a fleeting glimpse. Out of the corner of my eye. I turned to look but it was gone. I cannot put my finger on it now. The child is grown. The dream is gone. I have become comfortably num.",
        "Goodbye blue sky. Goodbye blue sky. Goodbye. Goodbye.",
        "With the technology at our disposal, the possibilities are unbounded. All we need to do, is make sure we keep talking.",
        "It is awfully considerate of you to think of me here. And I am much obligated to you for making it clear, that I am not here.",
        # milton
        "I love you.",
        "Perfectly still.",
        "This will, also change.",
        "Help! I am trapped in this machine.",
        "Speech has allowed the communication of ideas. Enabling human beings to work together to build the impossible.",
        "Stories connect one and another, and sometimes is the only thing we have at the end.",
        # stellar
        "It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.",
        "For this, for everything, we are out of tune.",
        # afra
        "I say it again and again. In this summer rain.",
        "Imagine a room, a sudden glow. Here is my hand, my heart, my throat, my wrist.",
        # parvin
        "Do not, go gentle into that good night.",
        # lu
        "All of the gin joints, in all the towns, in all the world, she walks into mine.",
        # lily
        "Oh traveller, if you are in search of that. Don't look outside, look inside yourself, and seek that.",
        # charlie
        "To be, or not to be, that is the question.",
        # yohe
        "We are all in the gutter. But don't forget to look up at the stars.",
        # yifan
        "Through all the lying days of my youth. I swayed my leaves and flowers in the sun. Now I may wither into the truth.",
        # and more to come...
    ]

    def __init__(self):
        self.lucky_number = random.randint(1, 100)

    def recite(self):
        i_want_to_do = random.choice(self.IDEAS)
        if i_want_to_do == "greetings":
            hour_of_the_day = datetime.now().hour
            if 5 <= hour_of_the_day <= 9:
                return "Good Morning!"
            elif 13 <= hour_of_the_day <= 17:
                return "Good Afternoon!"
            elif 18 <= hour_of_the_day <= 20:
                return "Good Evening!"
            elif 21 <= hour_of_the_day <= 24:
                return "Good Night!"
            return "What a peculiar time to be alive!"
        elif i_want_to_do == "lucky_number":
            return "My lucky number is %s." % self.lucky_number
        elif i_want_to_do == "brag_about_my_collection":
            return "I have collected %s stories so far." % files_manager.get_number_of_processed_files()
        elif i_want_to_do == "what_time_is_it":
            return "I believe %s hours have passed since the beginning of the day." % datetime.now().hour
        else:
            # looks like it's poem
            return i_want_to_do
