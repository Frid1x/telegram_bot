import telebot
import sqlite3
def get_db_connection():
    return sqlite3.connect('users.db')
db = get_db_connection()
c = db.cursor()
# c.execute("""CREATE TABLE users (
#     id integer,
#     name text,
#     age integer,
#     phone_number text,
#     registrated integer,
#     language text
# )""")
nick=None
reg_message_id=None
user_nick=None
# c.execute("DELETE FROM users WHERE registrated = 1")
db.commit()
c.execute(f"SELECT * FROM users")
items = c.fetchall()
for item in items:
    print(item)

# c.execute(f"SELECT name FROM users")
# items = c.fetchall()
# for item in items:
#     print(item[0])
bot=telebot.TeleBot("7598811790:AAG8AVP6fn3BaVlbg4pX5CrVczSZTSC1Wvk")
# @bot.message_handler(commands=["text"])
# def text(message):
#     markup=telebot.types.InlineKeyboardMarkup()
#     markup.add(telebot.types.InlineKeyboardButton(text="Нажми!",url="youtube.com"))
#     bot.send_message(message.chat.id,text="Привет",reply_markup=markup)
item1=None
item2=None
item3=None
item4=None
def get_db_connection():
    return sqlite3.connect('users.db')

# Словарь для хранения данных пользователей
user_data = {}
name = "Как тебя зовут?"
age = "Сколько тебе лет ?"
number = "какой у тебя номер телефона ? "
give_number = "Отправить номер телефона"
not_give_number = "Не отправлять номер телефона"
final_name = "Имя"
final_age = "Возраст"
final_number = "Номер телефона"
not_specified = "Не указан"
not_lying_me = "Не ври мне"
set_language = "Язык выбран"
choose_language="Выбирите язык"
used_command="Вы уже использовали эту команду"
already_reg="Вы уже зарегистрированы"
cant_send_to_mes="Вы не можете отправить сообщение сами себе"
not_registr="Вы не зарегистрированы, пожалуйста, зарегистрируйтесь"
well_send_mes="Ваше сообщение успешно отправлено!"
write_message="Напишите ваше сообщение"
acc_not_be="Такого аккаунта не существует"
writ_name_of_acc="Напишите имя аккаунта, которому вы хотите отправить сообщение"
your_message_text="сообщение"
have_new_message="У вас новое сообщение от"

