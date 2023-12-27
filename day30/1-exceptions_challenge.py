# Solve an Error through catching exceptions

# Initial code:

facebook_posts = [
    {'Likes': 23, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 1},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3},
]
total_likes = 0


# CAUSE OF THE ERROR
# for post in facebook_posts:
#     total_likes = total_likes + post['Likes']


"""METHOD 1: USING TRY/CATCH"""
for post in facebook_posts:
    try:
        total_likes = total_likes + post.get('Likes')
    except (KeyError, TypeError):
        total_likes += 0

print(total_likes)

"""METHOD 2: USING GET METHOD"""

for post in facebook_posts:
    # USe 0 for values that dont match the key 'Likes'
    total_likes = total_likes + post.get('Likes', 0)
