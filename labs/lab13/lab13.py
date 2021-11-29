"""
Name: <Luke Wood>
<lab13>.py
"""


def is_in_binary(search_val, values):
    mid = search_val[len(search_val) // 2]
    while mid != values and len(search_val) != 1:
        if mid > values:
            search_val = search_val[:mid]
        else:
            search_val = search_val[mid:]
        mid = search_val[len(search_val) // 2]
    if len(search_val) == 1 and search_val[0] != values:
        return False
    else:
        return True


def selection_sort(values):
    for i in range(len(values)):
        lowest = values[i]
        pos = i
        for j in range(i + 1, len(values)):
            if values[j] < lowest:
                lowest = values[j]
                pos = j
        values[i], values[pos] = values[pos], values[i]


def calc_area(rect):
    p1 = rect.getP1()
    p2 = rect.getP2()
    dx = abs(p1.getX() - p2.getX())
    dy = abs(p1.getY() - p2.getY())
    return dx * dy


def rect_sort(rectangles):
    dict = {}
    areas = []
    for rect in rectangles:
        dict[calc_area(rect)] = rect
        areas.append(calc_area(rect))
    selection_sort(areas)
    for i in range(len(areas)):
        rectangles[i] = dict[areas[i]]


def star_find(filename):
    file = open(filename, "r")
    found = []
    signals = file.read().split()
    for i in range(len(signals)):
        if 4000 <= int(signals[i]) <= 5000:
            found.append(int(signals[i]))
        if len(found) == 5:
            break
    print(len(found))
    print(found)
    if len(found) != 5:
        print("5 signals were not found")
    else:
        print(i)


def main():
    is_in_binary([1, 2, 3], 4)
    selection_sort([4, 2, 3, 1])
    rect_sort({4: "r3", 8: "r2", 10: "r1"})
    star_find("signals.txt")

    # add other function calls here
    pass

    main()
