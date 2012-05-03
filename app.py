import os
from random import randint
import flask
from twilio import twiml
app = flask.Flask(__name__)


@app.route('/sms', methods=['POST'])
def sms():
    response, data, dice, sides = twiml.Response(), None, None, None
    try:
        dice, sides = flask.request.form['Body'].lower().split('d')
    except:
        response.sms("Thanks for using SMS Dice Bag.  Format query like: 2d6")
    if dice and sides and (int(dice) > 20 or int(sides) > 20):
        response.sms("Easy there tiger.  Let's keep dice and sides under 20.")
    elif dice and sides:
        data = [randint(1, int(sides)) for i in range(0, int(dice))]
    if data:
        response.sms("Total: %s  Rolls: %s" % (str(sum(data)), str(data)))
    return str(response)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
