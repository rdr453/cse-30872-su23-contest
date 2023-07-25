def count_buildings_with_sunrise_view(buildings):
    count = 0
    max_height = 0

    for height in reversed(buildings):
        if int(height) > max_height:
            count += 1
            max_height = int(height)

    return count

while True:
    try:
        inp = input().split()
        print(count_buildings_with_sunrise_view(inp))
    except EOFError:
        break
