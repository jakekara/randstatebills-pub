from sunlight import openstates, config
import env, json, random

config.API_KEY = env.API_KEY

meta = openstates.state_metadata(state=env.STATE)

# print (json.dumps(meta,indent=2))

bills_lower = openstates.bills(
    state=env.STATE,
    session=env.SESSION,
    chamber="lower"
    )

# print (json.dumps(bills_lower[:10],indent=2))

first_detail = openstates.bill_detail("ct",
                                      env.SESSION,
                                      random.choice(bills_lower)["bill_id"])


# print (json.dumps(first_detail,indent=2))
print first_detail["title"]
print first_detail["session"]

