with open("puzzle_input") as f:
    puzzle_input = [line.strip() for line in f.readlines()]

reports = []
for line in puzzle_input:
    reports.append([int(item) for item in line.split(" ")])


def is_safe(report):
    def increasing(report):
        for i in range(len(report)-1):
            if report[i] > report[i+1]:
                return False
            if report[i+1] - report[i] < 1:
                return False
            if report[i+1] - report[i] > 3:
                return False
        return True

    def decreasing(report):
        for i in range(len(report)-1):
            if report[i] < report[i+1]:
                return False
            if report[i] - report[i+1] < 1:
                return False
            if report[i] - report[i+1] > 3:
                return False
        return True

    if report[0] <= report[1]:
        return increasing(report)
    else:
        return decreasing(report)

safe_report_count = 0
failed_reports = []

for report in reports:
    if is_safe(report):
        safe_report_count += 1
    else:
        failed_reports.append(report)

for report in failed_reports:
    for i in range(len(report)):
        dampened_report = report[:i] + report[i+1:]
        if is_safe(dampened_report):
            safe_report_count += 1
            break

print(safe_report_count)
