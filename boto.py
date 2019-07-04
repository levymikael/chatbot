"""
This is the template server side for ChatBot
"""

from bottle import route, run, template, static_file, request
import json


@route('/', method='GET')
def index():

    return template("chatbot.html")

# this is the line
@route("/chat", method='POST')
def chat():
    user_input = request.POST.get('msg')
    print(user_input)
    input_list = user_input.split()
    print(input_list)
    swear_words_list = ["arse","ass","asshole",",bastard","bitch","bollocks","child-fucker","Christ on a bike","Christ on a cracker","crap",\
                        "cunt","damn","frigger","fuck","goddamn","godsdamn","hell","holy shit","horseshit""Jesus Christ","Jesus fuck","Jesus H. Christ",\
                        "Jesus Harold Christ,","Jesus wept","Jesus, Mary and Joseph","Judas Priest","motherfucker","nigga","nigger","prick","shit",\
                        "shit ass","shitass","slut","son of a bitch","son of a motherless goat","son of a whore","sweet Jesus","twat"]
    for index, word in enumerate(input_list):
        print(input_list[index])
        if input_list[index] == "love":
            return_message = "Let's spread love together"
            gif_name = "inlove"
        elif input_list[index] == "animal" or "puppy" or "dog"
        else:
            return_message = "Sorry, I didn't understand what you just typed"
            gif_name = "confused"


    return json.dumps({"animation": gif_name, "msg": return_message})


@route("/test", method='POST')
def chat():
    user_message = request.POST.get('msg')
    return json.dumps({"animation": "inlove", "msg": user_message})


@route('/js/<filename:re:.*\.js>', method='GET')
def javascripts(filename):

    return static_file(filename, root='js')


@route('/css/<filename:re:.*\.css>', method='GET')
def stylesheets(filename):
    return static_file(filename, root='css')


@route('/images/<filename:re:.*\.(jpg|png|gif|ico)>', method='GET')
def images(filename):
    return static_file(filename, root='images')


def main():
    run(host='localhost', port=7000)

if __name__ == '__main__':
    main()
