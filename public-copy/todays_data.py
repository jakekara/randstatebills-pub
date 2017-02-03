# from sunlight import openstates, config
from datetime import datetime
from my_open_states import bill_list
import env, json, os

def today():
    return datetime.today().strftime("%Y-%m-%d")

def base_path(state):
    return os.path.join(env.DATA_PATH,
                        state)

def archive_fname(chamber, date=None):
    if date == None:
        date = today()
        
    return chamber + "-" + date + ".json"

def current_fname(chamber):
    return archive_fname(chamber)

def write_json(obj,path):
    fh = open(path,'wb')
    fh.write(json.dumps(obj))
    fh.close()

def exists(path):
    return os.path.exists(path)

def makedir(path):
    if not os.path.exists(path):
        os.makedirs(path)
    
def save_json(obj,state, chamber):

    path = base_path(state)
    makedir(path)
    makedir(os.path.join(path, chamber))
    # Save the current version
    write_json(obj,
               os.path.join(path,
                            current_fname(chamber)))
               
    # Save the archive copy
    write_json(obj,
               os.path.join(path,
                           chamber,
                           archive_fname(chamber)))

def api_get_bill_list(state, chamber):

    try:
        ret = bill_list(state, chamber)
    except:
        print ":( Crap. Request failed"
        exit(1)

    return ret


def file_get_bill_list(file_path):
    
    if exists(file_path):
        return json.loads(open(file_path,'r').read())

    return None
    
# Get bill list remotely, or from disk if file exists
# use force=True to force fetching of new data
def get_bill_list(state, chamber, force=False):

    # Check for file on disk
    file_path = os.path.join(
        base_path(state),
        current_fname(chamber))

    if force == False:
        blist = file_get_bill_list(file_path)
        if blist != None:
            return blist

    # if it doesn't exist, download it
    bill_list = api_get_bill_list(state, chamber)

    # save current and archive copies
    save_json(bill_list, state, chamber)

    return bill_list