cant_send_comm_now="Вам надо отправить текст, а не команду"
def set_user_language(message):
    global name, age, number, give_number, not_give_number, final_number, final_age, final_name, not_specified, not_lying_me, set_language, choose_language, already_reg, used_command, cant_send_to_mes, not_registr, well_send_mes, write_message, acc_not_be, writ_name_of_acc, your_message_text, have_new_message,cant_send_comm_now
    db = get_db_connection()
    c = db.cursor()
    c.execute(f"SELECT language FROM users WHERE id = {message.chat.id}")
    items = c.fetchall()
    for item in items:
        if item[0] == "english":
            name = "What's your name?"
            age = "How old are you ?"
            number = "What's your phone number ?"
            give_number = "Send number"
            not_give_number = "Not send number"
            final_name = "name"
            final_age = "age"
            final_number = "phone number"
            not_specified = "Not specified"
            not_lying_me = "Don't deceive me"
            set_language = "language selected"
            choose_language = "Choose language"
            already_reg = "You are already registered"
            used_command = "you are already used this command"
            cant_send_to_mes = "You can't send message to yourself"
            not_registr = "you don't registerd, please registrate"
            well_send_mes = "your message sent well"
            write_message = "please write message"
            acc_not_be = "this account doesn't exist "
            writ_name_of_acc = "write name of account to which you want send message"
            your_message_text = "message"
            have_new_message = "you have a new message"

            cant_send_comm_now = "You need to send a message,not a command"
        elif item[0] == "germany":
            name = "Was ist deine Name?"
            age = "Wie atl sind Sie ?"
            number = "Wie lauet Telefonnummer ? "
            give_number = "Geben Telefonnummer"
            not_give_number = "Geben nicht Telefonnummer"
            final_name = "Name"
            final_age = "atl"
            final_number = "Telefonnummer"
            not_specified = "Nicht spezifiziert"
            not_lying_me = "Betrügen nicht "
            set_language = "Sprache ausgewählt"
            choose_language = "Sprache auswählen"
            already_reg = "Sie sind bereits registriert"
            used_command = "Sie haben diesen Befehl bereits verwendet"
            cant_send_to_mes = "Sie können keine Nachricht an sich selbst senden"
            not_registr = "Sie sind nicht registriert, bitte registrieren Sie sich"
            well_send_mes = "Nachricht erfolgreich gesendet"
            write_message = "Nachricht schreib"
            acc_not_be = "Es existiert kein solches Konto"
            writ_name_of_acc = "Geben Sie den Namen des Kontos ein, an das Sie die Nachricht senden möchten"
            your_message_text = "Nachricht"
            have_new_message = "Sie haben neu Nachricht"

            cant_send_comm_now="Sie müssen einen Text senden, keinen Befehl"
        elif item[0] == "chinese":
            name = "你叫什么名字?"
            age = "多大？"
            number = "你的电话号码是都少 ？"
            give_number = "给电话号码"
            not_give_number = "不给电话号码"
            final_name = "名字"
            final_age = "岁"
            final_number = "电话号码"
            not_specified = "不指出的"
            not_lying_me = "不诓"
            set_language = "语取的"
            choose_language = "取语"
            already_reg = "你是已经挂号"
            used_command = "你已经用了"
            cant_send_to_mes = "您不可以寄给消息给对自己"
            not_registr = "您还没有注册,请注册"
            well_send_mes = "你的消息邮寄了的好!"
            write_message = "请写消息"
            acc_not_be = "这种账户不存在"
            writ_name_of_acc = "请写账户的名字你想寄给消息"
            your_message_text = "消息"
            have_new_message = "新的消息"

            cant_send_comm_now="您需要寄给消息"
        elif item[0] == "japanese":
            name = "お名前は？"
            age = "おいくつですか"
            number = "あなたの電話番号は何ですか？"
            give_number = "送ります"
            not_give_number = "送りません"
            final_name = "お名前"
            final_age = "歳"
            final_number = "電話番号"
            not_specified = "指定されていない"
            not_lying_me = "ごまかさないでください"
            set_language = "言語は選択された"
            choose_language = "言語を選択してください"
            already_reg = "あなたはすでに登録されています"
            used_command = "すでにコマンドを使用しています"
            cant_send_to_mes = "自分自身にメッセージを送信することはできません"
            not_registr = "あなたは登録されていません、登録してください"
            well_send_mes = "メッセージは正常に送信されました!"
            write_message = "メッセージを書いてください"
            acc_not_be = "このアカウントは存在しません"
            writ_name_of_acc = "メッセージを送りたいアカウントの名前を書いてください"
            your_message_text = "メッセージ"
            have_new_message = "から新しいメッセージが届きました"

            cant_send_comm_now="コマンドではなくメッセージを送信する必要があります"
        elif item[0] == "russian":
            name = "Как тебя зовут?"
            age = "Сколько тебе лет ?"
            number = "какой у тебя номер телефона ? "
            give_number = "Отправить номер телефона"
            not_give_number = "Не отправлять номер телефона"
            final_name = "Имя"
            final_age = "Возраст"
            final_number = "Номер телефона"
            not_specified = "Не указан"
            not_lying_me = "Не ври мне"
            set_language = "Язык выбран"
            choose_language = "Выбирите язык"
            used_command = "Вы уже использовали эту команду"
            already_reg = "Вы уже зарегистрированы"
            cant_send_to_mes = "Вы не можете отправить сообщение сами себе"
            not_registr = "Вы не зарегистрированы, пожалуйста, зарегистрируйтесь"
            well_send_mes = "Ваше сообщение успешно отправлено!"
            write_message = "Напишите ваше сообщение"
            acc_not_be = "Такого аккаунта не существует"
            writ_name_of_acc = "Напишите имя аккаунта, которому вы хотите отправить сообщение"
            your_message_text = "сообщение"
            have_new_message = "У вас новое сообщение от"

            cant_send_comm_now="Вам надо отправить сообщение, а не команду"
