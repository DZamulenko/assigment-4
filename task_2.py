def get_grade(score):
    std_ratings=[]
    for i in range(len(score)):
        if 90<=score[i]<=100:
            std_ratings.append('A')
        elif 80<=score[i]<=89:
            std_ratings.append('B')
        elif 70<=score[i]<=79:
            std_ratings.append('C')
        elif 60<=score[i]<=69:
            std_ratings.append('D')
        else:
            std_ratings.append('F')
    return std_ratings
scores = [95, 45, 78, 82, 60]
print(get_grade(scores))