import pandas as pd
import requests
import json
import datetime
import csv
"""
    Name: Amie Kong
    Description: Python program to gather Reddit Submissions for r/abuse &
    r/domesticviolence using Pushshift's API and storing them into a CSV format
    to be further processed for data analysis.
    Resources: https://www.jcchouinard.com/how-to-use-reddit-api-with-python/
"""


"""
    Takes the URL with the given parameters:
        size — increase limit of returned entries to 1000
        after — where to start the search (converted in Unix timestamp)
        before — where to end the search (converted in Unix timestamp)
        query — to search only within the submission’s title
        sub (subreddit) — to narrow it down to a particular subreddit

    It also accesses the URL through the requests module, while using JSON
    module to collect the text of the url page, so that we can preprocess the
    data further using Python.
"""
def get_pushshift_data(after, before, sub):
    url = 'https://api.pushshift.io/reddit/search/submission/?&after='+str(after)+'&before='+str(before)+'&subreddit='+str(sub)+'&sort=asc&sort_type=created_utc'
    print(url)
    r = requests.get(url)
    data = json.loads(r.text, strict=False)
    return data['data']


"""
    Stores the data points as it is extracted through the JSON inputs.
    'subData' holds all of the data in a list which is then added to the global
    dictionary of 'subStats'.
"""
def collect_subData(subm):
    subData = list() #list to store data points
    title = subm['title']
    url = subm['url']
    try:
        flair = subm['link_flair_text']
    except KeyError:
        flair = "NaN"
    try:
        # returns the body of the posts
        body = subm['selftext']
    except KeyError:
        body = ''
    author = subm['author']
    subId = subm['id']
    score = subm['score']
    created = datetime.datetime.fromtimestamp(subm['created_utc']) #1520561700.0
    numComms = subm['num_comments']
    permalink = subm['permalink']

    subData.append((subId,title,body,url,author,score,created,numComms,permalink,flair))
    subStats[subId] = subData


"""
    Uploads the data stored in 'subStats' into a CSV file for further
    data processing.
"""
def update_subFile():
    upload_count = 0
    location = "subreddit_data_uncleaned/"
    print("input filename of submission file, please add .csv")
    filename = input()
    file = location + filename
    with open(file, 'w', newline='', encoding='utf-8') as file:
        a = csv.writer(file, delimiter=',')
        headers = ["Post ID","Title","Body","Url","Author","Score","Publish Date","Total No. of Comments","Permalink","Flair"]
        a.writerow(headers)
        for sub in subStats:
            a.writerow(subStats[sub][0])
            upload_count+=1

        print(str(upload_count) + " submissions have been uploaded into a csv file")

#global dictionary to hold 'subData'
subStats = {}
#tracks no. of submissions
subCount = 0
#Subreddit to query
sub='homeless'
# Unix timestamp of date to crawl from.
# 2019/11/01
# 2020/05/01
before = "1598918400"
# 2018/11/01
# 2020/01/15
after = "1579046400"

data = get_pushshift_data(after, before, sub)

while len(data) > 0:
    for submission in data:
        collect_subData(submission)
        subCount+=1
    # Calls getPushshiftData() with the created date of the last submission
    print(len(data))
    print(str(datetime.datetime.fromtimestamp(data[-1]['created_utc'])))
    after = data[-1]['created_utc']
    data = get_pushshift_data(after, before, sub)

print(len(data))

update_subFile()
