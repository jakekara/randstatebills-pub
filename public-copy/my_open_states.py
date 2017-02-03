import env, requests
import random

url = "https://openstates.org/api/v1/"

def request(add_on):

    if "?" in add_on:
        api_add_on = "&"
    else:
        api_add_on = "?"

    api_add_on += "api_key=env.API_KEY"

    add_on += api_add_on
    
    resp = requests.get(url + add_on)

    if resp.status_code != 200:
        print url + add_on
        raise Exception("request failed. status code: " + str(resp.status_code))

    return resp.json()

def meta(state=None):
    if state == None:
        return request("metadata/")

    return request("metadata/" + state)

def bill_list(state, chamber):
    add_on = "bills/"
    add_on += "?state=" + state
    add_on += "&chamber=" + chamber
    add_on += "&search_window=session"

    return request(add_on)

def bill_detail(state, session, bill_id):
    add_on = "bills/"
    add_on += state + "/"
    add_on += session + "/"
    add_on += bill_id 

    return request(add_on)

# bill =  random.choice(bill_list("ct","lower"))
# print bill
# print bill_detail(bill["state"],
#                   bill["session"],
#                   bill["bill_id"])

# print random.choice(meta());
