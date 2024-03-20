def solution(todo_list, finished):
    return [work for i, work in enumerate(todo_list) if finished[i] is False]