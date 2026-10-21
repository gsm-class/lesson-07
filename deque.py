from collections import deque

array_list = deque()

print(array_list)

array_list.append(10)
array_list.append(20)
array_list.append(30)

array_list.appendleft(1)
array_list.appendleft(2)
array_list.appendleft(3)

print(array_list)

print(array_list.pop())
print(array_list.popleft())