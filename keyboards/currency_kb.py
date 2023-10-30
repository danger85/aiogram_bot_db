from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

#def markup_currency(c_f: str, data: dict, row_name: list): #создание таблицы со значениями курса валют в виде кнопок.
def currency_kb(c_f:str, data:dict )->InlineKeyboardMarkup:
  row_name = ["Валюта", "операция", "до 200", "<10.000", ">10.000"]
  print(f"\tCame from {c_f} in markup_currency, markup layout")
  print(data)
  currency_table: list [InlineKeyboardButton] = []
  currency_table_kb = InlineKeyboardBuilder()
  for i,row_value in enumerate(row_name):
    currency_table_kb.add(InlineKeyboardButton(text=str(i), callback_data="{\"Kb\":\"cur\",\"V\":\"v\",\"CF\":\"cur\"}"), # 0 колонка ['Валюта','операция',  'до 200', '<10.000', '>10.000'])
                          InlineKeyboardButton(text=str(data[i][0]), callback_data="{\"Kb\":\"" + 'mul$' + "\",\"V\":\"" + str(data[i][0]) + "\",\"CF\":\"cur\"}"),# 1 колонка ['$','покупка', '63.80', ...]
                          InlineKeyboardButton(text=str(data[i][1]), callback_data="{\"Kb\":\"" + 'div$' + "\",\"V\":\"" + str(data[i][1]) + "\",\"CF\":\"cur\"}"),  # 2 колонка ['$','продажа', '65.30',...]
                          InlineKeyboardButton(text=str(data[i][2]), callback_data="{\"Kb\":\"" + 'mul€' + "\",\"V\":\"" + str(data[i][2]) + "\",\"CF\":\"cur\"}"),# 3 колонка ['€','покупка', '64.50', ...]
                          InlineKeyboardButton(text=str(data[i][3]), callback_data="{\"Kb\":\"" + 'div€' + "\",\"V\":\"" + str(data[i][3]) + "\",\"CF\":\"cur\"}")) # 4  колонка ['€','продажа', '66.00',...]
  currency_table_kb.add(InlineKeyboardButton(text="Выйти из меню", callback_data="{\"Kb\":\"param\",\"V\":\"leave\",\"CF\":\"parameters\"}"))
  #currency_table_kb.row(*currency_table)
  return currency_table_kb.as_markup()