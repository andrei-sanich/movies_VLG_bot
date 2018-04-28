import telebot
import config
import time
import logging

from get_info import get_info
from storer import Storer
import markups


global template
template = ''
bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def handle_start(message):

    if Storer('userdata.txt').check_user(str(message.chat.id)) is not None:
        msg = bot.send_message(
                                message.chat.id,
                                'Выбирайте',
                                reply_markup=markups.choice_buttons1
                              )
        bot.register_next_step_handler(msg, ask_run_or_template)
    else:
        Storer('userdata.txt').save_user(str(message.chat.id))
        msg = bot.send_message(message.chat.id, 'Введите название шаблона')
        bot.register_next_step_handler(msg, ask_template)
    return


def ask_template(message):

    global template
    template = message.text
    Storer('userdata.txt').add_template(str(message.chat.id), template)
    msg = bot.send_message(
                            message.chat.id, 'Добавьте жанры в шаблон',
                            reply_markup=markups.choice_genres
                          )
    bot.register_next_step_handler(msg, add_genres)
    return


def add_genres(message):        

    genre = message.text
    Storer('userdata.txt').add_genre(str(message.chat.id), template, genre)
    msg = bot.send_message(
                            message.chat.id,
                            'Выбирайте',
                            reply_markup=markups.choice_buttons2
                          )
    bot.register_next_step_handler(msg, add_genre_or_finish)
    return


def add_genre_or_finish(message):

    if message.text == 'Еще':
        msg = bot.send_message(
                                message.chat.id,
                                "Выбирайте жанр",
                                reply_markup=markups.choice_genres
                              )
        bot.register_next_step_handler(msg, add_genres)
    elif message.text == 'Завершить':
        msg = bot.send_message(
                                message.chat.id,
                                'Выбирайте',
                                reply_markup=markups.choice_buttons1
                              )
        bot.register_next_step_handler(msg, ask_run_or_template)
        return


def ask_run_or_template(message):
    
    if message.text == 'Запустить поиск':
        findMovies(str(message.chat.id))
    elif message.text == 'Добавить шаблон':
        msg = bot.send_message(message.chat.id, 'Введите название шаблона')
        bot.register_next_step_handler(msg, ask_template)
    elif message.text == 'Редактировать шаблон':
        msg = bot.send_message(
                                message.chat.id,
                                'Выбирайте',
                                reply_markup=markups.correct_buttons
                               )
        bot.register_next_step_handler(msg, correct_template)
    return


def correct_template(message):
    
    if message.text == 'Добавить жанр':
        msg = bot.send_message(
                                message.chat.id,
                                'Выбирайте',
                                reply_markup=markups.choice_genres
                              )
        bot.register_next_step_handler(msg, add_genres)        
    elif message.text == 'Удалить жанр':
        msg = bot.send_message(
                                message.chat.id,
                                'Введите жанр'
                               )
        bot.register_next_step_handler(msg, del_genre)
     

def del_genre(message):
   
    genre = message.text
    Storer('userdata.txt').del_genre(str(message.chat.id), template, genre)
    msg = bot.send_message(
                            message.chat.id,
                            'Выбирайте',
                            reply_markup=markups.choice_buttons2
                          )
    bot.register_next_step_handler(msg, del_genre_or_finish)
    return

def del_genre_or_finish(message):

    if message.text == 'Еще':
        msg = bot.send_message(
                                message.chat.id,
                                "Выбирайте жанр",
                                reply_markup=markups.choice_genres
                              )
        bot.register_next_step_handler(msg, del_genre)
    elif message.text == 'Завершить':
        msg = bot.send_message(
                                message.chat.id,
                                'Выбирайте',
                                reply_markup=markups.choice_buttons1
                              )
        bot.register_next_step_handler(msg, ask_run_or_template)
        return


def findMovies(userid):

    usersets = Storer('userdata.txt').get_usersets(str(userid))
    afisha = Storer('database.txt').get_data('afisha')
    afisha_movies = get_info(usersets, afisha)
    if afisha_movies:
        for movie in afisha_movies:
            bot.send_message(userid, movie)
    else:
        bot.send_message(userid, "Из текущего репертуара подходящих фильмов нет")
    bot.send_message(userid, "Обзор среди премьер текущего месяца: ")
    time.sleep(1)
    premieres = Storer('database.txt').get_data('premieres')
    premieres_movies = get_info(usersets, premieres)
    if premieres:
        for movie in premieres_movies:
            bot.send_message(userid, movie)
    else:
        bot.send_message(userid, "Увы, и среди премьер подходящих фильмов нет")
    bot.send_message(userid, 'Готово', reply_markup=markups.start_markup)
    return


if __name__ == '__main__':
    try:
        bot.polling(none_stop=True)

    except Exception as err:
        logging.error(err)
        time.sleep(5)
        print("Internet error!")