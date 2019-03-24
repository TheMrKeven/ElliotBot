import os
from src.config.messages import MSG_BOAS_VINDAS, MSG_REGRAS, \
    MSG_LINK_CANAL, MSG_LINK_CURSO, MSG_ALERT_CTF, PRINT_EVENTS
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
URL_BOT = str(os.getenv("URL_BOT"))
MSG_LINK_CANAL = MSG_LINK_CANAL
MSG_LINK_CURSO = MSG_LINK_CURSO
MSG_ALERT_CTF = MSG_ALERT_CTF.format(no_entry_sign= u'\U0001F6AB', x=u'\U0000274C')
MSG_BOAS_VINDAS = MSG_BOAS_VINDAS
MSG_REGRAS = MSG_REGRAS.format(no_entry_sign = u'\U0001F6AB')
PRINT_EVENTS = PRINT_EVENTS