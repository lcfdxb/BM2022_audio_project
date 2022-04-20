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
        # milton
        "I love you.",
        "This will, also change.",
        "Help! I am trapped in this machine.",
        "Speech has allowed the communication of ideas. Enabling human beings to work together to build the impossible.",
        "With the technology at our disposal, the possibilities are unbounded. All we need to do, is make sure we keep talking.",
        "It is awfully considerate of you to think of me here. And I am much obligated to you for making it clear, that I am not here.",
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
