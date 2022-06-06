from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

#============呼叫的檔案內容=====
from message import *


#======python的函數庫==========
import tempfile, os
import datetime
import time
#====Line bot setting==========

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token
line_bot_api = LineBotApi('ZsDxA+s/eAEl36MVqxcwnigazVpsfRSOwtl6elkmebDgHDhoKeT/odkUNO6hqLoVAvIrMAUUzfDfyGeYO8pWi7D0L4TWIvK726rDjl0XeIjUTZsfp0x4I1FniCNFYgumiiwPWX5fU5qFBxm3rbiLJQdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('c0694b3b94744270cfc70b524b2a59e7')

#================
# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


# 處理一般訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    try:
        if '吃什麼' in msg or 'recommend'in msg or 'Recommend'in msg or 'RECOMMEND'in msg or '喝什麼' in msg or '推薦' in msg:
            flex_message = TextSendMessage(text="想知道哪裡的推薦美食呢？Where?",
                                           quick_reply=QuickReply(items=[
                                               QuickReplyButton(action=PostbackAction(label='市區Downtown', text='市區Downtown', data='L&市區')), #data的目的是為了Postback (可以連續對話)
                                               QuickReplyButton(action=PostbackAction(label='清夜NTHU Night Market', text='清夜NTHU Night Market', data='L&清夜')),
                                           ]))
            line_bot_api.reply_message(event.reply_token, flex_message)

    except Error as e:
        print(e)


#處理Postback訊息
@handler.add(PostbackEvent)
def handle_message(event):
    reply_msg = event.postback.data
    if reply_msg[0:2] == 'L&':
        area = reply_msg[2:]
        flex_message = TextSendMessage(text="想知道什麼類別的推薦美食呢？What type?",
                                       quick_reply=QuickReply(items=[
                                           QuickReplyButton(action=PostbackAction(label='Breakfast', text='Breakfast',data='B&' + area + '&Breakfast')),  #label不能超過20個字
                                           QuickReplyButton(action=PostbackAction(label='Lunch/Dinner', text='Lunch/Dinner', data='B&'+area+'&Lunch/Dinner')),
                                           QuickReplyButton(action=PostbackAction(label='Drink', text='Drink', data='B&'+area+'&Drink')),
                                           QuickReplyButton(action=PostbackAction(label='Cafe', text='Cafe', data='B&' + area + '&Cafe'))
                                       ]))

        line_bot_api.reply_message(event.reply_token, flex_message)
    elif reply_msg[0:2] =='B&':
        result = reply_msg[2:].split('&')
        area = result[0]
        type = result[1]
        if area =='清夜':
            if type == 'Lunch/Dinner':
                message = Tsing_Dinner_Carousel()
                line_bot_api.reply_message(event.reply_token, message)
            elif type =='Breakfast':
                message = Tsing_Break_Carousel()
                line_bot_api.reply_message(event.reply_token, message)
            elif type == 'Cafe':
                message = Tsing_Coffee_Carousel()
                line_bot_api.reply_message(event.reply_token, message)
            elif type == 'Drink':
                message = Tsing_Drink_Carousel()
                line_bot_api.reply_message(event.reply_token, message)
        elif area =='市區':
            if type == 'Lunch/Dinner':
                message = City_Dinner_Carousel()
                line_bot_api.reply_message(event.reply_token, message)
            elif type =='Breakfast':
                message = City_Break_Carousel()
                line_bot_api.reply_message(event.reply_token, message)
            elif type == 'Cafe':
                message = City_Coffee_Carousel()
                line_bot_api.reply_message(event.reply_token, message)
            elif type == 'Drink':
                message = City_Drink_Carousel()
                line_bot_api.reply_message(event.reply_token, message)

    else:
        reply_arr = []
        reply_arr.append(TextSendMessage(text='Good choice! Hope you like it:)')) #文字
        reply_arr.append(StickerSendMessage(package_id='6362', sticker_id='11087922')) #貼圖(在line developer有代號)
        line_bot_api.reply_message(event.reply_token, reply_arr)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

#=====
#美食選單
#https://www.learncodewithmike.com/2020/07/line-bot-buttons-template-message.html