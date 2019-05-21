school = [
    {'school_class':'1a', 'score':[3,4,5,2,2]},
    {'school_class':'2a', 'score':[4,3,4,2,3]},
    {'school_class':'3a', 'score':[3,5,5,4,4]},
    {'school_class':'4a', 'score':[2,5,4,2,2]},
    {'school_class':'5a', 'score':[5,3,5,4,3]},
]


def average_score(smth):
    result = list()
    for dict1 in school:
        for number in dict1['score']:
            result.append(number)
    return(result)


result1 = sum(average_score(school)) / len(average_score(school))
print("Средний балл по школе: ", result1)

for dict2 in school:
    result2 = sum(dict2['score']) / len(dict2['score'])
    print("Средний балл по классам: ", result2)     