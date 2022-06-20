def dangerous(players):
    players_sequence = 1
    danger_reached = False
    i = 1
    while i < len(players):
        if players[i] == players[i-1]:
            players_sequence += 1
        else:
            players_sequence = 1
        i += 1
        if players_sequence == 7:
            i = len(players)
            danger_reached = True
            break
    if danger_reached:
        print("YES")
        return("YES")
    else:
        print("NO")
        return("NO")

players=str(input())
dangerous(players)

