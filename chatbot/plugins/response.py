import requests
user = input("Enter your username: ")
while True:
    message = input (user+": ")
    r = requests.get('https://some-random-api.ml/chatbot?message='+message)
    response_json  = r.json()
    bot_reply = response_json['response']
    print('Chatbot:',bot_reply)
