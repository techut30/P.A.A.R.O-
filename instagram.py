import instaloader
import os
import sys


def download_profile_info(username):
    L = instaloader.Instaloader()

    try:

        L.login("your_id", "your_password")
        profile = instaloader.Profile.from_username(L.context, username)
        main_folder = f"{username}_data"
        os.makedirs(main_folder, exist_ok=True)


        L.download_profile(username, profile_pic_only=True)

        for post in profile.get_posts():
            post_folder = os.path.join(main_folder, post.date.strftime("%Y-%m-%d_%H-%M-%S"))
            L.download_post(post, target=post_folder)

        followers_file = os.path.join(main_folder, "followers.txt")
        with open(followers_file, 'w') as file:
            for follower in profile.get_followers():
                file.write(follower.username + '\n')

        following_file = os.path.join(main_folder, "following.txt")
        with open(following_file, 'w') as file:
            for followee in profile.get_followees():
                file.write(followee.username + '\n')

    except instaloader.exceptions.InstaloaderException as e:
        print(f"An error occurred: {e}")

def input(username):
    if username:
        try:
            download_profile_info(username)
        except KeyboardInterrupt:
            print("\nProcess interrupted.")
            sys.exit(0)
    else:
        print("No username provided. Exiting...")
