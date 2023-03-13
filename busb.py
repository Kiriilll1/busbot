import sqlite3
import asyncio
import logging
from aiogram import Bot, Dispatcher, types, executor
from bust import user_task
from bottkn import bot
from sqlbus import db_create_user
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.web_app_info import WebAppInfo


logging.basicConfig(level=logging.INFO)

dp=Dispatcher(bot)


#celery уведомления для тг 
#butefuelsoup


@dp.message_handler(text=['Cоздать напоминание⏰'])
async def send_buss(message:types.Message):
    ###user_task()
    keyboard=InlineKeyboardMarkup()
    button1=InlineKeyboardButton("50", callback_data="bus_50")
    button2=InlineKeyboardButton("2", callback_data="2")
    keyboard.add(button1,button2)
    await bot.send_message(message.chat.id,'Выберете автобус',reply_markup=keyboard)

@dp.callback_query_handler(text="bus_50")
async def bus_50(callback: types.CallbackQuery):
    user_task()
    keyboard=InlineKeyboardMarkup()
    button1=InlineKeyboardButton("Синтез",callback_data='x')
    button2=InlineKeyboardButton("Спортивный комплекс Турбинка",callback_data='x')
    button3=InlineKeyboardButton("Хлебокомбинат №1",callback_data='x')
    button4=InlineKeyboardButton("Орлова",callback_data='x')
    button5=InlineKeyboardButton("Стадион Центральный",callback_data='x')
    keyboard.add(button1, button2, button3, button4, button5)
    await callback.message.answer("Выберете остановку",reply_markup=keyboard)



@dp.message_handler(commands=['start'])
async def send_welcom(message:types.Message):
    await bot.send_message(message.chat.id, "Привет! Это бот для поиска нужного Вам автобуса")
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_geo = types.KeyboardButton(text="Отправить местоположение📍", request_location=True)
    task_user=types.KeyboardButton(text='Cоздать напоминание⏰')
    keyboard.add(button_geo,task_user)
    await bot.send_message(message.chat.id,"для этого нужно отправить геопозицию", reply_markup=keyboard)


@dp.message_handler(content_types=["location"])
async def location(message):
    if message.location is not None:
        lat=message.location.latitude
        lon=message.location.longitude
        print("latitude: %s; longitude: %s" % (message.location.latitude, message.location.longitude))
        await bot.send_location(message.chat.id, lat, lon)
        await message.answer("Перейти для поиска автобуса",
        reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(text="Карта",
        web_app=WebAppInfo(url="https://2gis.ru/kurgan"))))
        user_id=message.from_user.id
        latitude=message.location.latitude 
        longitude=message.location.longitude
        db_create_user(user_id=user_id,latitude=lat,longitude=lon)


    """webKeyboard=types.ReplyKeyboardMarkup(row_width=1)
    webAppTest=types.WebAppInfo("http://localhost:3000/")
    one_butt=types.KeyboardButton(text="Test", web_app=webAppTest)
    keyboard.add(one_butt)
    return keyboard"""



#@dp.message_handler(commands=['location'])
#async def send_location(message:types.Location):
#    await bot.send_message(message.chat,'это геопозиция')

@dp.message_handler(content_types=["text"])
async def handle_text(message):
    await bot.send_message(message.chat.id, 'Это не геопозиция!')
    print(message.chat.id,":" ,message.text)




async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

input()
