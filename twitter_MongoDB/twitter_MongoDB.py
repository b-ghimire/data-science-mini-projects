# This python code scrapes twitter data and stores in MongoDB

# Import the python-twitter package
import twitter

# Import pymongo package which interfaces python with mongodb
import pymongo

# Start the twitter api class with the authentication key and secret
tconsumer_key = 'ENTER_HERE'
tconsumer_secret = 'ENTER_HERE'
taccess_token_key = 'ENTER_HERE'
taccess_token_secret = 'ENTER_HERE'
api = twitter.Api (consumer_key=tconsumer_key, consumer_secret=tconsumer_secret, 
       access_token_key=taccess_token_key, access_token_secret=taccess_token_secret)

# Searching for tweets with a given keyword
tweets = api.GetSearch(term='Nepal')

# Displaying data type
type(tweets)

# Displaying data type of first list item
tweets[1]

# Displaying variables
vars(tweets[1])

# Create pymongo client connection
conn = pymongo.MongoClient()

# Creating mongodb database named twitter_database
db = conn.twitter_database

# Creating a collection within the database
# Collection is a group of documents
# Collection is equivalent to a table in a relational database
collection = db.collection

# Inserting document to a collection
# A document is equivalent to a record in a relational database
# A document is equivalent to a dictionary in python
for tw in tweets:

     # Define empty python dictionary
    tweet = {} 

    # Fill the dictionary
    tweet['contributors'] = tw.contributors
    tweet['coordinates'] = tw.coordinates
    tweet['created_at'] = tw.created_at
    tweet['current_user_retweet'] = tw.current_user_retweet
    tweet['geo'] = tw.geo
    tweet['id'] = tw.id
    tweet['id_str'] = tw.id_str
    tweet['in_reply_to_screen_name'] = tw.in_reply_to_screen_name
    tweet['in_reply_to_status_id'] = tw.in_reply_to_status_id
    tweet['in_reply_to_user_id'] = tw.in_reply_to_user_id
    tweet['location'] = tw.location
    tweet['now'] = tw.now
    tweet['place'] = tw.place
    tweet['retweet_count'] = tw.retweet_count
    tweet['retweeted'] = tw.retweeted
    tweet['source'] = tw.source
    tweet['text'] = tw.text
        
    collection.insert(tweet)

print tweet
