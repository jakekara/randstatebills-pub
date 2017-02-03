from random_bill import random_bill
from bill_details import bill_detail

max_tweet = 140
url_len = 25

def state(bill):
    return bill["state"]

def session(bill):
    return bill["session"]
    
def links(bill):
    return bill["sources"]

def title(bill):
    return bill["title"]

def web_source(bill):
    sources = links(bill)

    for obj in sources:
        if str(obj["url"].upper()).startswith("HTTP"):
            return obj["url"]

    return None
        
def random_bill_detail(state=None, require_web_source=True, tries=0):

    bill = bill_detail(random_bill(state=state))

    if require_web_source == False:
        return bill

    # check that bill has a source with http in it
    if web_source(bill) == None:
        if tries < 5:
            return random_bill_detail(state = state,
                                      tries = tries + 1)
        else:
            raise Exception("Cannot find bill with web source URL.")
        
    return bill

def sentence(txt):
    if len(txt) <= 0:
        return txt
    
    lower = txt.lower()
    lower = lower[0].upper() + lower[1:]
    return lower

def hashtag(bill):
    return "#RandomBills" + state(bill).upper()

def trunc(txt, max_len=None):
    if max_len == None:
        max_len = max_tweet (1 + url_len)

    if (len(txt) <= max_len):
        return txt

    elipses = "..."

    max_len -= len(elipses)

    return txt[:max_len] + elipses

def tweet(state=None):

    tweet_text = ""
    chars_left = max_tweet
    
    bill = random_bill_detail(state=state)

    # Add the hastag
    tag = hashtag(bill)
    tag_len = len(tag)
    tweet_text += " " + tag
    chars_left -= (1 + tag_len)

    # Add the link
    tweet_text += " " + web_source(bill)
    chars_left -= (1 + url_len)

    # Add the truncated bill title
    text = trunc(sentence(title(bill)),
                       max_len=chars_left)
    tweet_text = text + tweet_text
    chars_left -= len(text)

    # print ("CHARS LEFT: " + str(chars_left))
    # print ("SESSION YR: " + str(session(bill)))
    return tweet_text
    

