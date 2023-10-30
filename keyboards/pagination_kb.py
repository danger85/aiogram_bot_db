from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon_ru import LEXICON_RU,LEXICON,LEXICON_COMMANDS


def create_pagination_keyboards(*buttons:str)->InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    kb_builder.row(*[InlineKeyboardButton(text=LEXICON[button] if button in LEXICON else button, callback_data=button) for button in buttons])
    return kb_builder.as_markup()
