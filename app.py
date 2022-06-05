from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('PfUQ7qISV7xaU3gmEfuv5TLguyobnSn8M/4d3XUMNSX77ymBFQzeLO1/epfH2M9Hl4O4IgCRChrta6hyFLesz0Tjt7iqKQ3feGeATxzrPfYo+I77z0CwtMlBFVnHAiHhQJxefRFmZ0p0sZp3xdIVIAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('fedcb3acf4e7a6d47b5b50e03832ec79')


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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = "哈哈哈哈哈哈"

    if msg == '哈':
        r = '嘿'
    elif msg == '呀':
        r = '耶'
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()