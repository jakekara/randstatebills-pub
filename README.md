# RandStateBills

**Collect and tweet random state bills**

Online live: https://twitter.com/randstatebills

#### Data source: Open States API

Data comes from the [OpenStates API](https://openstates.org/). Originally I
was using
[python-sunlight](https://github.com/sunlightlabs/python-sunlight) to access
it, but I'm not sure that's being updated. For one, the .bills() search
method takes a session keyword that doesn't seem to be supported by the
API. So I wrote my_open_states.py to wrap the few API calls I needed.

#### env.py

env.py.example should be renamed to env.py and filled out with your Twitter
and OpenStates API credentials.

#### Command line utility

To send a single random tweet from the command line us:

```
python util.py [st]

```

st is an optional argument you can use to specify a certain state, but note
that not all states will work (sorry tx). This will only tweet legislation
that has a "source" URL with an HTTP or HTTPS web address. I figure it's
more useful to only tweet stuff people can follow links to.

#### Heroku-ready

This app is running live [twitter](https://twitter.com/randstatebills) via
Heroku. The Procfile is the only Heroku-specific file, but Requirements.txt
is also required by Heroku to deploy. For more on running a Heroku Python
app check out [this
document](https://devcenter.heroku.com/articles/getting-started-with-python#introduction).

Don't be intimidated by Heroku! I was able to figure out how to use it in
10 minutes, and it was a nice change from AWS, which can be pretty
cumbersome for running tiny apps like this.

The clock.py file is what controls the 10-minute interval.

#### About this repo

This repo is automatically generated to shield private files, so it won't
have my real commits. This is not ideal, I know, but I made dozens of
commits before realizing I'd want to publish this code and needed to remove
my API keys.