import telebot
import random
bot = telebot.TeleBot("1840551118:AAHXwiqiIPMaDK89jtyy0tJPTHP3QEZbrJQ")

"""<--Основная клавиатура-->"""
mainboard = telebot.types.InlineKeyboardMarkup(row_width=2)
but_rand = telebot.types.InlineKeyboardButton(text="Угадай число", callback_data="ug_c")
but_bj = telebot.types.InlineKeyboardButton(text="Blackjack", callback_data="bj")
but_bon = telebot.types.InlineKeyboardButton(text="Кости", callback_data="skelet")
but_word = telebot.types.InlineKeyboardButton(text="Угадай слово", callback_data="ug_s")
mainboard.add(but_bj, but_rand, but_word, but_bon)

"""<--Клавиатура для "Угадай число"-->"""
mar_rand = telebot.types.InlineKeyboardMarkup(row_width=3)
f_mar = telebot.types.InlineKeyboardButton(text="1", callback_data='rand_1')
s_mar = telebot.types.InlineKeyboardButton(text="2", callback_data='rand_2')
t_mar = telebot.types.InlineKeyboardButton(text="3", callback_data='rand_3')
fr_mar = telebot.types.InlineKeyboardButton(text="4", callback_data='rand_4')
ff_mar = telebot.types.InlineKeyboardButton(text="5", callback_data='rand_5')
sx_mar = telebot.types.InlineKeyboardButton(text="6", callback_data='rand_6')
sn_mar = telebot.types.InlineKeyboardButton(text="7", callback_data='rand_7')
e_mar = telebot.types.InlineKeyboardButton(text="8", callback_data='rand_8')
n_mar = telebot.types.InlineKeyboardButton(text="9", callback_data='rand_9')
mar_rand.add(f_mar, s_mar, t_mar, fr_mar, ff_mar, sx_mar, sn_mar, e_mar, n_mar)

"""<--Переходы-->"""
again = telebot.types.InlineKeyboardMarkup(row_width=2)
ag_1 = telebot.types.InlineKeyboardButton(text="Конечно", callback_data="ag_1")
ag_2 = telebot.types.InlineKeyboardButton(text="Выберу другую игру", callback_data="ag_2")
again.add(ag_1, ag_2)

"""<-Угадай число-->"""
def number(call,answer):
    random_number = str(random.randint(1,9))
    if answer == random_number:
        media=telebot.types.InputMediaPhoto(open("image/cool.png","rb"),caption="Молоток!\nЕщё раз?")
        bot.edit_message_media(media=media,chat_id=call.message.chat.id,message_id=call.message.message_id,reply_markup=again)
        bot.answer_callback_query( call.id, text="" )
    else:
        media=telebot.types.InputMediaPhoto(open("image/notcool.png","rb"),caption="Не повезло =(\nЕщё раз?")
        bot.edit_message_media(media=media,chat_id=call.message.chat.id,message_id=call.message.message_id,reply_markup=again)
        bot.answer_callback_query( call.id, text="" )


@bot.message_handler(commands=["start"])
def start_message(commands):
    bot.send_photo(commands.chat.id,open("image/hi_bot.jpg","rb"),"Привет! Меня зовут Фёдор! Я - игровой бот!\nХочу предложить сыграть тебе в следующие игры:\nУгадай число\nBlackJack\nКости\nУгадай слово",reply_markup=mainboard)

@bot.callback_query_handler(func=lambda call: True)
def check_call(call):
    if call.data == "ug_c":
        media = telebot.types.InputMediaPhoto( open( "image/rand_bot.png", "rb" ), caption="Я загадал число! Попробуй его отгадать!" )
        bot.edit_message_media(media=media,chat_id=call.message.chat.id,message_id=call.message.message_id, reply_markup=mar_rand )
        bot.answer_callback_query( call.id, text="" )
    if call.data == "bj":
        bot.answer_callback_query( call.id, text="Эта игра будет доступна в следующих версиях бота" )
    if call.data == "skelet":
        bot.answer_callback_query( call.id, text="Эта игра будет доступна в следующих версиях бота " )
    if call.data == "ug_s":
        bot.answer_callback_query( call.id, text="Эта игра будет доступна в следующих версиях бота" )

    if call.data.split("_")[0]=="rand":
        number(call, call.data.split("_")[1])
    if call.data == "ag_1":
        media = telebot.types.InputMediaPhoto(open( "image/rand_bot.png", "rb"), "\nЯ загадал число! Попробуй его отгадать!")
        bot.edit_message_media(media=media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=mar_rand)
    if call.data == "ag_2":
        media = telebot.types.InputMediaPhoto(open("image/choise.png", "rb"), "\nВыбери игру" )
        bot.edit_message_media( media=media, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=mainboard )



bot.infinity_polling()
