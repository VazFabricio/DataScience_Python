from __future__ import division
from collections import Counter, defaultdict

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
    # Cria um contador vazio para armazenar o número de ocorrências de cada ID de amigo dos amigos do usuário
    # que atendem às condições especificadas abaixo
    return Counter(
        # Retorna o ID de cada amigo do amigo do usuário que atende às condições especificadas abaixo
        friend_of_friend["id"]
        # Loop sobre todos os amigos do usuário
        for friend in user["friends"]
        # Loop sobre todos os amigos de cada amigo do usuário (que são os amigos dos amigos do usuário)
        for friend_of_friend in friend["friends"]
        # Verifica se o amigo do amigo não é o próprio usuário e se ele não é um amigo direto do usuário
        if not_the_same(user, friend_of_friend) and not_friends(user, friend_of_friend)
    )


FriendsOfFriendsGoog = friends_of_friends_ids_good(users[3])
print(number_of_friends(users[3]))
print(FriendsOfFriendsGoog)


def direct_friends_ids(user):
    return [friend["id"] for friend in user["friends"]]


print(direct_friends_ids(users[3]))
print(direct_friends_ids(users[0]))
print(direct_friends_ids(users[5]))

print(direct_friends_ids(users[1]))
print(direct_friends_ids(users[2]))
print(direct_friends_ids(users[4]))

interests = [(0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"), (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
             (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"), (1, "Postgres"),
             (2, "Python"), (2, "scikit-learn"), (2, "scipy"), (2, "numpy"), (2, "statsmodels"), (2, "pandas"),
             (3, "R"), (3, "Python"), (3, "statistics"), (3, "regression"), (3, "probability"),
             (4, "machine learning"), (4, "regression"), (4, "decision trees"), (4, "libsvm"),
             (5, "Python"), (5, "R"), (5, "Java"), (5, "C + +"), (5, "Haskell"), (5, "programming languages"),
             (6, "statistics"), (6, "probability"), (6, "mathematics"), (6, "theory"),
             (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"), (7, "neural networks"),
             (8, "neural networks"), (8, "deep learning"), (8, "Big Data"), (8, "artificial intelligence"),
             (9, "Hadoop"), (9, "Java"), (9, "MapReduce"), (9, "Big Data")]


def data_scientists_who_like(target_interest):
    return [user_id for user_id, user_interest in interests
                        if user_interest == target_interest]


likes = data_scientists_who_like("Big Data")

user_ids_by_interest = defaultdict(list)

for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)

print(user_ids_by_interest["Big Data"])

interests_by_user_id = defaultdict(list)

for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)

print(interests_by_user_id[0])
