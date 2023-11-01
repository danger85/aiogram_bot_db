from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from lexicon.lexicon_ru import LEXICON_DB

def markup_menu(came_from)->InlineKeyboardMarkup:
    print(f"\tCame from {came_from} to markup_menu, qty_out={qty_out}")
    # print("\t", messages_dict)
    db_navigation_builder = InlineKeyboardBuilder()

    db_navigation_builder.row(*[InlineKeyboardButton(text=LEXICON_DB[i], callback_data=str({"Kb":"menu","V":i,"CF":came_from})) for i in LEXICON_DB.keys()])
    return db_navigation_builder.as_markup()