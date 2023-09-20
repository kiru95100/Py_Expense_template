from PyInquirer import prompt
user_questions = [

{
        "type":"input",
        "name":"name",
        "message":"Quel est votre nom et prénom? ",
    }
]

def add_user():
    # This function should create a new user, asking for its name
    infos = prompt(user_questions)
    return