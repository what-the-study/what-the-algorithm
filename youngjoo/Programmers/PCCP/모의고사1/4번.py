from heapq import heappop, heappush


def solution(program):
    program.sort(key=lambda p: (p[1], p[0]))
    answer = [0] * 11

    wait, execute = [], []
    node, second, stopped = 0, 0, 0

    while True:
        while node < len(program) and program[node][1] == second:
            heappush(wait, program[node])
            node += 1

        if execute and execute[-1][-1] == second:
            answer[0] = execute.pop()[-1]
            stopped += 1

            if stopped == len(program):
                break

        if wait and not execute:
            p = heappop(wait)
            answer[p[0]] += second - p[1]
            execute.append(p + [second + p[2]])

        second += 1

    return answer
