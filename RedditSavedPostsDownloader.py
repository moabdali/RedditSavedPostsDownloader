# Made by Mo Ab
# IMPORTANT: This program will not run "as is".  You have to provide your
# own API secret key and reddit log-in info.  Since it's private info, I
# put in placeholders.  Use this video to learn how to get your own secret
# key for your account.  https://www.youtube.com/watch?v=6Pie-uoDYG4 I assume 
# you have a reddit account if you're using this program anyway since the whole 
# point of it is to download your own saved posts.  It won't give you access to 
# anyone else's since it's private info. 
# Note: if your saved file loads for a split second and then turns white, it's
# because your pop up blocker is misconfigured. Try opening it in a different
# browser and your webpage will load correctly.

import praw  # reddit API
import urllib3  # for downloading websites

# refer to the block of text above if you don't understand what goes here
reddit = praw.Reddit(
    client_id="Your client ID",
    client_secret="PUTYOURAPICODEHERE",
    user_agent="my user agent",
    username="PUTYOURUSERNAMEHERE",
    password="PUTYOURPASSWORDHERE",
)
# enable http
http = urllib3.PoolManager()

# using the reddit API, look at your entire list of saved posts
for link in reddit.user.me().saved(limit=None):
    # the wrapper only returns the ID of the post.  You have to supply the URL yourself
    url = "redd.it/" + str(link)
    # kind of a debug notice, but still nice to know that progress is being made
    print(url)
    # save the website to a variable
    resultingPage = http.request("get", url)
    # save the variable to a text (html) file; make sure to save as bytestream
    with open(str(link) + ".html", "wb") as fileID:
        fileID.write(resultingPage.data)

    print("done with file.")