# Обработчик команды /start
@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    db = get_db_connection()
    c = db.cursor()
    global cant_send_comm_now,name,age,number,give_number,not_give_number,final_number,final_age,final_name, not_specified,not_lying_me,set_language,choose_language,already_reg,used_command,      cant_send_to_mes,not_registr,well_send_mes,write_message,acc_not_be,writ_name_of_acc,your_message_text,have_new_message
    if call.data == 'english':
        name = "What's your name?"
        age = "How old are you ?"
        number = "What's your phone number ?"
        give_number="Send number"
        not_give_number="Not send number"
        final_name="name"
        final_age="age"
        final_number="phone number"
        not_specified="Not specified"
        not_lying_me="Don't deceive me"
        set_language="language selected"
        choose_language="Choose language"
        already_reg="You are already registered"
        used_command="you are already used this command"

        cant_send_to_mes="You can't send message to yourself"
        not_registr="you don't registerd, please registrate"
        well_send_mes="your message sent well"
        write_message="please write message"
        acc_not_be="this account doesn't exist "
        writ_name_of_acc="write name of account to which you want send message"
        your_message_text="message"
        have_new_message="you have a new message"
        cant_send_comm_now = "You need to send a message,not a command"
        c.execute(f"UPDATE users SET language = 'english' WHERE id = {call.message.chat.id}")
        db.commit()
        # bot.send_message(call.message.chat.id, "Good")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None,text="Good")
    elif call.data == 'germany':
        name = "Was ist deine Name?"
        age = "Wie atl sind Sie ?"
        number = "Wie lauet Telefonnummer ? "
        give_number="Geben Telefonnummer"
        not_give_number="Geben nicht Telefonnummer"
        final_name="Name"
        final_age="atl"
        final_number="Telefonnummer"
        not_specified="Nicht spezifiziert"
        not_lying_me="Betrügen nicht "
        set_language="Sprache ausgewählt"
        choose_language = "Sprache auswählen"
        already_reg = "Sie sind bereits registriert"
        used_command = "Sie haben diesen Befehl bereits verwendet"

        cant_send_to_mes="Sie können keine Nachricht an sich selbst senden"
        not_registr="Sie sind nicht registriert, bitte registrieren Sie sich"
        well_send_mes="Nachricht erfolgreich gesendet"
        write_message="Nachricht schreib"
        acc_not_be="Es existiert kein solches Konto"
        writ_name_of_acc="Geben Sie den Namen des Kontos ein, an das Sie die Nachricht senden möchten"
        your_message_text="Nachricht"
        have_new_message="Sie haben neu Nachricht"
        cant_send_comm_now = "Sie müssen einen Text senden, keinen Befehl"
        c.execute(f"UPDATE users SET language = 'germany' WHERE id = {call.message.chat.id}")
        db.commit()
        # bot.send_message(call.message.chat.id, "Gute")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None,text="Gute")
    elif call.data=="chinese":
        name = "你叫什么名字?"
        age = "多大？"
        number = "你的电话号码是都少 ？"
        give_number="给电话号码"
        not_give_number="不给电话号码"
        final_name="名字"
        final_age="岁"
        final_number="电话号码"
        not_specified="不指出的"
        not_lying_me="不诓"
        set_language="语取的"
        choose_language="取语"
        already_reg="你是已经挂号"
        used_command="你已经用了"

        cant_send_to_mes="您不可以寄给消息给对自己"
        not_registr="您还没有注册,请注册"
        well_send_mes="你的消息邮寄了的好!"
        write_message="请写消息"
        acc_not_be="这种账户不存在"
        writ_name_of_acc="请写账户的名字你想寄给消息"
        your_message_text="消息"
        have_new_message="新的消息"
        cant_send_comm_now = "您需要寄给消息"
        c.execute(f"UPDATE users SET language = 'chinese' WHERE id = {call.message.chat.id}")
        db.commit()
        # bot.send_message(call.message.chat.id,text="太好了")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None,text="太好了")
    elif call.data == "japanese":
        name = "お名前は？"
        age = "おいくつですか"
        number = "あなたの電話番号は何ですか？"
        give_number="送ります"
        not_give_number="送りません"
        final_name="お名前"
        final_age="歳"
        final_number="電話番号"
        not_specified="指定されていない"
        not_lying_me="ごまかさないでください"
        set_language="言語は選択された"
        choose_language="言語を選択してください"
        already_reg="あなたはすでに登録されています"
        used_command="すでにコマンドを使用しています"

        cant_send_to_mes="自分自身にメッセージを送信することはできません"
        not_registr="あなたは登録されていません、登録してください"
        well_send_mes="メッセージは正常に送信されました!"
        write_message="メッセージを書いてください"
        acc_not_be="このアカウントは存在しません"
        writ_name_of_acc="メッセージを送りたいアカウントの名前を書いてください"
        your_message_text="メッセージ"
        have_new_message="から新しいメッセージが届きました"
        cant_send_comm_now = "コマンドではなくメッセージを送信する必要があります"

        c.execute(f"UPDATE users SET language = 'japanese' WHERE id = {call.message.chat.id}")
        db.commit()
        # bot.send_message(call.message.chat.id,text="いいです")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None,text="いいです")
    elif call.data =="russian":
        name = "Как тебя зовут?"
        age = "Сколько тебе лет ?"
        number = "какой у тебя номер телефона ? "
        give_number="Отправить номер телефона"
        not_give_number="Не отправлять номер телефона"
        final_name="Имя"
        final_age="Возраст"
        final_number="Номер телефона"
        not_specified="Не указан"
        not_lying_me="Не ври мне"
        set_language="Язык выбран"
        choose_language = "Выбирите язык"
        used_command = "Вы уже использовали эту команду"
        already_reg = "Вы уже зарегистрированы"

        cant_send_to_mes = "Вы не можете отправить сообщение сами себе"
        not_registr = "Вы не зарегистрированы, пожалуйста, зарегистрируйтесь"
        well_send_mes = "Ваше сообщение успешно отправлено!"
        write_message = "Напишите ваше сообщение"
        acc_not_be = "Такого аккаунта не существует"
        writ_name_of_acc = "Напишите имя аккаунта, которому вы хотите отправить сообщение"
        your_message_text = "сообщение"
        have_new_message = "У вас новое сообщение от"
        cant_send_comm_now = "Вам надо отправить сообщение, а не команду"
        c.execute(f"UPDATE users SET language = 'russian' WHERE id = {call.message.chat.id}")
        db.commit()
        # bot.send_message(call.message.chat.id,text="Хорошо")
        # bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,reply_markup=None)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,reply_markup=None,text="Хорошо")
    db.close()
    bot.answer_callback_query(call.id, set_language)

