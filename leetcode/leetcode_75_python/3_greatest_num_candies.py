def kidsWithCandies(candies: list[int], extraCandies: int) -> list[bool]:
    yep = []
    biggest_count = max(candies)
    
    for i in range(len(candies)):
        if (candies[i] + extraCandies) < biggest_count:
            yep.append(False)
        elif (candies[i] + extraCandies) >= biggest_count:
            yep.append(True)
    
    return yep

print(kidsWithCandies([4,2,1,1,2], 1))