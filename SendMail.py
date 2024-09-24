import yagmail
import os
from dotenv import looad_dotenv

load_dotenv()



sender = "amarooplab@gmail.com"
receiver = "gjzbpkxzi@emltmp.com"
subject = 'Test mail using python'
contents = ''''''
this is the content side for sending mail
''''''

yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))
yag.send(to=receiver, subject=subject, contents=contents)
print("Email send!")
