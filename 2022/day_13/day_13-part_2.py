with open('day_13-input') as f:
    packets = [eval(line.rstrip()) for line in f.readlines() if line.rstrip() != '']
packets.append([[2]])
packets.append([[6]])

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
            left = left + ['x' for _ in range(len(right) - len(left))]
            right = right + ['x' for _ in range(len(left) - len(right))]
        pairs = list(zip(left, right))
        for a, b in pairs:
            is_ordered = compare(a,b)
            if is_ordered is not None:
                return is_ordered

    elif type(left) == list and type(right) == int:
        return compare(left, [right])
    elif type(left) == int and type(right) == list:
        return compare([left], right)

is_ordered = False
while not is_ordered:
    is_ordered = True
    for i in range(len(packets)-1):
        if not compare(packets[i], packets[i+1]):
            is_ordered = False
            temp = packets[i]
            packets[i] = packets[i+1]
            packets[i+1] = temp

print((packets.index([[2]])+1) * (packets.index([[6]])+1))