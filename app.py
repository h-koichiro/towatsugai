from flask import Flask, request, abort, render_template, redirect
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

def txt_r():
    f = open('state.txt', 'r', encoding='UTF-8')
    STATE = f.read()
    f.close()
    return STATE

def txt_w(state):
    f = open('state.txt', 'w', encoding='UTF-8')
    f.write(state)
    f.close()

@app.route('/')
def index():
    state = txt_r()
    print(state)
    return render_template("index.html", state=state)


line_bot_api = LineBotApi("jlgmsj1CCoCWSLh491ILVZxpJNLsqSoyFrgbXTFjmnBcMuQqaRm6sUQOqwLVav/c8zFzeZNSg3UDLHVBKqj4gRsMw/ZHH1q4YP0W1IKX8PpihfKA3PCibwbys1hr8inEjDZaNjYgOZ5TKErIZ/8bDAdB04t89/1O/w1cDnyilFU=")
handler = WebhookHandler("644c830373e830f0a682507bc73b23e6")
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
    # line_bot_api.reply_message(
    #     event.reply_token,
    #     TextSendMessage(text=event.message.text))
    txt_w(event.message.text)
    return redirect("/")

@app.route('/')
def index():
    return render_template("index.html", state=txt_r())


if __name__ == "__main__":
    app.run()
