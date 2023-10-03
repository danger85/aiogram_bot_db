import asyncio
from bs4 import BeautifulSoup
import requests
import logging
import json

from aiogram import Bot, Dispatcher, types #
from aiogram.filters.command import Command # обработка команд
from aiogram.enums.dice_emoji import DiceEmoji # кубики подбрасывать
from aiogram import F # для обработки нажатий клавиш
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData

import os #для token

#logging.basicConfig(level=logging.INFO)
bot = Bot (token='please fill inasdfdsfsadfasdf')
dp = Dispatcher()

class MyCallback(CallbackData, prefix="my"):
  keyboard: str
  data_value: str
  came_from: str

def markup_num(c_f: str, val: str): #формирование кнопок в виде циферок
  print(f"\tCame from {c_f} in markup_num, markup layout ")
  print(f"\tmessage is {val}, lh = {len(val)}")
  lh = len(val)
  m_up_num = InlineKeyboardBuilder()
  ikb = types.InlineKeyboardButton

  def _num_one_to_nine():# создание кнопок от 1 до 9
    m_up_num.add(types.InlineKeyboardButton(text="7", callback_data="{\"Kb\":\"num\",\"V\":\"7\",\"CF\":\"" + c_f + "\"}"),
                 types.InlineKeyboardButton(text="8", callback_data="{\"Kb\":\"num\",\"V\":\"8\",\"CF\":\"" + c_f + "\"}"),
                 types.InlineKeyboardButton(text="9", callback_data="{\"Kb\":\"num\",\"V\":\"9\",\"CF\":\"" + c_f + "\"}"),
                 types.InlineKeyboardButton(text="4", callback_data="{\"Kb\":\"num\",\"V\":\"4\",\"CF\":\"" + c_f + "\"}"),
                 types.InlineKeyboardButton(text="5", callback_data="{\"Kb\":\"num\",\"V\":\"5\",\"CF\":\"" + c_f + "\"}"),
                 types.InlineKeyboardButton(text="6", callback_data="{\"Kb\":\"num\",\"V\":\"6\",\"CF\":\"" + c_f + "\"}"),
                 types.InlineKeyboardButton(text="1", callback_data="{\"Kb\":\"num\",\"V\":\"1\",\"CF\":\"" + c_f + "\"}"),
                 types.InlineKeyboardButton(text="2", callback_data="{\"Kb\":\"num\",\"V\":\"2\",\"CF\":\"" + c_f + "\"}"),
                 types.InlineKeyboardButton(text="3", callback_data="{\"Kb\":\"num\",\"V\":\"3\",\"CF\":\"" + c_f + "\"}")
                )

  if c_f == "fill_table" and lh == 0 or val == "_":  # первая цифра дня
    InlineKeyboardBuilder().add(ikb(text="1", callback_data="{\"Kb\":\"num\",\"V\":\"1\",\"CF\":\"" + c_f + "\"}"),
                 ikb(text="2", callback_data="{\"Kb\":\"num\",\"V\":\"2\",\"CF\":\"" + c_f + "\"}"),
                 ikb(text="3", callback_data="{\"Kb\":\"num\",\"V\":\"3\",\"CF\":\"" + c_f + "\"}")
                )
    if val != 0:
      InlineKeyboardBuilder().add(ikb(text="0", callback_data="{\"Kb\":\"num\",\"V\":\"0\",\"CF\":\"" + c_f + "\"}"))

  if c_f == "fill_table" and lh == 1:  # вторая цифра дня
    if val == "3":  # а первой является ...
      InlineKeyboardBuilder().add(ikb(text="1", callback_data="{\"Kb\":\"num\",\"V\":\"1\",\"CF\":\"" + c_f + "\"}"))
      InlineKeyboardBuilder().add(ikb(text="0", callback_data="{\"Kb\":\"num\",\"V\":\"0\",\"CF\":\"" + c_f + "\"}"))
    if val == "0":
      _num_one_to_nine()
    if val in str(list(range(1, 3))):
      _num_one_to_nine()
      InlineKeyboardBuilder().add(ikb(text="0", callback_data="{\"Kb\":\"num\",\"V\":\"0\",\"CF\":\"" + c_f + "\"}"))

  if c_f == "fill_table" and lh == 3:  # первая цифра месяца
    InlineKeyboardBuilder().add(ikb(text="1", callback_data="{\"Kb\":\"num\",\"V\":\"1\",\"CF\":\"" + c_f + "\"}"))
    InlineKeyboardBuilder().add(ikb(text="0", callback_data="{\"Kb\":\"num\",\"V\":\"0\",\"CF\":\"" + c_f + "\"}"))

  if c_f == "fill_table" and lh == 4:  # вторая цифра месяца
    print(f"\t ({val[0:2]}, {type(val[0:2])}) , ({val[-1]},{type(val[-1])})")
    if val[0:2] == "31":
      if val[-1] == "0":
        InlineKeyboardBuilder().add(ikb(text="июля", callback_data="{\"Kb\":\"num\",\"V\":\"7\",\"CF\":\"" + c_f + "\"}"))
        InlineKeyboardBuilder().add(ikb(text="января", callback_data="{\"Kb\":\"num\",\"V\":\"1\",\"CF\":\"" + c_f + "\"}"),
                                  ikb(text="марта", callback_data="{\"Kb\":\"num\",\"V\":\"2\",\"CF\":\"" + c_f + "\"}"),
                                  ikb(text="мая", callback_data="{\"Kb\":\"num\",\"V\":\"3\",\"CF\":\"" + c_f + "\"}"))
      if val[-1] == "1":
        InlineKeyboardBuilder().add(ikb(text="декабря", callback_data="{\"Kb\":\"num\",\"V\":\"2\",\"CF\":\"" + c_f + "\"}"))
        InlineKeyboardBuilder().add(ikb(text="октября", callback_data="{\"Kb\":\"num\",\"V\":\"0\",\"CF\":\"" + c_f + "\"}"))
    else:
      if val[-1] == "0":
        _num_one_to_nine()
      if val[-1] == "1":
        InlineKeyboardBuilder().add(ikb(text="1", callback_data="{\"Kb\":\"num\",\"V\":\"1\",\"CF\":\"" + c_f + "\"}"),
                                 ikb(text="2", callback_data="{\"Kb\":\"num\",\"V\":\"2\",\"CF\":\"" + c_f + "\"}"))
        InlineKeyboardBuilder().add(ikb(text="0", callback_data="{\"Kb\":\"num\",\"V\":\"0\",\"CF\":\"" + c_f + "\"}"))

  if c_f == "fill_table" and lh in list(range(6, 10)):
    _num_one_to_nine()
    InlineKeyboardBuilder().add(ikb(text="0", callback_data="{\"Kb\":\"num\",\"V\":\"0\",\"CF\":\"" + c_f + "\"}"))

  if c_f == "fill_table" and lh <= 10:
    InlineKeyboardBuilder().add(ikb(text="Очистить", callback_data="{\"Kb\":\"num\",\"V\":\"cls\",\"CF\":\"fill_table\"}"))
    if lh in list(range(7, 11)):
      InlineKeyboardBuilder().add(ikb(text="↲ Ввод", callback_data="{\"Kb\":\"func_key\",\"V\":\"enter\",\"CF\":\"fill_table\"}"))

  if c_f == "delete":
    _num_one_to_nine()
    InlineKeyboardBuilder().add(ikb(text="Удалить id", callback_data="{\"Kb\":\"func_key\",\"V\":\"enter\",\"CF\":\"delete\"}"),
                 ikb(text="0", callback_data="{\"Kb\":\"num\",\"V\":\"0\",\"CF\":\"delete\"}"),
                 ikb(text="Выйти", callback_data="{\"Kb\":\"func_key\",\"V\":\"exit\",\"CF\":\"delete\"}")
                )

  if c_f == "mod_p" or c_f == "calc":
    _num_one_to_nine()
    m_up_num.add(types.InlineKeyboardButton(text="0", callback_data="{\"Kb\":\"num\",\"V\":\"0\",\"CF\":\"" + c_f + "\"}"))
    m_up_num.add(types.InlineKeyboardButton(text="Ввод.", callback_data="{\"Kb\":\"func_key\",\"V\":\"enter\",\"CF\":\"" + c_f + "\"}"))
  m_up_num.adjust(3)
  return m_up_num.as_markup()

