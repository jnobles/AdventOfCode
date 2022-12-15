with open('day_13-input') as f:
    file_input = [line.strip() for line in f.readlines()]

packet_pairs = []
for i in range(0, len(file_input), 3):
    left = eval(file_input[i])
    right = eval(file_input[i+1])
    packet_pairs.append((left, right))


def compare(left, right):
    if left == 'x':
        return True
    elif right == 'x':
        return False
    elif type(left) == int and type(right) == int:
        if left == right:
            return None
        else:
            return left < right

    if type(left) == list and type (right) == list:
        if len(left) != len(right):
            left.extend('x' for _ in range(len(right) - len(left)))
            right.extend('x' for _ in range(len(left) - len(right)))
        pairs = list(zip(left, right))
        for a, b in pairs:
            is_ordered = compare(a,b)
            if is_ordered is not None:
                return is_ordered

    elif type(left) == list and type(right) == int:
        return compare(left, [right])
    elif type(left) == int and type(right) == list:
        return compare([left], right)

ordered_index_sum = 0
for i, (left, right) in enumerate(packet_pairs, start=1):
    if compare(left, right):
        ordered_index_sum += i

print(ordered_index_sum)

