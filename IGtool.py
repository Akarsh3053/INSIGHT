import instaloader
import pandas as pd

# Creating an instance of the Instaloader class
bot = instaloader.Instaloader()

# Loading a profile from an Instagram handle
def get_insta():
    user = input("\n Enter Instagram Username : ")
    profile = instaloader.Profile.from_username(bot.context, user)
    print("\n\n\nUsername: ", profile.username)
    print("User ID: ", profile.userid)
    print("Number of Posts: ", profile.mediacount)
    print("Followers Count: ", profile.followers)
    print("Following Count: ", profile.followees)
    print("Bio: ", profile.biography)
    print("External URL: ", profile.external_url)