@bot.message_handler(commands=['send_message'])
def s_message_to_someone(message):
    global cant_send_comm_now,name, age, number, give_number, not_give_number, final_number, final_age, final_name, not_specified, not_lying_me, set_language, choose_language, already_reg, used_command,user_nick,cant_send_to_mes,not_registr,well_send_mes,write_message,acc_not_be,writ_name_of_acc,your_message_text,have_new_message
    db = get_db_connection()
    c = db.cursor()
    set_user_language(message)
    # Проверяем, зарегистрирован ли пользователь
    c.execute(f"SELECT registrated FROM users WHERE id = {message.chat.id}")
    items = c.fetchall()

    if not items:
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        bot.send_message(message.chat.id, not_registr)


    else:
        for item in items:
            print(item[0])
            if item[0] == 1:
                bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
                c.execute(f"SELECT name FROM users WHERE id = {message.chat.id}")
                items = c.fetchall()
                for item in items:
                    print(item[0])
                    user_nick=item[0]
                bot.send_message(message.chat.id, text=writ_name_of_acc + ":")
                bot.register_next_step_handler(message, get_name)
            elif item[0] == 0:
                bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
                bot.send_message(message.chat.id, not_registr)

    db.close()
def get_name(message):
    global nick
    if message.text.startswith('/'):
        bot.send_message(message.chat.id,cant_send_comm_now)
    else:
        db = get_db_connection()
        c = db.cursor()
        c.execute(f"SELECT name FROM users WHERE id = {message.chat.id}")
        items = c.fetchall()
        name_found = False
        for item in items:
            if item[0] == message.text:
                bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
                bot.send_message(message.chat.id,cant_send_to_mes)
                return
            else:
                c.execute(f"SELECT name FROM users ")
                items = c.fetchall()
                for item in items:
                    if item[0] == message.text:
                        name_found = True
                        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
                        bot.send_message(message.chat.id,write_message + ":")
                        nick=message.text
                        bot.register_next_step_handler(message, get_soo)
                        break
        if not name_found:
            bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
            bot.send_message(message.chat.id, acc_not_be)
            # if not items:
            #     bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
            #     bot.send_message(message.chat.id,"Такой пользователь не найден, пожалуйста попробуйте еще раз")
