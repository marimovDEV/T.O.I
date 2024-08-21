from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder,ReplyKeyboardMarkup
from languages import languages

def phone_kb(lang,key):
    txt = languages[lang][key]
    phone_kb = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text=txt,request_contact=True)]
    ],
                                resize_keyboard=True,one_time_keyboard=True)
    return phone_kb


def are_you_sure(lang,key_1,key_2):
    txt_1 = languages[lang][key_1]
    txt_2 = languages[lang][key_2]
    are_you_sure = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text=txt_1),KeyboardButton(text=txt_2)]
    ],
                                    resize_keyboard=True, one_time_keyboard=True)
    return are_you_sure