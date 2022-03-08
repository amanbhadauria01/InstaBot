# Instagram Direct Message Bot

You can do the following using this bot :  
1. Login to instagram 
2. Read comments on a post 
3. Delete comments on a post
4. Find all followers of a public account
5. DM people on instagram

## Example : 

To find all followers of a public account having handle xyz : 
```
   obj = InstaDM(user_handle,user_password)
   follower_data = obj.(followers_list(xyz)) 
```