def markup_currency(c_f: str, data: dict, row_name: list): #создание таблицы со значениями курса валют в виде кнопок.
  print(f"\tCame from {c_f} in markup_currency, markup layout")
  print(data)
  markup_cur = InlineKeyboardBuilder()
  for x, i in enumerate(row_name):
    markup_cur.add(types.InlineKeyboardButton(text=str(i), callback_data="{\"Kb\":\"cur\",\"V\":\"v\",\"CF\":\"cur\"}"),  # 0 колонка ['Валюта','операция',  'до 200', '<10.000', '>10.000']
                   types.InlineKeyboardButton(text=str(data[i][0]), callback_data="{\"Kb\":\"" + 'mul$' + "\",\"V\":\"" + str(data[i][0]) + "\",\"CF\":\"cur\"}"),# 1 колонка ['$','покупка', '63.80', ...]
                   types.InlineKeyboardButton(text=str(data[i][1]), callback_data="{\"Kb\":\"" + 'div$' + "\",\"V\":\"" + str(data[i][1]) + "\",\"CF\":\"cur\"}"),  # 2 колонка ['$','продажа', '65.30',...]
                   types.InlineKeyboardButton(text=str(data[i][2]), callback_data="{\"Kb\":\"" + 'mul€' + "\",\"V\":\"" + str(data[i][2]) + "\",\"CF\":\"cur\"}"), # 3 колонка ['€','покупка', '64.50', ...]
                   types.InlineKeyboardButton(text=str(data[i][3]), callback_data="{\"Kb\":\"" + 'div€' + "\",\"V\":\"" + str(data[i][3]) + "\",\"CF\":\"cur\"}")) # 4  колонка ['€','продажа', '66.00',...]
  markup_cur.add(types.InlineKeyboardButton(text="Выйти из меню", callback_data="{\"Kb\":\"param\",\"V\":\"leave\",\"CF\":\"parameters\"}"))
  markup_cur.adjust(5)
  return markup_cur.as_markup(resize_keyboard = True)

