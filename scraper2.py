import json
from facebook_scraper import get_posts

# Set the group ID and access token
GROUP_ID = "37493541545"
MAX_COMMENTS = 100
PAGES = 10
#access_token = "access_token_here"

# Create lists to store the comments and reactors
comments_list = []
reactors_list = []
posts_list = []
posts_full = []

# Loop through the posts in the group
#for post in get_posts(group=group_id, access_token=access_token, pages=10):
for post in get_posts(group=GROUP_ID, pages=PAGES, options={"comments": MAX_COMMENTS, "reactors": True, "progress": True}):

    posts_full.append({"post_id": post["post_id"], "post": post})
    posts_list.append({'post_id': post["post_id"], "post_user_id": post['user_id'], "post_username":post['username'], "post_text": post['text'], "post_time": post['time'], "post_likes": post['likes'], "comment_count": post['comments']})

    # Get the comments on the post
    post_comments = post["comments_full"]
    
    # Loop through the comments and add them to the comments list
    for comment in post_comments:
        comments_list.append({"post_id": post["post_id"], "commenter_name": comment["commenter_name"], "commenter_id": comment["commenter_url"], "comment_text": comment["comment_text"]})
    
    # Get the reactors on the post
    reactors = post["reactions"]
    
    if reactors is not None:
        # Loop through the reactors and add them to the reactors list
        for reactor in reactors:
            reactors_list.append({"post_id": post["post_id"], "reactor_name": reactor["name"], "reactor_id": reactor["id"]})

# Save the comments and reactors lists as JSON files
with open("comments.json", "w") as comments_file:
    json.dump(comments_list, comments_file, indent=4, sort_keys=True, default=str)

with open("reactors.json", "w") as reactors_file:
    json.dump(reactors_list, reactors_file, indent=4, sort_keys=True, default=str)

with open("posts.json","w") as posts_file:
    json.dump(posts_list, posts_file, indent=4, sort_keys=True, default=str)
    

with open("posts_full.json","w") as posts_full_file:
    json.dump(posts_full, posts_full_file, indent=4, sort_keys=True, default=str)