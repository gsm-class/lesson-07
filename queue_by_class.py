# [..., 1,2,3,4,5,6,7, ...]

class Queue:
    def __init__(self, n):
        # self.array = [None] * n
        self.array: list[int | None] = [None for _ in range(n)]
        self.f_idx = 0
        self.b_idx = 0

    def push(self, num):
        self.array[self.b_idx] = int(num)
        self.b_idx += 1
    
    def pop(self):
        # if self.b_idx - self.f_idx == 0:
        # if self.f_idx == self.b_idx:
        # if self.size() == 0:
        if self.is_empty():
            return -1

        # self.f_idx += 1
        # return self.array[self.f_idx-1]
        last_val = self.array[self.f_idx]
        self.f_idx += 1
        return last_val
    
    def size(self):
        return self.b_idx - self.f_idx
    
    def empty(self):
        return int(self.is_empty())
    
    def is_empty(self):
        return self.size() == 0
    
    def front(self):
        if self.is_empty():
            return -1

        return self.array[self.f_idx]
    
    def back(self):
        if self.is_empty():
            return -1

        return self.array[self.b_idx-1]

def run_cmd_with_queue(queue_obj, command):
    cmd_type = command[0]
    
    if cmd_type == "push":
        _, num = command
        queue_obj.push(int(num))
    elif cmd_type == "pop":
        print(queue_obj.pop())
    elif cmd_type == "size":
        print(queue_obj.size())
    elif cmd_type == "empty":
        print(queue_obj.empty())
    elif cmd_type == "front":
        print(queue_obj.front())
    elif cmd_type == "back":
        print(queue_obj.back())

n = int(input())
queue_obj = Queue(n)

for _ in range(n):
    run_cmd_with_queue(queue_obj, input().split())