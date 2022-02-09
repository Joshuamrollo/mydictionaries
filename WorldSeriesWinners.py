def main(file_name): 
    team_dict = {}
    year_dict = {}
    year = 1903

    file = open(file_name, mode="r")
    
    text = file.read().split('\n')

    for team in text:
        if team not in team_dict:
            team_dict[team] = 0
        else:
            team_dict[team] += 1

        year_dict[year] = team
        year += 1

    file.close()

    while(True):
        year = input("pick a year between 1903 and 2009: ")
        if not year.isdigit(): 
            print("Please enter a valid year")
            continue
        if int(year) >= 1903 and int(year) <= 2009:
            break
        print("Please enter a valid year")
    team = year_dict[int(year)]

    print(year + " world series winner is " + team)
    print("The " + team + " have won the world series " + str(team_dict[team]) + " times between 1903 and 2009")
            
    


main('WorldSeriesWinners.txt')