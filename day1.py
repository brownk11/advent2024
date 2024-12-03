def parse_input():
    with open("input", "r") as file1:  # Using with for proper file handling
        distance_list = file1.readlines()
        list1 = []
        list2 = []
        for s in distance_list:
            split_list = s.split()
            list1.append(int(split_list[0]))  # Converting to int immediately
            list2.append(int(split_list[1]))  # No need to handle \n separately
        return list1, list2

def day_one(l1, l2):
    _sum = 0
    for i in range(len(l1)):
        _sum = _sum + abs(int(l1[i]) - int(l2[i]))  # Fixed syntax error with *sum
    return _sum

def part_two(l1, l2):
    total = 0
    # Process each number in left list independently
    for num in l1:
        count = l2.count(num)  # Count occurrences in right list
        similar_score = num * count  # Calculate similarity score for this number
        total += similar_score  # Add to total
    return total

if __name__ == '__main__':
    l1, l2 = parse_input()
    print('part two ' + str(part_two(l1, l2)))
    l1.sort()
    l2.sort()
    print('part one ' + str(day_one(l1, l2)))
