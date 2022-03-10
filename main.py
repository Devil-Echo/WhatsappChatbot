from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse,Body,Message,Redirect
from chatbot import send_response


app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


@app.route("/chatbot", methods=["POST"])
def chatbot():
    # print(request)
    incoming_msg = request.values.get("Body").lower()

    resp = MessagingResponse()
    msg = Message()
    msg.body('Hello World!')
    resp.append(msg)
    #resp.redirect('https://demo.twilio.com/welcome/sms/')

    # msg.body(send_response(incoming_msg))
    # msg.media('https://example.com/path/image.jpg')
    return str(resp)
    

if __name__ == "__main__":
    app.run(debug=True)

