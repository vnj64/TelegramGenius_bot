import logging
from matplotlib import artist
import requests
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils.markdown import hide_link
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


API_TOKEN = '5611755208:AAEhMQAMR2lmGAS1uNH1AGkW0EUeoMoUfZA'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)

storage = MemoryStorage()

dp = Dispatcher(bot, storage=storage)


"""
This handler will be called when user sends `/start` or `/help` command
"""
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    kb = [
        [types.KeyboardButton(text='20 треков Scally')],
        [types.KeyboardButton(text='Топ 10 треков Genius')],
        [types.KeyboardButton(text='Бросить кубики')],
        [types.KeyboardButton(text='Любимый артист info')],
        [types.KeyboardButton(text='Секретная ссылка')],
        [types.KeyboardButton(text='Чарт артистов')],
        [types.KeyboardButton(text='Текст песни Scally')]

    ]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder='Пиши команду'
    )
    
    await message.answer('С чего начнем?', reply_markup=keyboard)
    await message.reply("Привет!\nДоступные команда:\n/milano_songs\n/chart_top10\n/dice\n/lovely_artist\n/hidden_link\n/artists_chart\n/lyrics")


# Хэндлер на команду /milano_songs
@dp.message_handler(text='20 треков Scally')
async def cmd_test1(message: types.Message):
    url = "https://genius-song-lyrics1.p.rapidapi.com/artists/2040265/songs"

    querystring = {"sort":"title","per_page":"20","page":"1"}

    headers = {
        "X-RapidAPI-Key": "c30a3e4eefmsh005fbb18a21016ap15e87cjsnac664dd22942",
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
@dp.message_handler(text='Топ 10 треков Genius')
async def cmd_test2(message: types.Message):
    url = "https://genius-song-lyrics1.p.rapidapi.com/songs/chart"

    querystring = {"time_period":"day","chart_genre":"all","per_page":"10","page":"1"}

    headers = {
        "X-RapidAPI-Key": "c30a3e4eefmsh005fbb18a21016ap15e87cjsnac664dd22942",
        "X-RapidAPI-Host": "genius-song-lyrics1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    jsonData = response.json()['response']

    await message.answer("Топ 10 чарт Genius")

    result = []
    
    for data in jsonData['chart_items']:
        result.append(data['item']['full_title'])
    await message.answer('\n'.join(result))


# Хэндлер на команду /dice
@dp.message_handler(text="Бросить кубики")
async def cmd_dice(message: types.Message):
    await message.answer("Если выпало 3 - ты проиграл")
    await message.answer_dice(emoji="🎲 ")



class Artist(StatesGroup):
    name = State()

# Хэндлер на команду /lovely_artist
@dp.message_handler(text='Любимый артист info')
async def my_lovely_artist(message: types.Message):
    await Artist.name.set()
    await message.reply("Введите любимого исполнителя ( Пошлая Молли ): ")


@dp.message_handler(state='*', commands='cancel')
@dp.message_handler(Text(equals='отмена', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    
    await state.finish()
    await message.reply('OK')


@dp.message_handler(state=Artist.name)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text


@dp.message_handler(state=Artist.name)
async def parse_lovely_artist(message: types.Message, state: FSMContext):
    await bot.send_message('OK')


# Хэндлер на команду /lyrics
@dp.message_handler(text='Текст песни Scally')
async def send_text(message: types.Message):
    url = "https://genius-song-lyrics1.p.rapidapi.com/songs/6329375/lyrics"

    headers = {
        "X-RapidAPI-Key": "c30a3e4eefmsh005fbb18a21016ap15e87cjsnac664dd22942",
        "X-RapidAPI-Host": "genius-song-lyrics1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    user_id = message.from_user.id
    jsonData = response.json()['response']
    double = jsonData['lyrics']
    bd = double
    result = bd['lyrics']['body']
    
    with open('lyrics.txt', 'w') as f:
        f.write(result['html'])
    f.close()

    await bot.send_document(user_id, open('lyrics.txt', 'rb'))


# Хэндлер на команду /hidden_link
@dp.message_handler(text='Секретная ссылка')
async def cmd_hidden_link(message: types.Message):
    await message.answer(
        f"{hide_link('https://telegra.ph/file/562a512448876923e28c3.png')}"
        f"Документация Telegram: *существует*\n"
        f"Пользователи: *не читают документацию*\n"
        f"Груша:"
    )


# Хэндлер на команду /artists_chart
@dp.message_handler(text='Чарт артистов')
async def artists_chart(message: types.Message):
    url = "https://genius-song-lyrics1.p.rapidapi.com/artists/chart"

    querystring = {"time_period":"day","per_page":"10","page":"1"}

    headers = {
        "X-RapidAPI-Key": "c30a3e4eefmsh005fbb18a21016ap15e87cjsnac664dd22942",
        "X-RapidAPI-Host": "genius-song-lyrics1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    jsonData = response.json()['response']
	
    result = []

    for data in jsonData['chart_items']:
        result.append(data['item']['name'])
    await message.answer("Топ 10 артистов по мнению Genius:\n ")
    await message.answer('\n'.join(result))


# Возвращает строку, которая не предусмотрена
@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)