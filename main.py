from __future__ import division
from collections import Counter

users = [{"id": 0, "name": "Hero"},
         {"id": 1, "name": "Dunn"},
         {"id": 2, "name": "Sue"},
         {"id": 3, "name": "Chi"},
         {"id": 4, "name": "Thor"},
         {"id": 5, "name": "Clive"},
         {"id": 6, "name": "Hicks"},
         {"id": 7, "name": "Devin"},
         {"id": 8, "name": "Kate"},
         {"id": 9, "name": "Klein"}]

friendships = [(0, 1),
               (0, 2),
               (1, 2),
               (1, 3),
               (2, 3),
               (3, 4),
               (4, 5),
               (5, 6),
               (5, 7),
               (6, 8),
               (7, 8),
               (8, 9)]
print(users)

for user in users:
    user["friends"] = []
for i, j in friendships:
    users[i]["friends"].append(users[j])
    users[j]["friends"].append(users[i])


def number_of_friends(user):
    return len(user['friends'])


total_connections = sum(number_of_friends(user) for user in users)
print(total_connections)

num_users = len(users)

avg_connections = total_connections / num_users

print(avg_connections)

num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]
print(num_friends_by_id)

num_friends_by_id = sorted(num_friends_by_id, key=lambda x: x[1], reverse=True)

print(num_friends_by_id)


def friends_of_friends_ids_bad(user):
    return [friend_of_friend["id"]
            for friend in user["friends"]
            for friend_of_friend in friend["friends"]]


FriendsOfFriendsBad = friends_of_friends_ids_bad(users[0])

print(FriendsOfFriendsBad)


def not_the_same(user, other_user):
    return user["id"] != other_user["id"]


notTheSame = not_the_same(users[0], users[1])


def not_friends(user, other_user):
    return all(not_the_same(friend, other_user)
               for friend in user["friends"])


notFriends1 = not_friends(users[0], users[1])
print(notFriends1)
notFriends2 = not_friends(users[0], users[0])
print(notFriends2)


def friends_of_friends_ids_good(user):
    return Counter(friend_of_friend["id"]
                   for friend in user["friends"]
                   for friend_of_friend in friend["friends"]

                   if not_the_same(user, friend_of_friend) and not_friends(user, friend_of_friend))


FriendsOfFriendsGoog = friends_of_friends_ids_good(users[3])
print(FriendsOfFriendsGoog)
