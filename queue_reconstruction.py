def reconstructQueue(people):
    # sort by largest height and least amount of people taller
    people.sort(key=lambda p:(-p[0],p[1]))
    result = []
    for i in range(0, len(people)):
        # insert by amount of people taller
        result.insert(people[i][1], people[i])
    return result

people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
print(reconstructQueue(people))
