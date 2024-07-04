def solution(rank, attendance):
    answer = {}
    for i in range(len(rank)):
        if attendance[i] is True:
            answer[rank[i]] = i
    values = [answer[key] for key in sorted(answer)]
    return 10000 * values[0] + 100 * values[1] + values[2]