from donbot import Donbot
import sys
import re

class Prodbot(Donbot):
    def __init__(self, username, password, thread=None, postdelay=1.5):
        super().__init__(username, password, thread, postdelay)
        self.overview_data = self.getActivityOverview()

    def sendProds(self, days_until_prod, prod_subject, prod_body):
        prod_recipients = []
        for i in self.overview_data:
            # Find the first consucutive string of digits in the
            # 'sincelast' field of the activity overview list items
            days_since_last = int(re.match('\d+', i['sincelast']).group(0))

            if days_since_last >= days_until_prod:
                prod_recipients.append(i['user'])

        self.sendPM(prod_subject, prod_body, prod_recipients)
