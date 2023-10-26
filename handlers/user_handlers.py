from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram import Router
from lexicon.lexicon_ru import LEXICON_RU
from bs4 import BeautifulSoup
import requests

router= Router()
@router.message(CommandStart)
async def cmd_start(message:Message):
  await message.answer(text=LEXICON_RU['/start'])

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