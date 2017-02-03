import random

from todays_data import get_bill_list
from my_open_states import meta

def random_state():
    return random.choice(meta())

def random_bill(state=None):

    if state == None:
        state = random_state()
        st = state["abbreviation"]
    else:
        state = meta(state)
        st = state["abbreviation"]

    chamber = random.choice(state["chambers"].keys())
    blist = get_bill_list(st, chamber)
    return random.choice(blist)

