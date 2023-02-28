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
import os
app = Flask(__name__)
#環境変数取得
line_bot_api = LineBotApi("jlgmsj1CCoCWSLh491ILVZxpJNLsqSoyFrgbXTFjmnBcMuQqaRm6sUQOqwLVav/c8zFzeZNSg3UDLHVBKqj4gRsMw/ZHH1q4YP0W1IKX8PpihfKA3PCibwbys1hr8inEjDZaNjYgOZ5TKErIZ/8bDAdB04t89/1O/w1cDnyilFU=")
handler = WebhookHandler("644c830373e830f0a682507bc73b23e6")
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
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


@app.route('/')
def index():
    return ("ｂｂｂｂｂ")
if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
    app.run()
#     port = int(os.getenv("PORT", 5000))
#     app.run(host="0.0.0.0", port=port)
