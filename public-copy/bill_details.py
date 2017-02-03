# from sunlight import openstates, config
from my_open_states import bill_detail as bd
import env

# config.API_KEY = env.API_KEY

def bill_detail(bill):
    return bd(
        bill["state"],
        bill["session"],
        bill["bill_id"])
        
