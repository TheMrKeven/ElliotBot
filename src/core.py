import time
import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from src.config.settings import TELEGRAM_TOKEN, MSG_BOAS_VINDAS, \
    MSG_REGRAS, URL_BOT, MSG_LINK_CANAL, MSG_LINK_CURSO, MSG_ALERT_CTF, \
    PRINT_EVENTS

__bot = telebot.TeleBot(TELEGRAM_TOKEN)

def get_admin_ids(chat_id):
    return [admin.user.id for admin in __bot.get_chat_administrators(chat_id)]

def rules_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("Regras", url=URL_BOT))
    return markup


def listener(messages):
    for m in messages:
        print(str(PRINT_EVENTS).format(
            m.chat.id,
            m.chat.title,
            m.from_user.id,
            m.from_user.first_name + " " + m.from_user.last_name,
            m.text,
            m.content_type
        ))
        file.write(str(m) + "\n")
        file.flush()


def user_format(message):
    if message.new_chat_member.username is None:
        return "{}".format(message.new_chat_member.first_name)
    else:
        return"@{}".format(message.new_chat_member.username)

@__bot.message_handler(commands=['start', 'rules'])
def send_welcome(message):
    if message.chat.type == 'private':
        __bot.reply_to(message, MSG_REGRAS)
    elif (message.chat.type == 'supergroup'):
        admin = get_admin_ids(message.chat.id)
        if (message.from_user.id in admin and
                message.text != "/start"):
            __bot.reply_to(message, "Regras do Grupo", reply_markup=rules_markup())

@__bot.message_handler(commands=['ban'])
def ban_user(message):
    if message.chat.type == 'supergroup':
        admin = get_admin_ids(message.chat.id)
        if (message.from_user.id in admin and
                message.reply_to_message != None):
            __bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id)

@__bot.message_handler(func=lambda m: True, content_types=['new_chat_members'])
def reply_msg(message):
    username = user_format(message)
    __bot.reply_to(message, MSG_BOAS_VINDAS.format(
        name=message.new_chat_member.first_name,
        username = username,
        id=message.new_chat_member.id
    ), reply_markup=rules_markup(), parse_mode='markdown')

@__bot.message_handler(commands=['canal'])
def send_canal(message):
    __bot.reply_to(message, MSG_LINK_CANAL)

@__bot.message_handler(commands=['curso'])
def send_curso(message):
    __bot.reply_to(message, MSG_LINK_CURSO)

@__bot.message_handler(commands=['ctf'])
def send_alert_ctf (message):
    __bot.reply_to(message, MSG_ALERT_CTF)

if __name__ == '__main__':
    print("Aperte CTRL + C para cancelar.")
    __bot.set_update_listener(listener)
    while True:
        try:
            file = open(".log", "a")
            __bot.polling(none_stop=True)
            file.close()
        except Exception:
            time.sleep(15)