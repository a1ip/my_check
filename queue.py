def letter_queue2(seq):
    que = []
    for item  in seq:
        _, *value = item.split(" ")
        if value:
            que.append(value[0])
        else:
            try:
                que.pop(0)
            except:
                pass
    return "".join(que)

def letter_queue__xxx(seq):
    s = ""
    for item in seq:
        if item[-2] == " ":
            s += item[-1]
        else:
            s = s[1:]
    return s

letter_queue = lambda seq: "".join(sum(([c[-1]] if c[-2] else [c[1:]] for c in seq),[]))


from collections import deque #japoncovo
def letter_queue_(commands):
    l = deque()
    for c in commands:
        if c.startswith('PUSH'):
            l.append(c[5:])
        elif c == 'POP' and len(l) > 0:
            l.popleft()
    return ''.join(l)


from timeit import timeit

def letter_queue__(commands): #twice faster?
    queue, idx = [], 0
    for c in commands:
        if c == 'POP':
            if idx < len(queue):
                idx += 1
        else:
            queue.append(c[-1])
    return ''.join(queue[idx:])


s="""letter_queue(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"])"""
print(
    timeit(s, setup = "from __main__ import letter_queue", number=100000)
    )
s="""letter_queue_(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"])"""
print(
    timeit(s, setup = "from __main__ import letter_queue_", number=100000)
    )

s="""letter_queue2(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"])"""
print(
    timeit(s, setup = "from __main__ import letter_queue2", number=100000)
    )

s="""letter_queue__(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"])"""
print(
    timeit(s, setup = "from __main__ import letter_queue__", number=100000)
    )



    
    
        



assert letter_queue(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]) == "DOT"
assert letter_queue(["POP", "POP"]) == ""
assert letter_queue(["PUSH H", "PUSH I"]) == "HI"
assert letter_queue([]) == ""
