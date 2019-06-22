def points(games):
    points_total = 0
    
    for i in games:
        if  i[0] > i[2]:
            points_total += 3
        elif i[0] == i[2]:
            points_total += 1
            
    return points_total