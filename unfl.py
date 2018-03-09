# This script is used to remove everyone you follow, but doesn't follow you back, on Instagram
# Set IG_USERNAME and IG_PASSWORD environment variables before running
# Unix example: IG_USERNAME='username' IG_PASSWORD='password' python3 unfl.py

import time
import os
import pprint
from InstagramAPI import InstagramAPI


def main():
    pp = pprint.PrettyPrinter()
    ig_handler = InstagramAPI(os.environ["IG_USERNAME"], os.environ["IG_PASSWORD"])
    if ig_handler.login():
        followers = []
        following = []
        followers_names = []
        following_names = []
        tbd = []
        ig_handler.getSelfUserFollowers()
        for user in ig_handler.LastJson['users']:
            followers_names.append(user['username'])
            followers.append(user)
        ig_handler.getSelfUsersFollowing()
        for user in ig_handler.LastJson['users']:
            following_names.append(user['username'])
            following.append(user)
        print("followers: {}".format(followers_names))
        print("following: {}".format(following_names))
        for user_name in following_names:
            if user_name not in followers_names:
                tbd.append(user_name)
        print("tbd: {}".format(tbd))
        for user_name in tbd:
            for user in following:
                if user['username'] == user_name:
                    print("Found: ")
                    pp.pprint(user)
                    print("unfollowing user...")
                    ig_handler.unfollow(user['pk'])
                    time.sleep(3)
    else:
        print("Can't login!")

if __name__ == "__main__":
    main()


