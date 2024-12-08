with open("puzzle_input") as f:
    puzzle_input = [line.strip() for line in f.readlines()]

calibration_list = []
for line in puzzle_input:
    product, inputs = line.split(": ")
    product = int(product)
    inputs = list(int(val) for val in inputs.split(" "))
    calibration_list.append([product, inputs])


def get_next_operator_combination(item_count, previous_attempt):
    if previous_attempt == "".join(["*" for _ in range(item_count - 1)]):
        return False
    bin_value = int(previous_attempt.replace("+", "0").replace("*", "1"), base=2)
    bin_value += 1
    next_combination = format(bin_value, "b").replace("0", "+").replace("1", "*")
    while len(next_combination) < item_count - 1:
        next_combination = "+" + next_combination
    return next_combination


calibration_result = 0
for test in calibration_list:
    product, inputs = test
    attempt = "".join(["+" for _ in range(len(inputs) - 1)])
    while attempt:
        value = inputs[0]
        for i, operator in enumerate(attempt):
            if operator == "+":
                value += inputs[i+1]
            elif operator == "*":
                value *= inputs[i+1]
        if value == product:
            print(f"{product} is valid: {attempt}")
            calibration_result += product
            break
        attempt = get_next_operator_combination(len(inputs), attempt)
print(calibration_result)