def get_soo(message):
    global cant_send_comm_now,nick,user_nick,name, age, number, give_number, not_give_number, final_number, final_age, final_name, not_specified, not_lying_me, set_language, choose_language, already_reg, used_command,user_nick,cant_send_to_mes,not_registr,well_send_mes,write_message,acc_not_be,writ_name_of_acc,your_message_text,have_new_message
    if message.text.startswith('/'):
        bot.send_message(message.chat.id,cant_send_comm_now)
    else:
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        bot.send_message(message.chat.id, well_send_mes)
        db = get_db_connection()
        c = db.cursor()
        c.execute(f"SELECT id FROM users WHERE name = '{nick}'")
        items = c.fetchall()
        for item in items:
            print(item[0])
            c.execute(f"SELECT language FROM users WHERE name = '{nick}'")
            items= c.fetchall()
            for item in items:
                if item[0] == "english":
                    name = "What's your name?"
                    age = "How old are you ?"
                    number = "What's your phone number ?"
                    give_number = "Send number"
                    not_give_number = "Not send number"
                    final_name = "name"
                    final_age = "age"
                    final_number = "phone number"
                    not_specified = "Not specified"
                    not_lying_me = "Don't deceive me"
                    set_language = "language selected"
                    choose_language = "Choose language"
                    already_reg = "You are already registered"
                    used_command = "you are already used this command"
                    cant_send_to_mes = "You can't send message to yourself"
                    not_registr = "you don't registerd, please registrate"
                    well_send_mes = "your message sent well"
                    write_message = "please write message"
                    acc_not_be = "this account doesn't exist "
                    writ_name_of_acc = "write name of account to which you want send message"
                    your_message_text = "message"
                    have_new_message = "you have a new message"
                    cant_send_comm_now = "You need to send a message,not a command"
                elif item[0] == "germany":
                    name = "Was ist deine Name?"
                    age = "Wie atl sind Sie ?"
                    number = "Wie lauet Telefonnummer ? "
                    give_number = "Geben Telefonnummer"
                    not_give_number = "Geben nicht Telefonnummer"
                    final_name = "Name"
                    final_age = "atl"
                    final_number = "Telefonnummer"
                    not_specified = "Nicht spezifiziert"
                    not_lying_me = "Betrügen nicht "
                    set_language = "Sprache ausgewählt"
                    choose_language = "Sprache auswählen"
                    already_reg = "Sie sind bereits registriert"
                    used_command = "Sie haben diesen Befehl bereits verwendet"
                    cant_send_to_mes = "Sie können keine Nachricht an sich selbst senden"
                    not_registr = "Sie sind nicht registriert, bitte registrieren Sie sich"
                    well_send_mes = "Nachricht erfolgreich gesendet"
                    write_message = "Nachricht schreib"
                    acc_not_be = "Es existiert kein solches Konto"
                    writ_name_of_acc = "Geben Sie den Namen des Kontos ein, an das Sie die Nachricht senden möchten"
                    your_message_text = "Nachricht"
                    have_new_message = "Sie haben neu Nachricht"
                    cant_send_comm_now = "Sie müssen einen Text senden, keinen Befehl"
                elif item[0] == "chinese":
                    name = "你叫什么名字?"
                    age = "多大？"
                    number = "你的电话号码是都少 ？"
                    give_number = "给电话号码"
                    not_give_number = "不给电话号码"
                    final_name = "名字"
                    final_age = "岁"
                    final_number = "电话号码"
                    not_specified = "不指出的"
                    not_lying_me = "不诓"
                    set_language = "语取的"
                    choose_language = "取语"
                    already_reg = "你是已经挂号"
                    used_command = "你已经用了"
                    cant_send_to_mes = "您不可以寄给消息给对自己"
                    not_registr = "您还没有注册,请注册"
                    well_send_mes = "你的消息邮寄了的好!"
                    write_message = "请写消息"
                    acc_not_be = "这种账户不存在"
                    writ_name_of_acc = "请写账户的名字你想寄给消息"
                    your_message_text = "消息"
                    have_new_message = "新的消息"
                    cant_send_comm_now = "您需要寄给消息"
                elif item[0] == "japanese":
                    name = "お名前は？"
                    age = "おいくつですか"
                    number = "あなたの電話番号は何ですか？"
                    give_number = "送ります"
                    not_give_number = "送りません"
                    final_name = "お名前"
                    final_age = "歳"
                    final_number = "電話番号"
                    not_specified = "指定されていない"
                    not_lying_me = "ごまかさないでください"
                    set_language = "言語は選択された"
                    choose_language = "言語を選択してください"
                    already_reg = "あなたはすでに登録されています"
                    used_command = "すでにコマンドを使用しています"
                    cant_send_to_mes = "自分自身にメッセージを送信することはできません"
                    not_registr = "あなたは登録されていません、登録してください"
                    well_send_mes = "メッセージは正常に送信されました!"
                    write_message = "メッセージを書いてください"
                    acc_not_be = "このアカウントは存在しません"
                    writ_name_of_acc = "メッセージを送りたいアカウントの名前を書いてください"
                    your_message_text = "メッセージ"
                    have_new_message = "から新しいメッセージが届きました"
                    cant_send_comm_now = "コマンドではなくメッセージを送信する必要があります"
                elif item[0] == "russian":
                    name = "Как тебя зовут?"
                    age = "Сколько тебе лет ?"
                    number = "какой у тебя номер телефона ? "
                    give_number = "Отправить номер телефона"
                    not_give_number = "Не отправлять номер телефона"
                    final_name = "Имя"
                    final_age = "Возраст"
                    final_number = "Номер телефона"
                    not_specified = "Не указан"
                    not_lying_me = "Не ври мне"
                    set_language = "Язык выбран"
                    choose_language = "Выбирите язык"
                    used_command = "Вы уже использовали эту команду"
                    already_reg = "Вы уже зарегистрированы"
                    cant_send_to_mes = "Вы не можете отправить сообщение сами себе"
                    not_registr = "Вы не зарегистрированы, пожалуйста, зарегистрируйтесь"
                    well_send_mes = "Ваше сообщение успешно отправлено!"
                    write_message = "Напишите ваше сообщение"
                    acc_not_be = "Такого аккаунта не существует"
                    writ_name_of_acc = "Напишите имя аккаунта, которому вы хотите отправить сообщение"
                    your_message_text = "сообщение"
                    have_new_message = "У вас новое сообщение от"
                    cant_send_comm_now = "Вам надо отправить сообщение, а не команду"
                c.execute(f"SELECT id FROM users WHERE name = '{nick}'")
                items = c.fetchall()
                for item in items:
                    bot.send_message(chat_id=item[0],text=f"{have_new_message}:\n{user_nick}\n{your_message_text}: {message.text}")
