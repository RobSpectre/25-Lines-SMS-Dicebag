import unittest
from .context import app


class TwiMLTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def assertTwiML(self, response):
        self.assertTrue("<Response>" in response.data, "Did not find " \
                "<Response>: %s" % response.data)
        self.assertTrue("</Response>" in response.data, "Did not find " \
                "</Response>: %s" % response.data)
        self.assertEqual("200 OK", response.status)

    def sms(self, body, path='/sms', number='+15555555555'):
        params = {
            'SmsSid': 'SMtesting',
            'AccountSid': 'ACtesting',
            'From': number,
            'To': '+16666666666',
            'Body': body,
            'ApiVersion': '2010-04-01',
            'Direction': 'inbound',
            'FromCity': 'BROOKLYN',
            'FromState': 'NY',
            'FromZip': '11211'}
        return self.app.post(path, data=params)

    def call(self, path='/voice', number='+15555555555', digits=None):
        params = {
            'CallSid': 'CAtesting',
            'AccountSid': 'ACtesting',
            'From': number,
            'To': '+16666666666',
            'CallStatus': 'ringing',
            'ApiVersion': '2010-04-01',
            'Direction': 'inbound'}
        if digits:
            params['Digits'] = digits
        return self.app.post(path, data=params)


class DicebagTests(TwiMLTest):
    def test_sms(self):
        response = self.sms("2d6")
        self.assertTwiML(response)
        self.assertTrue("Total" in response.data, "App did not return " \
                "dice roll, instead: %s" % response.data)
    
    def test_smsWrongFormat(self):
        response = self.sms("3x6")
        self.assertTwiML(response)
        self.assertTrue("Thanks" in response.data, "App did not return " \
                "error text, instead: %s" % response.data)

    def test_smsTooManyDice(self):
        response = self.sms("10000d10")
        self.assertTwiML(response)
        self.assertTrue("Easy there tiger" in response.data, "App did not " \
                "return error text, instead: %s" % response.data)

    def test_smsWTFInput(self):
        response = self.sms("sko-diddly!")
        self.assertTwiML(response)
        self.assertTrue("Thanks" in response.data, "App did not return " \
                "error text, instead: %s" % response.data)
