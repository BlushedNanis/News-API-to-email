from smtplib import SMTP_SSL
from ssl import create_default_context
from os import getenv
from dotenv import load_dotenv


load_dotenv()

def send_email(email_body:str):
    """
    Send an Email using a SMTP_SSL instance
    with the given enviromental variables for the sender
    and reciever email.

    Args:
        email_body (str): Message for the email, 
        in case of special characters it must be encoded in utf-8
    """
    with SMTP_SSL("smtp.gmail.com", 
                  context=create_default_context()) as server:
        server.login(getenv("email"), getenv("pypass"))
        server.sendmail(getenv("email"), getenv("reciever"), email_body)
        
if __name__ == "__main__":
    message = "Subject: E-mail function tests\n\nThis is an e-mail test"
    send_email(message)