@bot.message_handler(commands=['comment'])
def comment(message):
    global cant_send_comm_now,name,age,number,give_number,not_give_number,final_number,final_age,final_name, not_specified,not_lying_me,set_language,choose_language,already_reg,used_command,cant_send_to_mes,not_registr,well_send_mes,write_message,acc_not_be,writ_name_of_acc,your_message_text,have_new_message
    db = get_db_connection()
    c = db.cursor()
    set_user_language(message)
    # Проверяем, зарегистрирован ли пользователь
    c.execute(f"SELECT registrated FROM users WHERE id = {message.chat.id}")
    items = c.fetchall()

    if not items:
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        bot.send_message(message.chat.id,not_registr)


    else:
        for item in items:
            print(item[0])
            if item[0] == 1:
                bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
                bot.send_message(message.chat.id,text=write_message + ":")
                bot.register_next_step_handler(message, get_comment)
            elif item[0] == 0:
                bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
                bot.send_message(message.chat.id,not_registr)


    db.close()
def get_comment(message):
    if message.text.startswith('/'):
        bot.send_message(message.chat.id,cant_send_comm_now)
    else:
        db = get_db_connection()
        c = db.cursor()
        c.execute(f"SELECT name FROM users WHERE id = {message.chat.id}")
        items = c.fetchall()
        for item in items:
            bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
            bot.send_message(message.chat.id,well_send_mes)
            bot.send_message(chat_id=5098677942,text=f"Пользователь с ником:\n{item[0]}\nсообщение: {message.text}")
@bot.message_handler(commands=['data'])
def statics(message):
    global cant_send_comm_now,name,age,number,give_number,not_give_number,final_number,final_age,final_name, not_specified,not_lying_me,set_language,choose_language,already_reg,used_command,cant_send_to_mes,not_registr,well_send_mes,write_message,acc_not_be,writ_name_of_acc,your_message_text,have_new_message
    db = get_db_connection()
    c = db.cursor()
    set_user_language(message)
    c.execute(f"SELECT * FROM users WHERE id = {message.chat.id}")
    items = c.fetchall()
    for item in items:
        if not items:
            bot.send_message(message.chat.id,"Ваши данные не найдены , скорее всего вы не зарегестрированы")
        else :
            item1 = item[1]
            item2 = item[2]
            item3 = item[3]
            item4 = item[0]
            response = f"{final_name}: {item1}\n{final_age}: {item2}\n{final_number}: {item3}\nid: {item4}"
            print(response)
            bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
            bot.send_message(message.chat.id,response)
    db.commit()
    db.close()

