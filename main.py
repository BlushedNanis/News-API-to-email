from email_function import send_email
from requests import get
from os import getenv
from dotenv import load_dotenv


#Load envioremental variables from .env
load_dotenv()

#Set news parameters, check newsapi.org for more information
category = "general"
country = "mx"
url = (
    "https://newsapi.org/v2/top-headlines?"\
    f"category={category}&"\
    f"country={country}"\
    f"&apiKey={getenv("api_key")}"
    )

#Make a request
request = get(url)

#Obtain a dictionary from the request
content = request.json()

#Set Subject for the email
message = "Subject: Today's News\n"

#Extract the information from the dictionary 
#and add it to the message
for article in content["articles"]:
    message += f"""
    {article["author"]} - {str(article["publishedAt"][:10])}
    {article["title"]}
    {article["description"]}
    {article["url"]}\n"""

send_email(message.encode())