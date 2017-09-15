import requests
import OlxParser
import time

token = '385017512:AAHrISO0n6qaEcYbZq9utTdT8PqWLZw3Y7A'
URL ='https://api.telegram.org/bot'\
     + token\
     + '/'
triger = False
timer = 0

def get_updates():
    url = URL + 'getupdates'
    return requests.get(url).json()

def get_message():
    data = get_updates()
    chat_id = data['result'][-1]['message']['chat']['id']
    message_text = data['result'][-1]['message']['text']
    message = {'chat_id': chat_id,
               'text': message_text}
    return message

def get_update_id():
    data = get_updates()
    update_id = data['result'][-1]['update_id']
    return update_id


def send_message(chat_id, text = 'jast a second...'):
    url = URL + \
          'sendmessage?chat_id=' \
          + str(chat_id) \
          + '&text=' \
          + text
    print (url)
    requests.get(url)



if __name__ == "__main__":
    # def message_creator(heders):
    first_update_id = get_update_id()

    while True:
        if timer == 600:
            new_heders = OlxParser.parser()
            if new_heders != None:
                for i in range(len(new_heders)):
                    message = '    ' \
                              + new_heders[i]['text']\
                              + '   ' \
                              + new_heders[i]['link']
                    send_message(get_message()['chat_id'], message)
                    print (message)
            timer = 0

        print(get_update_id(), timer)
        timer += 1

        time.sleep(1)

        if first_update_id != get_update_id():
            if get_message()['text'] == '/help':
                send_message(get_message()['chat_id'], 'take instruction')
                first_update_id = get_update_id()