@bot.message_handler(commands=['language'])
def change_language(message):
    global cant_send_comm_now,name,age,number,give_number,not_give_number,final_number,final_age,final_name, not_specified,not_lying_me,set_language,choose_language,already_reg,used_command,reg_message_id,cant_send_to_mes,not_registr,well_send_mes,write_message,acc_not_be,writ_name_of_acc,your_message_text,have_new_message
    db = get_db_connection()
    c = db.cursor()
    set_user_language(message)
    markup = telebot.types.InlineKeyboardMarkup()
    btn1 = telebot.types.InlineKeyboardButton("English", callback_data="english")
    btn2 = telebot.types.InlineKeyboardButton("Deutsch", callback_data="germany")
    btn3 = telebot.types.InlineKeyboardButton("中文", callback_data="chinese")
    btn4 = telebot.types.InlineKeyboardButton("日本", callback_data="japanese")
    btn5 = telebot.types.InlineKeyboardButton("русский", callback_data="russian")
    markup.add(btn1, btn2, btn3, btn4, btn5)
    bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    sent_message=bot.send_message(message.chat.id, choose_language, reply_markup=markup)
    reg_message_id=sent_message.message_id

@bot.message_handler(commands=['start'])
def start_command(message):
    # Инициализация
    global cant_send_comm_now,name,age,number,give_number,not_give_number,final_number,final_age,final_name, not_specified,not_lying_me,set_language,choose_language,already_reg,used_command,cant_send_to_mes,not_registr,well_send_mes,write_message,acc_not_be,writ_name_of_acc,your_message_text,have_new_message
    db = get_db_connection()
    c = db.cursor()
    set_user_language(message)
    # Проверяем, зарегистрирован ли пользователь
    c.execute(f"SELECT registrated FROM users WHERE id = {message.chat.id}")
    items = c.fetchall()

    if not items:  # Если пользователь не найден, добавляем его
        c.execute(f"INSERT INTO users (id, registrated,language) VALUES ('{message.chat.id}', 0,'русский')")
        db.commit()
        print("Пользователь добавлен в базу данных.")

        # Отправляем сообщение с выбором языка
        markup = telebot.types.InlineKeyboardMarkup()
        btn1 = telebot.types.InlineKeyboardButton("English", callback_data="english")
        btn2 = telebot.types.InlineKeyboardButton("Deutsch", callback_data="germany")
        btn3 = telebot.types.InlineKeyboardButton("中文", callback_data="chinese")
        btn4 = telebot.types.InlineKeyboardButton("日本", callback_data="japanese")
        btn5 = telebot.types.InlineKeyboardButton("русский", callback_data="russian")
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        bot.send_message(message.chat.id, "Choose the language please", reply_markup=markup)
    else:
        for item in items:
            print(item[0])
            if item[0] == 1:
                bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
                bot.send_message(message.chat.id, used_command)
                db.close()
                return


    db.close()
    # user_data[message.chat.id] = {'id': 0}
    # db = get_db_connection()
    # c = db.cursor()
    # db.commit()
    # print(user_data[message.chat.id]['id'])
    # if user_data[message.chat.id]['id'] == 0:
    #     print(" gsflsg")
    #     c.execute(f"SELECT registrated FROM users WHERE id = {message.chat.id}")
    #     items = c.fetchall()
    #     for item in items:
    #         print(item[0])
    #         if item[0] == 1:
    #             bot.send_message(message.chat.id, text="Ты уже использовал эту команду")
    #             return
    #         else:
    #             c.execute(f"INSERT INTO users (id,registrated) VALUES ('{message.chat.id}',0)")
    #             markup=telebot.types.InlineKeyboardMarkup()
    #             btn1=telebot.types.InlineKeyboardButton("English", callback_data="english")
    #             btn2=telebot.types.InlineKeyboardButton("Deutsch",callback_data="germany")
    #             btn3=telebot.types.InlineKeyboardButton("中文",callback_data="chinese")
    #             btn4=telebot.types.InlineKeyboardButton("日本",callback_data="japanese")
    #             btn5=telebot.types.InlineKeyboardButton("русский",callback_data="russian")
    #             markup.add(btn1,btn2,btn3,btn4,btn5)
    #             bot.send_message(message.chat.id, "Choose the language please",reply_markup=markup)
    #
    # db.close()

@bot.message_handler(commands=["registr"])
def registr(message):
    global cant_send_comm_now,name,age,number,give_number,not_give_number,final_number,final_age,final_name, not_specified,not_lying_me,set_language,choose_language,already_reg,used_command,cant_send_to_mes,not_registr,well_send_mes,write_message,acc_not_be,writ_name_of_acc,your_message_text,have_new_message
    user_data[message.chat.id] = {'name': message.text }
    user_data[message.chat.id]['phone'] =f"{not_specified}"
    db = get_db_connection()
    c = db.cursor()
    set_user_language(message)
    c.execute(f"SELECT registrated FROM users WHERE id = {message.chat.id}")
    items=c.fetchall()
    for item in items:
        print(item[0])
        if item[0] == 1:
            bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
            bot.send_message(message.chat.id,already_reg)
            return
        elif item[0] == 0:
            bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
            bot.send_message(message.chat.id, name)
            bot.register_next_step_handler(message, process_name_step)
            return
    db.close()
