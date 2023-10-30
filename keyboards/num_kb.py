def markup_num(c_f: str, val: str): #формирование кнопок в виде циферок
  print(f"\tCame from {c_f} in markup_num, markup layout ")
  print(f"\tmessage is {val}, lh = {len(val)}")
  lh = len(val)
  m_up_num = InlineKeyboardBuilder()
  ikb = InlineKeyboardButton

  def _num_one_to_nine():# создание кнопок от 1 до 9
    m_up_num.add: list[InlineKeyboardButton]=[InlineKeyboardButton(text=i, callback_data="{\"Kb\":\"num\",\"V\":i,\"CF\":\"" + c_f + "\"}") for i in range(7,10))]
    m_up_num.add: list[InlineKeyboardButton]=[InlineKeyboardButton(text=i, callback_data="{\"Kb\":\"num\",\"V\":i,\"CF\":\"" + c_f + "\"}") for i in range(4,7))]
    m_up_num.add: list[InlineKeyboardButton]=[InlineKeyboardButton(text=i, callback_data="{\"Kb\":\"num\",\"V\":i,\"CF\":\"" + c_f + "\"}") for i in range(1,4))]
  """   m_up_num.add(InlineKeyboardButton(text="7", callback_data="{\"Kb\":\"num\",\"V\":\"7\",\"CF\":\"" + c_f + "\"}"),
                 InlineKeyboardButton(text="8", callback_data="{\"Kb\":\"num\",\"V\":\"8\",\"CF\":\"" + c_f + "\"}"),
                 InlineKeyboardButton(text="9", callback_data="{\"Kb\":\"num\",\"V\":\"9\",\"CF\":\"" + c_f + "\"}"),
                 InlineKeyboardButton(text="4", callback_data="{\"Kb\":\"num\",\"V\":\"4\",\"CF\":\"" + c_f + "\"}"),
                 InlineKeyboardButton(text="5", callback_data="{\"Kb\":\"num\",\"V\":\"5\",\"CF\":\"" + c_f + "\"}"),
                 InlineKeyboardButton(text="6", callback_data="{\"Kb\":\"num\",\"V\":\"6\",\"CF\":\"" + c_f + "\"}"),
                 InlineKeyboardButton(text="1", callback_data="{\"Kb\":\"num\",\"V\":\"1\",\"CF\":\"" + c_f + "\"}"),
                 InlineKeyboardButton(text="2", callback_data="{\"Kb\":\"num\",\"V\":\"2\",\"CF\":\"" + c_f + "\"}"),
                 InlineKeyboardButton(text="3", callback_data="{\"Kb\":\"num\",\"V\":\"3\",\"CF\":\"" + c_f + "\"}")
                ) """

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
    m_up_num.add(InlineKeyboardButton(text="0", callback_data="{\"Kb\":\"num\",\"V\":\"0\",\"CF\":\"" + c_f + "\"}"))
    m_up_num.add(InlineKeyboardButton(text="Ввод.", callback_data="{\"Kb\":\"func_key\",\"V\":\"enter\",\"CF\":\"" + c_f + "\"}"))
  m_up_num.adjust(3)
  return m_up_num.as_markup()