logs =  [[1950,1961],[1960,1971],[1970,1981]]
population = 0
Dict = {}
for i in range(len(logs)):
    currentBirthYear = logs[i][0]
    population += 1
    Dict[str(currentBirthYear)] = population

    currentDeathYear = logs[i][1]
    population -= 1
    Dict[str(currentDeathYear)] = population

    if i+1 < len(logs):
        nextBirthYear = logs[i+1][0]
        nextDeathYear = logs[i+1][1]
        if nextBirthYear <= currentDeathYear:
            population += 1
            Dict[str(nextBirthYear)] = population
        else:
            Dict[str(currentDeathYear)] = population
print(Dict)