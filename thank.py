import requests
from bs4 import BeautifulSoup
outputs = []

def process_message(data):
    #print(data['text'].lower()) 
    #words that will make calcium-bot respond
    keywords = ['calcium', 'doot', 'skeltal', 'thank', 'skeletal', 'bone', 'me_irl', 'me irl', 'meirl']
    text = data['text'].lower()
    if any(x in text for x in keywords):
        #gets a random page from ledootgeneration and then gets the link and title from it
        r = requests.get("https://www.reddit.com/r/ledootgeneration/random", headers = {'User-agent': 'calcium-bot'})
        soup = BeautifulSoup(r.text, 'html.parser')
        a = soup.findAll("a", { "class" : "title" })[0]
        link = a.get('href')
        title = a.string 
        #send the title and link to whatever channel said the keyword
        outputs.append([data['channel'], "{}\n{}".format(title, link)])
