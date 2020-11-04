#we are going to validate the expiry date of the credit card
from datetime import *
def validatecard(expDate):
    if expDate > datetime.now().date():
        print("valid")
    else:
        print("expired")

validatecard(date(2020,2,2))