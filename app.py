from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

ACCESS_TOKEN = "W4yKr2DpVZXhU6rWnXM+Y/fXgHBsYuOCbSEbOPARRQxp+Ke9A4jyuuYh4kkIDiRj8zFzeZNSg3UDLHVBKqj4gRsMw/ZHH1q4YP0W1IKX8PpagZ6L3gTjApD9jDvuUlUnUodpzECNCdAKmEbRMWJUKQdB04t89/1O/w1cDnyilFU="
SECRET = "644c830373e830f0a682507bc73b23e6"

line_bot_api = LineBotApi(ACCESS_TOKEN)
handler = WebhookHandler(SECRET)

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))

if __name__ == "__main__":
    app.run()
