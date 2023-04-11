def solution(id_list, report, k):
    id_dict = {}
    reported = {}

    for id in id_list:
        id_dict[id] = 0
        reported[id] = 0

    report = list(set(report))

    for i in range(len(report)):
        report[i] = list(report[i].split())

    for i in range(len(report)):
        reported[report[i][1]] += 1

    for i in range(len(report)):
        if reported[report[i][1]] >= k:
            id_dict[report[i][0]] += 1

    answer = []

    for name in id_dict:
        answer.append(id_dict[name])

    return answer


id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3

print(solution(id_list, report, k))