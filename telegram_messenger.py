import datetime
import telepot

bot = telepot.Bot('5781518019:AAFo3Q4haFUGHiGGHkl-uL0M85EVWY86Gss')

def send_person_on_door(person_name):
    msg = 'An unknown person is on the front door.'
    if (person_name != 'Unknown'):
        msg = person_name + ' is on the front door.'
    send_message(msg)

def send_image(image):
    #bot = telepot.Bot('5781518019:AAFo3Q4haFUGHiGGHkl-uL0M85EVWY86Gss')
    # here replace chat_id and test.jpg with real things
    bot.sendPhoto(-805188285, photo=open(image, 'rb'), caption=datetime.datetime.now().strftime("%H:%M:%S"))

def send_message(msg):
    bot.sendMessage(-805188285, msg)

def send_emotion_and_person_on_door(person_name, emotion):
    msg = 'An unknown person is on the front door.'
    if (person_name != 'Unknown'):
        msg = person_name + ' is on the front door ' + emotion + '.'
    send_message(msg)