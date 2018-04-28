from telebot import types

genres = ['аниме', 'биография', 'боевик', 'вестерн', 'военный',
          'детектив', 'детский',  'документальный', 'драма',
          'история', 'комедия', 'концерт', 'короткометражка',
          'криминал', 'мелодрама', 'музыка', 'мультфильм', 'мюзикл',
          'приключения', 'семейный', 'сериал', 'спорт',
          'триллер', 'ужасы', 'фантастика', 'фильм-нуар', 'фэнтези']

start_markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
start_markup_btn1 = types.KeyboardButton('/start')
start_markup.add(start_markup_btn1)

choice_buttons1 = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
choice_buttons1_btn1 = types.KeyboardButton('Запустить поиск')
choice_buttons1_btn2 = types.KeyboardButton('Добавить шаблон')
choice_buttons1_btn3 = types.KeyboardButton('Редактировать шаблон')
choice_buttons1.add(
					choice_buttons1_btn1,
					choice_buttons1_btn2,
					choice_buttons1_btn3,
					)

choice_buttons2 = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
choice_buttons2_btn1 = types.KeyboardButton('Еще')
choice_buttons2_btn2 = types.KeyboardButton('Завершить')
choice_buttons2.add(choice_buttons2_btn1, choice_buttons2_btn2)

correct_buttons = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
correct_buttons_btn1 = types.KeyboardButton('Добавить жанр')
correct_buttons_btn2 = types.KeyboardButton('Удалить жанр')
correct_buttons.add(correct_buttons_btn1, correct_buttons_btn2)

choice_genres = types.ReplyKeyboardMarkup(resize_keyboard=True)
choice_genres.add(*[types.KeyboardButton(item) for item in genres])
