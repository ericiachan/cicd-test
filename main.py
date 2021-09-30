import os 
from twilio.rest import Client

ACCOUNT_SID = os.environ['ACCOUNT_SID']
AUTH_TOKEN = os.environ['AUTH_TOKEN']

client = Client(ACCOUNT_SID, AUTH_TOKEN)

message = client.messages.create(
                              body='Update nade to cicd-test repo',
                              from_='whatsapp:+14155238886',
                              to='whatsapp:'+os.environ['TO_WHATSAPP_NUMBER']
                          )

print("Message ID:",message.sid)
