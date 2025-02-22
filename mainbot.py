import os
import telebot

BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot  = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands = ['start' , 'hello'])
def send_wellcom(message):
    bot.reply_to(message , "سلام خوبین چطورین")