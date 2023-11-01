from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
import sqlite3

def m_up_l_of_t(c_f: str, lh: int)->InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    print(f"\tCame from {c_f} in l_of_t, markup layout")
    conn = sqlite3.connect("book_db.db", check_same_thread=False, isolation_level=None)
    c = conn.cursor()
    dat = c.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
    tab_nam_l = sorted(list(zip(*dat))[0])
    kb_builder.row(*[InlineKeyboardButton(text=i, callback_data=str({"Kb":"l_o_t","V":i,"CF":c_f})) for i in tab_nam_l])
    return kb_builder.as_markup()