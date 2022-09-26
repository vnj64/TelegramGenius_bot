import logging
import requests
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.types.reply_keyboard import KeyboardButton


API_TOKEN = '5611755208:AAEhMQAMR2lmGAS1uNH1AGkW0EUeoMoUfZA'
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text='Все треки Скалли Милано'),
            types.KeyboardButton(text='Топ-10 чарт Genius'),
            types.KeyboardButton(text='Выбрать своего любимого исполнителя')
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder='Мне не интересен ваш любимый исполнитель'
    )

    await message.answer('С чего начнем?', reply_markup=keyboard)

    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Привет!\nДоступные команда:\n/milano_songs\n/chart_top10\n/dice")


# Хэндлер на команду /milano_songs
@dp.message_handler(commands=["milano_songs"])
async def cmd_test1(message: types.Message):
    url = "https://genius-song-lyrics1.p.rapidapi.com/artists/2040265/songs"

    querystring = {"sort":"title","per_page":"20","page":"1"}

    headers = {
        "X-RapidAPI-Key": "d8a2b24394msh530522f623e5ebcp1dff13jsn3401538088fc",
        "X-RapidAPI-Host": "genius-song-lyrics1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    jsonData = response.json()['response']

    result = []

    await message.answer("Все последние 20 треков Скалли Милано!!")

    for data in jsonData['songs']:
        result.append('genius.com' + data['api_path'])
    await message.reply('\n'.join(result))
    



# Хэндлер на команду /charts
@dp.message_handler(commands=['chart_top10'])
async def cmd_test2(message: types.Message):
    url = "https://genius-song-lyrics1.p.rapidapi.com/songs/chart"

    querystring = {"time_period":"day","chart_genre":"all","per_page":"10","page":"1"}

    headers = {
        "X-RapidAPI-Key": "d8a2b24394msh530522f623e5ebcp1dff13jsn3401538088fc",
        "X-RapidAPI-Host": "genius-song-lyrics1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    jsonData = response.json()['response']

    await message.answer("Топ 10 чарт Genius")

    result = []
    
    for data in jsonData['chart_items']:
        result.append(data['item']['full_title'])
    await message.answer('\n'.join(result))


@dp.message_handler(Text(text="Все треки Скалли Милано"))
async def scally_tracks(message: types.Message):
    await message.answer("Хороший выбор! Введи /milano_songs")


@dp.message_handler(commands=["dice"])
async def cmd_dice(message: types.Message):
    await message.answer("Если выпало 3 - ты проиграл")
    await message.answer_dice(emoji="🎲 ")

@dp.message_handler(commands=['lovely_artist'])
async def my_lovely_artist(message: types.Message):
    await message.answer('Введите своего любимого исполнителя')

@dp.message_handler(commands=['artists_chart'])
async def artists_chart(message: types.Message):
    url = "https://genius-song-lyrics1.p.rapidapi.com/artists/chart"

    querystring = {"time_period":"day","per_page":"10","page":"1"}

    headers = {
        "X-RapidAPI-Key": "d8a2b24394msh530522f623e5ebcp1dff13jsn3401538088fc",
        "X-RapidAPI-Host": "genius-song-lyrics1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    jsonData = response.json()['response']
    for data in jsonData['chart_items']:
        print(data['item'])


@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)