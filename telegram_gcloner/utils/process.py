#!/usr/bin/python3
# -*- coding: utf-8 -*-
import html
import logging


from telegram import ParseMode
from telegram.utils.helpers import mention_html

from utils.config_loader import config

logger = logging.getLogger(__name__)


def leave_chat_from_message(message, context):
    context.bot.send_message(chat_id=message.chat_id,
                             text='Hey, thank you for adding ⚡️ CloneBot to this group. ' + config.AS_STRING.format(context.bot.username),
                             parse_mode=ParseMode.HTML)
    context.bot.send_message(chat_id=message.chat_id, text='\n\nUnfortunately I am not allowed to be here 😔 \nIf you want me in this group, ask my owner to authorize me 😉.')
    if message.from_user:
        mention_html_from_user = mention_html(message.from_user.id,
                                              message.from_user.full_name.full_name)
        text = '🔙 Left unauthorized group : \n │ Name : {} ({}). \n │ Added by : {} {}. \n │ Message : {}'.format(
            html.escape(message.chat.title),
            message.chat_id,
            mention_html_from_user,
            message.from_user.id,
            message.text)
    else:
        text = '🔙 Left unauthorized group : \n │ Name : {} ({}). \n │ Message : {}'.format(
            html.escape(message.chat.title),
            message.chat_id,
            message.text)
    context.bot.leave_chat(message.chat_id)
    logger.warning(text)
    context.bot.send_message(chat_id=config.USER_IDS[0], text=text, parse_mode=ParseMode.HTML)
