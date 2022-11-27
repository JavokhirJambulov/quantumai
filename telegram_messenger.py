# We used the telepot library to send messages via Telegram bot
import datetime
import telepot

bot = telepot.Bot('5781518019:AAFo3Q4haFUGHiGGHkl-uL0M85EVWY86Gss')


# Function to send images
def send_image(image):
    bot.sendPhoto(-805188285, photo=open(image, 'rb'), caption=datetime.datetime.now().strftime("%H:%M:%S"))
# Function to send message
def send_message(msg):
    bot.sendMessage(-805188285, msg)

# Function to send message with some text
def send_emotion_and_person_on_door(person_name, emotion):
    msg = 'An unknown person is on the front door.'
    if (person_name != 'Unknown'):
        msg = person_name + ' is on the front door ' + emotion + '.'
    send_message(msg)