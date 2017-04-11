Twilio Wrapper Python Library For thinQ LCR integration
=========================================================================

**Note that you will need a valid LCR Account with thinQ before using the libraries. For more information please contact your thinQ Sales representative at http://www.thinq.com**
----------------------------------------------------------------------------------------------------------------

To use with version 5.X of Twilio's SDK, simply do:

    >>> from twilio_thinQLCR_python import TwilioWrapper
    >>> wrapper = TwilioWrapper(twilio_account_sid, twilio_auth_token, thinQ_id, thinQ_token)
    >>> call = wrapper.call("1234567890", "9876543210", "http://example.com/twilio.xml")
    >>> print "Call sid: " + str(call.sid)
