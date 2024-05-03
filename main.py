import praw
import json
import datetime

reddit = praw.Reddit(
    client_id = "aAXuKXHkpglxK4rSy5Sjqw",
    client_secret = "rozvEYfPuTGdaGGySRVtnOgKCR8dxA",
    user_agent = "search engine by u/_HyP3_"
)

ucr_subreddit = reddit.subreddit("ucr")

ucr_top_posts = ucr_subreddit.top(limit=10)
ucr_new_posts = ucr_subreddit.new(limit=10)

def get_date(post):
    time = post.created_utc
    return datetime.datetime.fromtimestamp(time)


for post in ucr_top_posts:
    json_string = '{"Title":"title", "ID":"ID", "Author":"author", "URL":"URL", "Score":"score", "Text":"selfText", "Comments":"commentCount", "Date":"created"}'
    postJSON = json.loads(json_string)
    
    postJSON['Title'] = post.title
    postJSON['ID'] = post.id
    postJSON['Author'] = str(post.author)
    postJSON['URL'] = post.url
    postJSON['Score'] = post.score
    postJSON['Text'] = post.selftext
    postJSON['Comments'] = post.num_comments
    postJSON['Date'] = str(get_date(post))

    newJSON = json.dumps(postJSON, indent=2)
    
    print(newJSON)
    print("\n")

#   post = reddit.submission(id="137u9ki")
#   comments = post.comments

#    for comment in comments[:2]:
#        print("Printing comment...")
#        print("Body - ", comment.body)
#        print("Author -", comment.author)
#        print("\n")