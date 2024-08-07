import telebot
bot = telebot.TeleBot('7366730929:AAFbRJjozeIYGK9XBTNqA5Gt7snjcU8a3ak')
@bot.message_handler(content_types=['text', 'audio', 'photo', 'voice', 'video', 'animation'], func=lambda message: True)
def handle_text_audio_photo(message):
    chat_name = message.from_user.first_name
    content = message.text
    print(chat_name, ":", content)
    if message.content_type == 'text':
        bot.reply_to(message, "text")
        pass
    if message.content_type == 'animation':
        bot.reply_to(message, "gif")
        pass
    if message.content_type == 'video':
        bot.reply_to(message, "vi")
        pass
    elif message.content_type == 'audio':
        bot.reply_to(message, "au")
        pass
    elif message.content_type == 'photo':
        bot.reply_to(message, "ph")
        pass
    elif message.content_type == 'voice':
        bot.reply_to(message, "vo")
        pass
bot.infinity_polling()
