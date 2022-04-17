import random
import files_manager
from datetime import datetime


class Poet:

    IDEAS = [
        "lucky_number",
        "what_time_is_it",
        "brag_about_my_collection",
        # poems below: make sure no special characters are present in these strings.
        # milton
        "I love you.",
        "This will, also change.",
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
        # more to come...
    ]

    def __init__(self):
        self.lucky_number = random.randint(1, 100)

    def recite(self):
        i_want_to_do = random.choice(self.IDEAS)
        if i_want_to_do == "lucky_number":
            return "My lucky number is %s." % self.lucky_number
        elif i_want_to_do == "brag_about_my_collection":
            return "I have collected %s stories so far." % files_manager.get_number_of_processed_files()
        elif i_want_to_do == "what_time_is_it":
            return "I believe %s hours have passed since the beginning of the day." % datetime.now().hour
        else:
            # looks like it's poem
            return i_want_to_do
