from twilio.rest import TwilioRestClient
import sys

class TwilioWrapper:
    THINQ_DOMAIN = "wap.thinq.com"
	TWIML_RESOURCE_URL = "http://demo.twilio.com/docs/voice.xml"

	def __init__(self, twilio_account_sid, twilio_account_token, thinQ_id, thinQ_token):
		self.twilio_account_sid = twilio_account_sid
		self.twilio_account_token = twilio_account_token
		self.thinQ_id = thinQ_id
        self.thinQ_token = thinQ_token
		self.client = TwilioRestClient(twilio_account_sid, twilio_account_token)

	def isClientValid(self):
		return (not self.client is None)

	def call(self, from, to):
		if not self.isClientValid():
			return "Invalid Twilio Account details."
		try:
			call = self.client.calls.create(url=TwilioWrapper.TWIML_RESOURCE_URL,
				to="sip:" + to + "@"+TwilioWrapper.THINQ_DOMAIN+"?thinQid="+self.thinQ_id+"&thinQtoken="+self.thinQ_token,
				from_=from)
			return call.sid
		except:
			return sys.exc_info()[0]

	# def test_call(self):
	# 	client.calls.create(url="http://demo.twilio.com/docs/voice.xml",
	# 		to=self.customer_number,
	# 		from_=self.twilio_phone_number)

