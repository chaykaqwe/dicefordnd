from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Подбросить монету🪙')],
                                     [KeyboardButton(text='d4')],
                                     [KeyboardButton(text='d6')],
                                     [KeyboardButton(text='d8')],
                                     [KeyboardButton(text='d12')],
                                     [KeyboardButton(text='d20')],
                                     [KeyboardButton(text='d100')],
                                     [KeyboardButton(text='свое значение')]
                                     ], resize_keyboard=True)