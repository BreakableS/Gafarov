users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

stat = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}

stat["Общее количество"] = len(users)
stat["Уникальные посещения"] = len(set(users))

print(stat)