@dp.callback_query(F.data.contains("cur"))
async def calc(callback: types.CallbackQuery):# "{\"Kb\":\"cur\",\"V\":\"" + str(data[i][0]) + "\",\"CF\":\"cur\"}"
  print(f"Came from markup_currency to CALC function by callback,{callback.data} ",
        f"called by {str(json.loads(str(callback.data))['CF'])}",
        f"value is {str(json.loads(str(callback.data))['V'])}",
        f"action is {str(json.loads(str(callback.data))['Kb'])}"
       )
  global mul_div
  global exchange_k
  exchange_k = json.loads(str(callback.data))['V']
  mul_div = json.loads(str(callback.data))['Kb']
  if mul_div[:-1] == "div":
    await callback.message.answer(f"Введите сумму для внесения в кассу (₽), которую хотите обменять на {mul_div[-1]}",
                                  reply_markup=markup_num("calc", "0"))
  elif mul_div[:-1] == "mul":
    await callback.message.answer(f"Введите сумму для внесения в кассу ({mul_div[-1]}), которую хотите обменять на ₽",
                                  reply_markup=markup_num("calc", "0"))

@dp.callback_query(F.data.contains("num")) #обработка показа клавиатуры
async def callback_num(callback: types.CallbackQuery):
  print(f"in callback_num function, by Callback, called by: {json.loads(callback.data)}")
  #print(f"\tmessage text is {callback.message.text}, came from user {callback.message.from_user.id}")
  digit = json.loads(callback.data)["V"]

  if json.loads(callback.data)["CF"] == "delete":  # если пришли из удаления
    global id_to_delete
    if len(id_to_delete) > 0:
      if id_to_delete[0] == "_":
          id_to_delete = ""
    id_to_delete = id_to_delete + digit
    await dp.edit_message_text(id_to_delete, callback.message.chat.id, callback.message.message_id, reply_markup=markup_num("delete", "0"))

  if json.loads(callback.data)["CF"] == "fill_table":
    global get_date
    if digit.isdigit() and len(get_date) <= 10:
      if get_date[:1] == "_":
        get_date = ""
      get_date = get_date + digit
    if len(get_date) == 2 or len(get_date) == 5:
      get_date = get_date + "."
    if digit == "cls":
      get_date = "_"
    await bot.edit_message_text(get_date, call.message.chat.id, call.message.message_id, reply_markup=markup_num("fill_table", get_date))

  if str(json.loads(callback.data)["CF"]) == "mod_p" or str(json.loads(callback.data)["CF"]) == "calc":
    global qty_out_text
    qty_out_text = qty_out_text + str(digit)
    await callback.message.edit_text(qty_out_text, reply_markup=markup_num(str(json.loads(callback.data)["CF"]), qty_out_text))

