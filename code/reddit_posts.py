import requests
import time
import pandas as pd
import numpy as np
import warnings

class RedditPostReader:
    header = {'user-agent': 'anne'}
    post_cols = ['subreddit', 'id', 'selftext', 'title', 'author', 'created', 'ups', 'downs']
  
    post_count = 0
    url=''
   
    def __init__(self):
         pass

   
    def gather_posts(self, url, n=100):

        df = pd.DataFrame(columns=self.post_cols)
        warnings.simplefilter('ignore')
        max_posts = n
        self.url = url
        self.post_count = 0
        empty_count = 0
        after = None
        print(f'Gathering posts from {self.url}')
 
        while True:

            if after == None:
                params = {}
            else:
                params = {'after': after}
            rep = requests.get(self.url, params=params, headers=self.header)
 
            if rep.status_code == 200:
                pjson = rep.json()
                nposts =  len(pjson['data']['children'])  

                for i in range(0, nposts):
                    self_text = [pjson['data']['children'][i]['data']['selftext']]

                    if len(self_text) > 0 and len(self_text[0]) > 0:
                        pdict = {
                            'subreddit' : [pjson['data']['children'][i]['data']['subreddit']],
                            'id' : [pjson['data']['children'][i]['data']['id']],
                            'selftext' : [pjson['data']['children'][i]['data']['selftext']],
                            'title' : [pjson['data']['children'][i]['data']['title']],
                            'author' : [pjson['data']['children'][i]['data']['author']],
                            'created' : [pjson['data']['children'][i]['data']['created']],
                            'ups' : [pjson['data']['children'][i]['data']['ups']],
                            'downs' : [pjson['data']['children'][i]['data']['downs']],
                        }
                        self.post_count += 1
                        if (self.post_count % 500 == 0):
                            print(f'Gathered {self.post_count} posts so far')
                        df2 = pd.DataFrame(pdict)
                        df = df.append(df2, ignore_index=True)
                    else:
                        empty_count += 1
                after = pjson['data']['after']
            else:
                print(rep.status_code)
                break

            if self.post_count < max_posts:
                time.sleep(3)
            else:
                print(f'Gathered {self.post_count} posts')
                print(f'skipped {empty_count} posts with no selftext')
                break
 
        return(df)