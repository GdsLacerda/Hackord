# -*- coding: utf-8 -*-

import os
import time
import sys
import re
from wrinter import wrint
try:
    import mailslurp_client
except ImportError:
    os.system("pip install -r requirements.bin")

p = wrint() # Print Class

class Verify:
    def __init__(self, api_key: str) -> None:
        super(Verify, self).__init__()
        self.configuration = mailslurp_client.Configuration()
        self.configuration.api_key['x-api-key'] = f"{api_key}"



    def ValidateEmail(self, email: str):
        # Validate MailBox
        api_client = mailslurp_client.ApiClient(self.configuration)
        mailserver_controller = mailslurp_client.MailServerControllerApi(api_client)
        verify_options = mailslurp_client.VerifyEmailAddressOptions(email_address=email)
        result = mailserver_controller.verify_email_address(verify_options=verify_options)
        assert result.error is None
        assert result.is_valid is True #DO POPRAWY 


    def CreateEmail(self):
        # Attemting to create mailbox
        try:
            api_client = mailslurp_client.ApiClient(self.configuration)

            # create an inbox using the inbox controller
            api_instance = mailslurp_client.InboxControllerApi(api_client)
            inbox = api_instance.create_inbox()

            # check the id and email_address of the inbox
            if len(inbox.id) > 0:
                return [str(inbox.id), str(inbox.email_address)]
            else:
                p.warning("Unable to create mailbox")
                return "ERROR"
        except:
            p.error("Monthly inbox limit reached! | Try to use different mailslurp account")
            p.handle("Insert new mailslurp API_KEY in settings.cfg")
            p.handle("Due to exception it's unable to generate discord token.")
            time.sleep(100)
            sys.exit()




    def ReceiveEmail(self, mailbox_id: any):
        api_client = mailslurp_client.ApiClient(self.configuration)
        # create two inboxes for testing
        inbox_controller = mailslurp_client.InboxControllerApi(api_client)
        inbox = inbox_controller.get_inbox(mailbox_id)

        # receive email for inbox.id
        waitfor_controller = mailslurp_client.WaitForControllerApi(api_client)
        email1 = waitfor_controller.wait_for_latest_email(inbox_id=inbox.id, timeout=10000, unread_only=True)

        #body = re.sub(r'<.*?>', '', str(email.body))
        while True:
            #p.handle(f"Arrived Email: [ {email1.subject} ]")

            if str(email1.subject) == "Verify Email Address for Discord":
                try:
                    links1 = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', email1.body)
                    #p.info(f"Successfully got links [ {links1} ]")
                    #p.debug(f"Found [{len(links1)}] links in email")

                    discord_links_1 = list()

                    for l1 in links1:
                        if str(l1).startswith("https://click.discord.com"):
                            discord_links_1.append(str(l1))

                    #p.info(f"Links: {discord_links_1}")
                    return discord_links_1[1]
                except Exception as e:
                    print(e)
                    break

            else:
                #p.debug("Waiting for another verification mail")
                inbox_controller2 = mailslurp_client.InboxControllerApi(api_client)
                inbox2 = inbox_controller2.get_inbox(mailbox_id)

                waitfor_controller2 = mailslurp_client.WaitForControllerApi(api_client)
                email2 = waitfor_controller2.wait_for_latest_email(inbox_id=inbox2.id, timeout=10000, unread_only=True)
                try:
                    links2 = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', email2.body)
                    #p.info(f"Successfully got links [ {links2} ]")
                    #p.debug(f"Found [{len(links2)}] links in email")
                    discord_links_2 = list()
                    for l2 in links2:
                        if str(l2).startswith("https://click.discord.com"):
                            discord_links_2.append(str(l2))
                    #p.info(f"Links: {discord_links_2}")
                    return discord_links_2[1]
                except Exception as e:
                    print(e)













#if __name__ == "__main__":
#    Verify("ca478fed360a649c0f89ee56af8116e95ca7f67cbed3906fafbd2d2013b8db2a").ReceiveEmail("2c39a9cb-879b-4793-a3b8-c93e7c69f4db")