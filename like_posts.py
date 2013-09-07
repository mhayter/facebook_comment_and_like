#Adopted from : http://www.quora.com/Python-programming-language-1/What-are-the-best-Python-scripts-youve-ever-written
import requests
import json
import random

#Insert your personalized token here
TOKEN = 'CAACEdEose0cBAECRnbC5VmITg4bMZCpZAOjwgDIK8whJuY4P3vP8sUz5qZC0CVNDhOuu8DScIwxQMclre8vZCSg7QjFqB6pQaWjqI64p3Q8ivuhXJYyOlnnTzMjomq6qGt32A7gXbPkYPYL6aVIYH7HdmLx08Ljs8CNghgx8kZBRrQwff6OMkrdXy6yZATOwNZBrjBxzNDg4AZDZD'

#Insert desired phrases here
PHRASES = ['#hellyeah', '#killinit', '#goblue', 'the man']; 


def get_posts():
    """Returns dictionary of id, first names of people who posted on my wall
    between start and end time"""
    query = ("SELECT post_id, actor_id, message FROM stream WHERE "
            "filter_key = 'others' AND source_id = me() LIMIT 10")

    payload = {'q': query, 'access_token': TOKEN}
    r = requests.get('https://graph.facebook.com/fql', params=payload)
    result = json.loads(r.text)
    return result['data']

def comment_all(wallposts):
    """Comments thank you on all posts"""
    for wallpost in wallposts:

        r = requests.get('https://graph.facebook.com/%s' %
                wallpost['actor_id'])
				
        url_comments = 'https://graph.facebook.com/%s/comments' % wallpost['post_id']
        url_likes = 'https://graph.facebook.com/%s/likes' % wallpost['post_id']
		
        user = json.loads(r.text)
        message = PHRASES[random.randint(0,len(PHRASES) - 1)]
		
        comments_payload = {'access_token': TOKEN, 'message': message}
        likes_payload = {'access_token': TOKEN}
		
        send_comments = requests.post(url_comments, data=comments_payload)
        send_likes = requests.post(url_likes, likes_payload)

        print "Wall post %s done" % wallpost['post_id']

if __name__ == '__main__':
	comment_all(get_posts())