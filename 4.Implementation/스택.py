#10828
import sys
n = int(sys.stdin.readline())
stack = []

for i in range(n) :
    stc = sys.stdin.readline().split()
    dr = stc[0]
    if dr == "push":
        stack.append(int(stc[1]))
    elif dr == "top" :
        if len(stack) == 0 :
            print(-1)
            continue
        print(stack[-1])
    elif dr == "size" :
        print(len(stack))
    elif dr == "pop" :
        if len(stack) == 0 :
            print(-1)
            continue
        print(stack.pop())
    elif dr == "empty" :
        if len(stack) == 0 :
            print(1)
        else :
            print(0)

