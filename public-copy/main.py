from tweet import tweet as send_tweet
from make_tweet import tweet as form_tweet

def go(state=None):
    msg = form_tweet(state=state)
    try:
        msg = form_tweet(state=state)
    except:
        print "Error forming tweet"
        exit (1)
        
    print "Sending tweet: " + msg

    try:
        pass
        send_tweet(msg)
    except:
        print "Error sending tweet"
        exit(1)


