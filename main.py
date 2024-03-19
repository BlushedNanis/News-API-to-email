from email_function import send_email
from requests import get
from os import getenv
from dotenv import load_dotenv


#Load envioremental variables from .env
load_dotenv()

#Make a request
request = get(getenv("url"))

#Obtain a dictionary from the request
content = request.json()

#Set Subject for the email
message = "Subject: Today's News\n"

#Extract the information from the dictionary 
#and add it to the message
for article in content["articles"]:
    message += f"""
    {article["author"]} - {str(article["publishedAt"][:10])}
    {article["description"]}
    {article["title"]}
    {article["url"]}"""

send_email(message.encode())