def process_name_step(message):
    user_data[message.chat.id] = {'name': message.text}
    # Запрашиваем возраст
    bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    bot.send_message(message.chat.id, age)
    bot.register_next_step_handler(message, process_age_step)

# Обработка возраста
def process_age_step(message):
    # if int(message.text)
    user_data[message.chat.id]['age'] = message.text
    # Запрашиваем номер телефона
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
    item = telebot.types.KeyboardButton(give_number, request_contact=True)
    item1 = telebot.types.KeyboardButton(not_give_number)
    markup.add(item)
    markup.add(item1)
    bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    bot.send_message(message.chat.id, number, reply_markup=markup)


# Обработка номера телефона
@bot.message_handler(content_types=['contact' , 'text'])
def process_contact(message):
    if message.text != not_give_number and message.content_type !='contact':
        return
    else:
        # bot.edit_message_reply_markup(chat_id=message.chat.id, message_id=message.message_id-2, reply_markup=None)
        db = get_db_connection()
        c = db.cursor()
        if message.content_type == 'contact':
            contact = message.contact
            phone_number = str(contact.phone_number)
            user_data[message.chat.id]['phone'] = phone_number
        elif message.content_type=="text":
            user_data[message.chat.id]['phone'] = f"{not_specified}"
        # if user_data[message.chat.id]['name'].lower() !=message.from_user.first_name.lower():
        #     user_data[message.chat.id]['name'] = message.from_user.first_name
        #     response=f"{final_name}: {user_data[message.chat.id]['name']}\n{final_age}: {user_data[message.chat.id]['age']}\n{final_number}: {user_data[message.chat.id]['phone']}"+f"\n{not_lying_me}"+"😈"
        if user_data[message.chat.id]['name'].lower() == message.from_user.first_name.lower() == message.from_user.first_name.lower():
            response = f"{final_name}: {user_data[message.chat.id]['name']}\n{final_age}: {user_data[message.chat.id]['age']}\n{final_number}: {user_data[message.chat.id]['phone']}"
        else :
            response = f"{final_name}: {user_data[message.chat.id]['name']}\n{final_age}: {user_data[message.chat.id]['age']}\n{final_number}: {user_data[message.chat.id]['phone']}"
        # c.execute(f"UPDATE users SET ('{message.chat.id}','{user_data[message.chat.id]['name']}',{user_data[message.chat.id]['age']},{user_data[message.chat.id]['phone']},1)")
        c.execute(f"UPDATE users SET name = '{user_data[message.chat.id]['name']}' WHERE id = {message.chat.id}")
        c.execute(f"UPDATE users SET age = {user_data[message.chat.id]['age']} WHERE id = {message.chat.id}")
        c.execute(f"UPDATE users SET phone_number = '{user_data[message.chat.id]['phone']}' WHERE id = {message.chat.id}")
        c.execute(f"UPDATE users SET registrated = 1 WHERE id = {message.chat.id}")
        db.commit()
        c.execute(f"SELECT * FROM users WHERE id = {message.chat.id}")
        db.commit()
        items=c.fetchall()
        for item in items:
            print(item)
        # Формируем и отправляем сообщение с данными

        print(user_data[message.chat.id])
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        bot.send_message(message.chat.id, response,reply_markup=telebot.types.ReplyKeyboardRemove())
        db.close()

# # Обработчик для автоматического определения данных
# @bot.message_handler(commands=['auto'])
# def auto_command(message):
#     user_data[message.chat.id] = {
#         'name': message.from_user.first_name,
#         'age': f'{not_specified}',  # Возраст нельзя получить автоматически
#         'phone': f'{not_specified}'  # Телефон также нельзя получить автоматически
#     }
#     # Формируем и отправляем сообщение с данными
#     response = f"{final_name}: {user_data[message.chat.id]['name']}\n{final_age}: {user_data[message.chat.id]['age']}\n{final_number}: {user_data[message.chat.id]['phone']}"
#     print(user_data[message.chat.id])
#     bot.send_message(message.chat.id, response)



if __name__ == "__main__":


    # c.execute(f"SELECT registrated FROM users WHERE id = {message.chat.id}")



    bot.infinity_polling()



