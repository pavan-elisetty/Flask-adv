import os
from typing import List
from requests import Response , post

FAILED_LOAD_API_KEY = "failed to load the mailgun api key"
FAILED_LOAD_DOMAIN="failed to load the mailgun domain"
ERROR_SENDING_EMAIL =  "Error in sending email,user registration failed"

class MailGunException(Exception):
    def __init__(self,message:str):
        super().__init__(message)



class Mailgun:
    MAILGUN_DOMAIN=os.environ.get("MAILGUN_DOMIAN")
    MAILGUN_API_KEY = os.environ.get("MAILGUN_API_KEY")
    FROM_TITLE ="Stores Rest Api"
    FROM_EMAIL = "postmaster@sandboxb15634d530bb43f5bb340ae9f6a3b8c1.mailgun.org"

    @classmethod
    def send_confirmation_email(cls,email:List[str],subject:str,text,html:str) -> Response:
        if cls.MAILGUN_API_KEY is None:
            raise MailGunException(FAILED_LOAD_API_KEY)
        if cls.MAILGUN_DOMAIN is None:
            raise MailGunException(FAILED_LOAD_DOMAIN)

        response= post(
            f"https://api.mailgun.net/v3/{cls.MAILGUN_DOMAIN}/messages",
            auth=("api", cls.MAILGUN_API_KEY),
            data={
                "from": f"{cls.FROM_TITLE} <{cls.FROM_EMAIL}>",
                "to": email,
                "subject": subject,
                "text": text,
                "html":html
            },
        )

        if response.status_code !=200:
            raise MailGunException(ERROR_SENDING_EMAIL)
        return response


