def solution(arr, idx):
    for i, v in enumerate(arr):
        if idx <= i and v == 1:
            return i
    return -1
  