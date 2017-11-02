from steem import Steem
from steem.blockchain import Blockchain
from steem.post import Post

#create steem instance and pass it your private posting key
s = Steem(keys = ["<your private posting key>"])
#create blockchain instance
b = Blockchain()

while True:
    try:
        # stream the blockchain
        stream = map(Post, b.stream(filter_by=['comment']))
        # go through all the posts in the block
        for post in stream:
            # get all the tags of the post
            postTags = post.json_metadata.get('tags', [])
            # check if "introduceyourself" is in the list of tags. You can add more tags
            if "introduceyourself" in postTags:
                title = post.title
                # check if the post/comment has a title
                if title == "":
                    #title is empty so it's most likely a comment
                    pass

                else:
                    #We have a title so it's a fresh posts so let's welcome them
                    post.reply("Welcome to Steemit!", "", "<your steemit username>")

            else:
                #no introduceyourself tag so skip the post
                pass

    #Catch any unexpected exceptions
    except Exception as e:
        print("Error: "+str(e))
