def getScore(time, active_row):
    score = 10_000 - (active_row**2)*1_000 - ((time-1) / 60) ** 2
    
    if score < 0:
        score = 0
    
    return round(score)


if __name__ == "__main__":
    print(getScore(600, 9))