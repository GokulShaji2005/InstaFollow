import zipfile
import json

zipFile="instalfol1.zip"#paste the zipfile downloaded from instagram account center in json format
following_list=[]
followers_list=[]
with zipfile.ZipFile(zipFile,"r") as z:
    
    for file in z.namelist():
        if file.endswith(".json"):
            # print(file)
            if  "following.json" in file:
                with z.open(file) as f:
                  following=json.load(f)
                  for item in following["relationships_following"]:
                      usernameOfFollowing=item["title"]
                 
                      following_list.append(usernameOfFollowing)
                    
                    #   print(following_set)

                #   print("Following",following)
            if "followers_1.json" in file:
                with z.open(file) as f:
                    followers=json.load(f)
                    
                    for item in followers:
                        usernameOfFollowers=item["string_list_data"][0]["value"]
                        
                        followers_list.append(usernameOfFollowers)
                          
following_set=set(following_list)
followers_set=set(followers_list)
notFollowBack=following_set-followers_set
notFollowing=followers_set-following_set


print(notFollowBack)   
# print(notFollowing)                
                     
                


  