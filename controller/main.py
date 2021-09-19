from controller.GetDate import getDate


def main_controller(bot, message):

  if (message.text == 'getDate'):
    date = getDate()
    bot.send_message(message.chat.id, date)
  else:
    pass
    # bot.send_message(message.chat.id, 'not implemented')