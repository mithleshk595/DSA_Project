from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/bot", methods=['POST'])
def whatsapp_bot():
    # User ka message nikalna
    user_msg = request.values.get('Body', '').lower()
    response = MessagingResponse()
    msg = response.message()

    # Logic: Agar user 'hi' bole toh kya reply kare
    if 'hi' in user_msg:
        msg.body("Hello! Main aapka Python chatbot hoon. Kaise madad karu?")
    elif 'date' in user_msg:
        from datetime import datetime
        msg.body(f"Aaj ki date hai: {datetime.now().strftime('%d-%m-%Y')}")
    else:
        msg.body("Maaf kijiye, mujhe sirf 'hi' aur 'date' samajh aata hai!")

    return str(response)

if __name__ == "__main__":
    app.run(port=5000)