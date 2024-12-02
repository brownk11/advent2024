
def parse_input():
    file1 = open("input", "r")
    distance_list = file1.readlines()
    list1 = []
    list2 = []

    for s in distance_list:
        split_list = s.split()
        list1.append(split_list[0])
        list2.append(split_list[1].split('\n')[0])

    return list1, list2

def day_one(l1, l2):
    _sum = 0
    for i in range(len(l1)):
        _sum = _sum + abs(int(l1[i]) - int(l2[i]))

    return _sum

def part_two(l1, l2):
    _map = {}
    total = 0

    for i in range(len(l1)):
        num = l1[i]
        if num in l2:
            count = l2.count(num)
            _map[int(num)] = count

    print(_map)
    for key, value in _map.items():
        similar_score = int(key) * int(value)
        print(similar_score)
        if value > 1:
            total = total + (similar_score * value)
        else:
            total = similar_score + total




    return total

if __name__ == '__main__':
    l1, l2 = parse_input()
    print('part two ' + str(part_two(l1, l2)))
    l1.sort()
    l2.sort()
    print('part one ' + str(day_one(l1,l2)))
