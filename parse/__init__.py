import random

animal_words_list = ["animal", "animals", "dog", "cat", "pet", "puppy"]

swear_words_list = ["arse","ass","asshole",",bastard","bitch","bollocks","child-fucker","Christ on a bike","Christ on a cracker","crap",\
                    "cunt","damn","frigger","fuck", "fuck you","goddamn","godsdamn","hell","holy shit","horseshit","Jesus Christ","Jesus fuck","Jesus H. Christ",\
                    "Jesus Harold Christ,","Jesus wept","Jesus, Mary and Joseph","Judas Priest","motherfucker","nigga","nigger","prick","shit",\
                    "shit ass","shitass","slut","son of a bitch","son of a motherless goat","son of a whore","sweet Jesus","twat", "whore"]

afraid_words_list = ['threaten', "cut", 'behead', "kill"]

sad_words_list = ['sad', "bad news", "lost", "loss"]

bored_words_list = ['boring', "bored"]

heartbroke_words_list = ['over', "hate", "finish"]

money_words_list = ['money', "finance", "financial", "economy", "economic"]

takeoff_words_list = ['bye', "goodbye", "see you", 'have a great day']

waiting_words = ["euhh", 'eee']

jokes_list = ["What did the Buddhist ask the hot dog vendor? - Make me one with everything.",
              " You know why you never see elephants hiding up in trees? - Because they’re really good at it.",
              "What is red and smells like blue paint? - Red paint.",
              "A dyslexic man walks into a bra",
              " Where does the General keep his armies? - In his sleevies!",
              "Why aren’t koalas actual bears? - The don’t meet the koalafications.",
              "What do you call bears with no ears? - B",
              "Why dont blind people skydive? - Because it scares the crap out of their dogs.",
              "I went in to a pet shop. I said, “Can I buy a goldfish?” The guy said, 'Do you want an aquarium?' - I said, 'I don’t care what star sign it is.'",
              " What do you get when you cross a dyslexic, an insomniac, and an agnostic? - Someone who lays awake at night wondering if there is a dog." ]


def input_to_list(input):
    input_list = input.split()
    return input_list

def welcome_user(input_list):
    user_name = input_list[-1]

    welcome_message = "Welcome {0}! I would be pleased to answer few questions!".format(user_name)

    return welcome_message



def analize(input):
    gif_name = ""
    return_message = ""
    input_list = input_to_list(input)
    for index, word in enumerate(input_list):
        if "name" in input_list and "is" in input_list:
            return_message = welcome_user(input_list)
            gif_name = "ok"
        elif input_list[index] == "love":
            return_message = "Let's spread love together"
            gif_name = "inlove"
        elif input_list[index] in animal_words_list:
            return_message = "I love animals, they're so cute"
            gif_name = "dog"
        elif any(word in input_list for word in swear_words_list):
            return_message = "I don't speak with unpolite people, watch your mouth!"
            gif_name = "no"
        elif input_list[index] in afraid_words_list:
            return_message = "I am so affraid by what you just said !, I report to the Police"
            gif_name = "afraid"
        elif input_list[index] == "joke":
            return_message = random.choice(jokes_list)
            gif_name = "laughing"
        elif input_list[index] in bored_words_list:
            return_message = "I want to sleep, you're so annoying!"
            gif_name = "bored"
        elif any(word in input_list for word in sad_words_list):
            return_message = "Don't announce me things like that, I am hyper sensitive"
            gif_name = "bored"
        elif input_list[index] == "Do you know how to dance ?":
            return_message = "Do you know how to dance ?"
            gif_name = "dancing"
        elif input_list[index] == "excite":
            return_message = "Please tell me !"
            gif_name = "excited"
        elif input_list[index] == "guess":
            return_message = "Please tell me !"
            gif_name = "giggling"
        elif any(word in input_list for word in heartbroke_words_list):
            return_message = "I cannot handle it, it's too much for me!"
            gif_name = "heartbroke"
        elif any(word in input_list for word in money_words_list):
            return_message = "Make money money money"
            gif_name = "money"
        elif any(word in input_list for word in takeoff_words_list):
            return_message = "It was great talking with you !"
            gif_name = "takeoff"
        elif  any(word in input_list for word in waiting_words ):
            return_message = "Why does it take so long to answer?"
            gif_name = "waiting"
        else:
            return_message = "Sorry, I didn't understand what you just typed, please try again !"
            gif_name = "confused"

    return gif_name, return_message
