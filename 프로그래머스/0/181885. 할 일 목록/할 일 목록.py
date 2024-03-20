def solution(todo_list, finished):
    todo = dict(zip(todo_list, finished))
    return [k for k, v in todo.items() if v is False]