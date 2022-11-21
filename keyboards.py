from aiogram.utils.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, \
    InlineKeyboardButton, ReplyKeyboardMarkup, \
    KeyboardButton, WebAppInfo 


web_app = WebAppInfo(url="https://mikhailtte.github.io/")

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Site", web_app=web_app)]
    ],
    resize_keyboard=True
)

cb = CallbackData('btn', 'action')
key = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton('Pay', callback_data='btn:buy')]]
)