@dp.callback_query(F.data.contains("func_key") & F.data.contains("enter") & F.data.contains("calc")) #пришли после нажатия ввода при вычислении денег
async def exchange_calc(call: types.CallbackQuery):
  print(f"in exchange_calc function, ClBkHr, called by {list(json.loads(call.data).values())}")
  print(f"\tmessage text is {call.message.text}, came from {call.message.from_user.id}")
  global messages_dict
  global exchange_k
  global qty_out_text
  global mul_div
  if mul_div[:-1] == "div":
    print(f"{qty_out_text}, {exchange_k}")
    await call.message.edit_text(f"При обмене {qty_out_text} ₽ , получите {float(qty_out_text) / float(exchange_k)} {mul_div[-1]}")
  else:
    await call.message.edit_text(f"При обмене {qty_out_text} {mul_div[-1]}, получите {float(qty_out_text) * float(exchange_k)} ₽")

@dp.message(Command("start"))
async def cmd_start(message:types.Message):
  await message.answer("Hello!")

@dp.message(Command("dice"))
async def cmd_dice(message: types.Message):
  await message.answer_dice(emoji="🎲")

@dp.message(Command("c"))
async def currency(message: types.Message):
    print(f"In currency function, called by command /c")
    #print(f"\tmessage text is {message.text}, came from {message.from_user.id}")
    global exchange_k
    global qty_out_text
    qty_out_text = ""
    exchange_k = 0
    #await bot.delete_message(message.chat.id, message.message_id)
    # print("in currency function. called by command. Message id = ", message.message_id)
    r = requests.get("https://blagodatka.ru/",timeout=10,verify=False)
    soup = BeautifulSoup(r.content, "lxml")
    curr_buy = []
    usd_curr_buy, eur_curr_buy = [], []
    for each in soup.findAll('td', class_="money_price buy_price"):
        if "eur-usd" not in str(each):
            if "usd" in str(each):
                usd_curr_buy.append(each.text)
            if "eur" in str(each):
                eur_curr_buy.append(each.text)
        curr_buy.append(each)

  # Благодатка
    curr_sell = []
    usd_curr_sell, eur_curr_sell = [], []
    for each in soup.findAll('td', class_="money_price"):
        if each not in curr_buy:
            if "eur-usd" not in str(each):
                if "usd" in str(each):
                    usd_curr_sell.append(each.text)
                if "eur" in str(each):
                    eur_curr_sell.append(each.text)
            curr_sell.append(each)
    print(f"\t usd currency sale{usd_curr_sell} ,eur currency sale{eur_curr_sell},"
          f"usd currency buy {usd_curr_buy}, eur currency buy{eur_curr_buy} ")
    row_name = ["Валюта", "операция", "до 200", "<10.000", ">10.000"]
    data = {row_name[0]: ["$", "$", "€", "€"],
            row_name[1]: ["покупка", "продажа", "покупка", "продажа"],
            row_name[2]: [usd_curr_buy[0], usd_curr_sell[0], eur_curr_buy[0], eur_curr_sell[0]],
            row_name[3]: [usd_curr_buy[1], usd_curr_sell[1], eur_curr_buy[1], eur_curr_sell[1]],
            row_name[4]: [usd_curr_buy[2], usd_curr_sell[2], eur_curr_buy[2], eur_curr_sell[2]]
            }

# ЦБР
    c = requests.get("http://www.cbr.ru")
    cbr_soup = BeautifulSoup(c.content, "lxml")
    x = cbr_soup.find_all('div', class_="main-indicator_rate")
    try:
      rmb = x[0].findAll('div', class_="col-md-2 col-xs-9 _right mono-num")
      usd = x[1].findAll('div', class_="col-md-2 col-xs-9 _right mono-num")
      eur = x[2].findAll('div', class_="col-md-2 col-xs-9 _right mono-num")
      usd_rate = [i.string[:7] for i in usd]
      eur_rate = [i.string[:7] for i in eur]
    except Exception as e:
      print(f'caught {type(e)}: e')
      usd_rate[1] = 0
      eur_rate[1] = 0
      await message.answer("Не смог запарсить сайт ЦентрБанка")
      print(f"\t {usd_rate[1]}, {eur_rate[1]}")
    await message.answer(f"Данные с обменного пункта Благодатка, курс по ЦБ на сегодня $={usd_rate[1]} ₽, € = {eur_rate[1]} ₽",
                         reply_markup = markup_currency("currency", data, row_name))

async def main():
  await dp.start_polling(bot)

if __name__ == "__main__":
 asyncio.run(main())
