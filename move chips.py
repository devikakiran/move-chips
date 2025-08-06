def minCostToMoveChips(position):
    even_count = 0
    odd_count = 0
    for p in position:
        if p % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return min(even_count, odd_count)
positions = [1, 2, 3,25,50,52,55,82]
print("Minimum cost to move chips:", minCostToMoveChips(positions))
