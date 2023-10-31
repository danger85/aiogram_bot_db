from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

class CallBackParametrs:
  def __init__(self,keyborad,value,came_from):
    self.keyboard=keyborad
    self.value=value
    self.came_from=came_from

#def markup_currency(c_f: str, data: dict, row_name: list): #создание таблицы со значениями курса валют в виде кнопок.
def currency_kb(c_f:str, data:dict )->InlineKeyboardMarkup:
  row_name = ["Валюта", "операция", "до 300", "<10.000", ">10.000"]
  print(f"\tCame from {c_f} to ", __name__)
  print(data)
  #return_parametrs = CallBackParametrs()
  kb=["cur","mul$","div$","mul€","div€"]

  currency_table_kb = InlineKeyboardBuilder()
  currency_table_kb.row(*[InlineKeyboardButton(text=str(data[0][i]), callback_data=str({"Kb":kb[i],"V":str(data[0][i]),"CF":"cur"})) for i in range(5)])
  currency_table_kb.row(*[InlineKeyboardButton(text=str(data[1][i]), callback_data=str({"Kb":kb[i],"V":str(data[1][i]),"CF":"cur"})) for i in range(5)])
  currency_table_kb.row(*[InlineKeyboardButton(text=str(data[2][i]), callback_data=str({"Kb":kb[i],"V":str(data[2][i]),"CF":"cur"})) for i in range(5)])
  currency_table_kb.row(*[InlineKeyboardButton(text=str(data[3][i]), callback_data=str({"Kb":kb[i],"V":str(data[3][i]),"CF":"cur"})) for i in range(5)])
  currency_table_kb.row(*[InlineKeyboardButton(text=str(data[4][i]), callback_data=str({"Kb":kb[i],"V":str(data[4][i]),"CF":"cur"})) for i in range(5)])
  currency_table_kb.add(InlineKeyboardButton(text="Выйти из меню", callback_data=str({"Kb":"param","V":"leave","CF":"parameters"}))).adjust(5)
  return currency_table_kb.as_markup()