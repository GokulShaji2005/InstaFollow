import zipfile
import json

def zipUpload(zipFile):
    following_list = []
    followers_list = []

    with zipfile.ZipFile(zipFile, "r") as z:
        for file in z.namelist():
            if file.endswith(".json"):

                if "following.json" in file:
                    with z.open(file) as f:
                        following = json.load(f)
                        for item in following["relationships_following"]:
                            usernameOfFollowing = item["title"]
                            following_list.append(usernameOfFollowing)

                if "followers_1.json" in file:
                    with z.open(file) as f:
                        followers = json.load(f)
                        for item in followers:
                            usernameOfFollowers = item["string_list_data"][0]["value"]
                            followers_list.append(usernameOfFollowers)

    following_set = set(following_list)
    followers_set = set(followers_list)

    not_follow_back = list(following_set - followers_set)
    not_following_you = list(followers_set - following_set)

    return {
        "not_follow_back": not_follow_back,
        "not_following_you": not_following_you
    }
