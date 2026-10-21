from collections import deque

def calc_last_card(n):
    d_list = deque([i for i in range(1, n+1)])

    rotate_flag = False

    while len(d_list) > 1:
        if not rotate_flag:
            d_list.popleft()
        else:
            d_list.append(d_list.popleft())
            # d_list.rotate(-1)

        rotate_flag = not rotate_flag

    return d_list.popleft()

n = int(input())
print(calc_last_card(n))

# sample_deque = deque([1,2,3,4,5])
# sample_deque.rotate(-1)
# print(sample_deque)
# sample_deque.rotate(-2)
# print(sample_deque)