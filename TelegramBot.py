import requests
import OlxParser

token = '385017512:AAHrISO0n6qaEcYbZq9utTdT8PqWLZw3Y7A'
URL ='https://api.telegram.org/bot' + token + '/'
new_heders = OlxParser.parser()




def get_updates():
    url = URL + 'getupdates'
    r = requests.get(url)
    return r.json()

def get_message():
    data = get_updates()
    chat_id = data['result'][-1]['message']['chat']['id']
    message_text = data['result'][-1]['message']['text']
    message = {'chat_id': chat_id,
               'text': message_text}
    return message

def send_message(chat_id, text = 'jast a second...'):
    url = URL + 'sendmessage?chat_id=' + str(chat_id) + '&text=' + text
    print (url)
    requests.get(url)


# def message_creator(heders):
if new_heders != None:
    for i in range(len(new_heders)):
        message = '    ' + new_heders[i]['text'] + '   ' + new_heders[i]['link']
        send_message(get_message()['chat_id'], message)
        print (message)

else:
    message = 'sorry, but I can`t find new position'
    send_message(get_message()['chat_id'], message)




