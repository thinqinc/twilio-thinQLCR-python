from twilio.rest import Client
import sys

class TwilioWrapper:
  THINQ_DOMAIN = "wap.thinq.com"
  TWIML_RESOURCE_URL = "http://demo.twilio.com/docs/voice.xml"

  def __init__(self, twilio_account_sid, twilio_account_token, thinQ_id, thinQ_token):
    self.twilio_account_sid = twilio_account_sid
    self.twilio_account_token = twilio_account_token
    self.thinQ_id = thinQ_id
    self.thinQ_token = thinQ_token
    self.client = Client(twilio_account_sid, twilio_account_token)

  def isClientValid(self):
    return (not self.client is None)

  def call(self, to, _from, twiml=None):
    if not self.isClientValid():
      return "Invalid Twilio Account details."
    if twiml is None:
    	twiml = TwilioWrapper.TWIML_RESOURCE_URL
    try:
      call = self.client.calls.create(
        to="sip:" + to + "@"+TwilioWrapper.THINQ_DOMAIN+"?thinQid="+self.thinQ_id+"&thinQtoken="+self.thinQ_token,
        from_=_from,
        url=twiml)
      return call
    except:
      return sys.exc_info()[0]
