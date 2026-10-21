from collections import deque

n, m = map(int, input().split())
target_list = map(int, input().split())

min_move = 0
num_list = ...

for find_idx in target_list:
    num_idx = num_list.index(find_idx)
    move_cnt = num_idx

    if move_cnt > (len(num_list) - move_cnt):
        move_cnt -= len(num_list)
    
    # print(move_cnt)

    min_move += abs(move_cnt)

    # num_list.append(num_list.popleft())
    # num_list.appendleft(num_list.pop())

    num_list.rotate(-move_cnt)
    num_list.popleft()

    # print(num_list)

print(min_move)
