# telebot был выбран тк он более оптимален по безопасности, надежности и отзывам сообщества
import telebot
import config.config as cfg

from controller.main import main_controller
from commands.GetHelp import getHelp

print(f"token=[{cfg.TOKEN}] \nTeleBot starting\n")

bot = telebot.TeleBot(cfg.TOKEN, parse_mode=None)



# обработка команд
# сейчас обрабатываются всего две команды:
# /start & /help

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message): #в message.text можно прочесть какая команда была дана
	
  if(message.text == "/help"):
    text = getHelp()
    bot.reply_to(message, text)
    
  else:
    bot.reply_to(message, F"{cfg.greeting}")



"""
	тут перехватываются все сообщения
	можно написать в папке контроллеры фу-цию
	для обработки сообщения...
	само сообщение находиться в переменной message
   его передовать как аргумент для ф-ции
   и возвращать ответ
   это нужно чтобы не писать тут простыни из фу-ций
   и логически их упорядочить
"""

@bot.message_handler(func=lambda m: True)
def echo_all(message):

  main_controller(bot, message)
	# print(F"message = {message}")






# for dev... for prod recomend webhooks
bot.polling()



""" пример тела 'message' 

message = {
  'content_type': 'text',
  'id': 11,
  'message_id': 11,
  'from_user': {
    'id': 1393115815,
    'is_bot': False,
    'first_name': 'Daedalus',
    'username':
    'daedalus_73',
    'last_name': None,
    'language_code': 'en',
    'can_join_groups': None,
    'can_read_all_group_messages': None,
    'supports_inline_queries': None
  },
  'date': 1632043428,
  'chat': {
    'id': 1393115815,
    'type': 'private',
    'title': None,
    'username': 'daedalus_73',
    'first_name': 'Daedalus',
    'last_name': None,
    'photo': None,
    'bio': None,
    'description': None,
    'invite_link': None,
    'pinned_message': None,
    'permissions': None,
    'slow_mode_delay': None,
    'message_auto_delete_time': None,
    'sticker_set_name': None,
    'can_set_sticker_set': None,
    'linked_chat_id': None,
    'location': None
  },
  'sender_chat': None,
  'forward_from': None,
  'forward_from_chat': None,
  'forward_from_message_id': None,
  'forward_signature': None,
  'forward_sender_name': None,
  'forward_date': None,
  'reply_to_message': None,
  'via_bot': None,
  'edit_date': None,
  'media_group_id': None,
  'author_signature': None,
  'text': 'asda',
  'entities': None,
  'caption_entities': None,
  'audio': None,
  'document': None,
  'photo': None,
  'sticker': None,
  'video': None,
  'video_note': None,
  'voice': None,
  'caption': None,
  'contact': None,
  'location': None,
  'venue': None,
  'animation': None,
  'dice': None,
  'new_chat_member': None,
  'new_chat_members': None,
  'left_chat_member': None,
  'new_chat_title': None,
  'new_chat_photo': None,
  'delete_chat_photo': None,
  'group_chat_created': None,
  'supergroup_chat_created': None,
  'channel_chat_created': None,
  'migrate_to_chat_id': None,
  'migrate_from_chat_id': None,
  'pinned_message': None,
  'invoice': None,
  'successful_payment': None,
  'connected_website': None,
  'reply_markup': None,
  'json': {
    'message_id': 11,
    'from': {
      'id': 1393115815,
      'is_bot': False,
      'first_name': 'Daedalus',
      'username': 'daedalus_73',
      'language_code': 'en'
    },
    'chat': {
      'id': 1393115815,
      'first_name': 'Daedalus',
      'username': 'daedalus_73',
      'type': 'private'
    },
    'date': 1632043428,
    'text': 'asda'
  }
}

"""