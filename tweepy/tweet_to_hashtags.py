import csv

filename = input("Write your file name (e.g. macron_0504_100) : ")

tweets_filename = filename + "tweets.csv"
hashtags_filename = filename + "hashtags.csv"

tweets = open(tweets_filename, 'r')
hashtags = open(hashtags_filename, 'w', newline = "")

rdr = csv.reader(tweets)
wtr = csv.writer(hashtags)

for line in rdr:
	hashtag_raw = line[-1]
	hashtag_raw = hashtag_raw.lstrip('[')
	hashtag_raw = hashtag_raw.rstrip(']')
	hashtag_raw = hashtag_raw.replace("'","")
	hashtag_list = hashtag_raw.split(',')
	wtr.writerow(hashtag_list)

tweets.close()
hashtags.close()

