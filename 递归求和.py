# 求和递归
def sum(items):
    head,*tail = items
    return head + sum(tail) if tail else head

print(sum(items = [100,99,89]))