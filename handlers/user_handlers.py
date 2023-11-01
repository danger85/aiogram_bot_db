from aiogram.types import Message,CallbackQuery
from aiogram.filters import Command, CommandStart
from aiogram import Router,F
from lexicon.lexicon_ru import LEXICON_RU
from bs4 import BeautifulSoup
import requests
from keyboards.currency_kb import currency_kb
from keyboards.num_kb import numbers_kb
import urllib3
urllib3.disable_warnings()

router= Router()

""" @router.message(CommandStart)
async def cmd_start(message:Message):
  await message.answer(text=LEXICON_RU['/start']) """


@router.message(Command(commands="help"))
async def help_command(message:Message):
  await message.answer(text=LEXICON_RU['/help'])

@router.message(Command("dice"))
async def cmd_dice(message: Message):
  await message.answer_dice(emoji="🎲")

@router.message(Command("c"))
async def currency(message: Message):
    print(f"In currency function, called by command /c")
    #print(f"\tmessage text is {message.text}, came from {message.from_user.id}")
    qty_out_text= ''
    exchange_k: int = 0
    #await bot.delete_message(message.chat.id, message.message_id)
    # print("in currency function. called by command. Message id = ", message.message_id)
    r = requests.get("https://blagodatka.ru/", timeout=10, verify=False)
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
    data : list [list] = [[row_name[0], "$", "$", "€", "€"],
                         [row_name[1], "покупка", "продажа", "покупка", "продажа"],
                         [row_name[2], usd_curr_buy[0], usd_curr_sell[0], eur_curr_buy[0], eur_curr_sell[0]],
                         [row_name[3], usd_curr_buy[1], usd_curr_sell[1], eur_curr_buy[1], eur_curr_sell[1]],
                         [row_name[4], usd_curr_buy[2], usd_curr_sell[2], eur_curr_buy[2], eur_curr_sell[2]]]

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
                         reply_markup = currency_kb("currency",data))

@router.callback_query(F.data.contains("cur"))
async def calc(callback: CallbackQuery):# {"Kb":"cur","V":"100.0","CF":"cur"}
  recieved_data = eval(callback.data)
  print(f"Came from {recieved_data['CF']} to {__name__},CALC function by callback,{recieved_data}, action is {recieved_data['Kb']}")
  exchange_k = recieved_data['V']
  mul_div = recieved_data['Kb']
  if mul_div[:-1] == "div":
    await callback.message.answer(f"Введите сумму для внесения в кассу (₽), которую хотите обменять на {mul_div[-1]}",
                                  reply_markup=numbers_kb("calc", "0"))
  elif mul_div[:-1] == "mul":
    await callback.message.answer(f"Введите сумму для внесения в кассу ({mul_div[-1]}), которую хотите обменять на ₽",
                                  reply_markup=numbers_kb("calc", "0"))

@router.callback_query(F.data.contains("num")) #обработка показа клавиатуры
async def callback_num(callback: CallbackQuery):
  print(f"in {__name__}, by Callback, called by: {callback.data}")
  #print(f"\tmessage text is {callback.message.text}, came from user {callback.message.from_user.id}")
  recived_data:dict = eval(callback.data)
  digit = recived_data["V"]

  if recived_data["CF"] == "delete":  # если пришли из удаления
    global id_to_delete
    if len(id_to_delete) > 0:
      if id_to_delete[0] == "_":
          id_to_delete = ""
    id_to_delete = id_to_delete + digit
    await callback.edit_message_text(id_to_delete, callback.message.chat.id, callback.message.message_id, reply_markup=numbers_kb("delete", "0"))

  if recived_data["CF"] == "fill_table":
    global get_date
    if digit.isdigit() and len(get_date) <= 10:
      if get_date[:1] == "_":
        get_date = ""
      get_date = get_date + digit
    if len(get_date) == 2 or len(get_date) == 5:
      get_date = get_date + "."
    if digit == "cls":
      get_date = "_"
    await callback.edit_message_text(get_date, callback.message.chat.id, callback.message.message_id, reply_markup=numbers_kb("fill_table", get_date))

  if recived_data["CF"] == "mod_p" or recived_data["CF"] == "calc":
    global qty_out_text
    qty_out_text = qty_out_text + str(digit)
    await callback.message.edit_text(qty_out_text, reply_markup=numbers_kb(callback.data["CF"]))

@router.callback_query(F.data.contains("func_key") & F.data.contains("enter") & F.data.contains("calc")) #пришли после нажатия ввода при вычислении денег
async def exchange_calc(callback: CallbackQuery):
  recived_data:dict= eval(callback.data)
  print(f"in exchange_calc function, ClBkHr, called by {list(recived_data.values())}")
  print(f"\tmessage text is {callback.message.text}, came from {callback.message.from_user.id}")
  global messages_dict
  global exchange_k
  global qty_out_text
  global mul_div
  if mul_div[:-1] == "div":
    print(f"{qty_out_text}, {exchange_k}")
    await callback.message.edit_text(f"При обмене {qty_out_text} ₽ , получите {float(qty_out_text) / float(exchange_k)} {mul_div[-1]}")
  else:
    await callback.message.edit_text(f"При обмене {qty_out_text} {mul_div[-1]}, получите {float(qty_out_text) * float(exchange_k)} ₽")
