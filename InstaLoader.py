"""""
from instaloader import Hashtag, Instaloader
from datetime import datetime
from itertools import dropwhile, takewhile

L = Instaloader()
HASHTAG = 'urbanphotography'

posts = Hashtag.from_name(L.context, HASHTAG).get_posts()

SINCE = datetime(2015,  3, 1)
UNTIL = datetime(2015, 5, 1)

# hashtag.get_top_posts()

for post in takewhile(lambda p: p.date > UNTIL, dropwhile(lambda p: p.date > SINCE, posts)):
    print(post.date)
    # L.download_post(post, target="#" + posts.name)
    L.download_post(post, '#urbanphotography')
"""

from datetime import datetime
from itertools import dropwhile, takewhile

import instaloader
L = instaloader.Instaloader()

posts = instaloader.Hashtag.from_name(L.context, 'blacklivesmatter').get_posts()
# or
# posts = instaloader.Profile.from_username(L.context, PROFILE).get_posts()

SINCE = datetime(2020, 6, 10)
UNTIL = datetime(2020, 6, 6)

for post in takewhile(lambda p: p.date > UNTIL, dropwhile(lambda p: p.date > SINCE, posts)):
    print(post.date)
    L.download_post(post, '#blacklivesmatter')

