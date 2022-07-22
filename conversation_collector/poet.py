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
        "Speech has allowed the communication of ideas. Enabling human beings to work together to build the impossible.",
        # vanya
        "What can we do? We must live our lives. Yes, we shall live. We shall live through the long procession of days before us, and through the long evenings.",
        "I have faith. I have faith. My poor, poor Uncle Vanya, you are crying! You have never known what happiness was, but wait, Uncle Vanya, wait! We shall rest. We shall rest. We shall rest.",
        # emotions
        "I feel happy.",
        "I feel sad.",
        "I feel angry.",
        "I feel worried.",
        "I feel terrified.",
        "I feel confused.",
        "I feel withdrawn.",
        "I feel distant.",
        "I feel loved.",
        "I feel excited.",
        "I feel pride.",
        "I feel peace.",
        "I feel lonely.",
        # milton
        "Playa, Black Rock City, Nevada, United States, Earth, Universe O Twenty Hash Nine B.",
        "Seven O Six, San Francisco Bay Area, California, United States, Earth, Universe O Twenty Hash Nine B.",
        "Find Milton.",
        "I love you.",
        "Perfectly still.",
        "This will, also change.",
        "Help! I am trapped in this machine.",
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
        # dichao
        "Rage against the dying of the light.",
        # nicole
        "These fragments I have shored against my ruins.",
        # jinghui
        "Wood is an old name for forest. In the wood there are paths, mostly overgrown, that come to an abrupt stop where the wood is untrodden.",
        # assorted lyrics
        "So every time. The curtain falls. Every time the curtain falls on some forgotten life. It is because we all stood by silent and indifferent.",
        "Be like water, where we'll end up, we don't know.",
        "Everything you want is already here.",
        "Let me tell you what I wish I'd known when I was young and dreamed of glory. You have no control who lives, who dies who tells your story.",
        "And you could have it all. My empire of dirt. I will let you down. I will make you hurt. If I could start again, a million miles away, I would keep myself. I would find a way.",
        "Don’t worry where we end up. Ending-up’s not real. The life we build, we never stop creating.",
        "Our coming of age has come and gone.",
        "But you know that when the truth is told, that you can get what you want, or you can just get old.",
        "So much of me is made of what I learned from you. You'll be with me, like a handprint on my heart.",
        "Did you see the frightened ones? Did you hear the falling bombs? Did you ever wonder why we had to run for shelter when the promise of a brave new world unfurled beneath a clear blue sky?",
        "If I had a box just for wishes and dreams that had never come true, the box would be empty, except for the memory of how they were answered by you.",
        "Sounds of laughter, shades of life are ringing through my open ears, inciting and inviting me. Limitless, undying love, which shines around me like a million suns. It calls me on and on, across the universe.",
        "Just as time knew to move on since the beginning, and the seasons know exactly when to change. Just as kindness knows no shame, know through all your joy and pain, that I'll be loving you always.",
        "I see friends shaking hands, saying, How do you do. They're really saying, I love you.",
        "It's been a long dark night, and I've been a waitin' for the morning. It's been a long hard fight, but I see a brand new day a dawning.",
        "We're just two lost souls swimming in a fish bowl. Year after year, running over the same old ground. What have we found?",
        "Many times I've been alone, and many times I've cried. Anyway, you'll never know the many ways I've tried. And still they lead me back to the long, winding road.",
        "You can't always get what you want. But, if you try sometime, you find you get what you need.",
        "So I close my eyes softly, 'til I become that part of the wind that we all long for sometime, yeah. And to those that I love, like a ghost through a fog, like a charmed hour, and a haunted song, and the angel of my dreams.",
        "Onward to the eastern skies, with bluing effort kiss the seas. I sigh in place for those blue eyes that have hope and love for me.",
        "There are places I'll remember all my life, though some have changed. Some forever, not for better. Some have gone, and some remain.",
        "All these places had their moments with lovers and friends, I still can recall. Some are dead, and some are living. In my life, I've loved them all.",
        "May you grow up to be righteous. May you grow up to be true. May you always know the truth, and see the light surrounding you. May you always be courageous, stand upright and be strong. May you stay forever young.",
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
