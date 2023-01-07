def getScore(time, active_row):
    score = 10_000 - (active_row**2)*100 - ((time-1) * 0.1) ** 2
    
    if score < 0:
        score = 0
    
    return round(score)


if __name__ == "__main__":
    print(getScore(600, 9))