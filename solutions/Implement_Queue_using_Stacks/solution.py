class MyQueue:

    def __init__(self):
        self.st1 = []
        self.st2 = []

    def push(self, x: int) -> None:
        self.st1.append(x)

    def pop(self) -> int:
        if not self.st2:  #len(self.s2)
            if not self.st1:
                return 0
            # if成立的話, 會直接進return, 若沒成立也會往下跑, 所以也沒必要寫else (optimized已改進)
            else:
                while self.st1:
                    self.st2.append(self.st1.pop())

        return self.st2.pop()

    def peek(self) -> int:
        if not self.st2:  #len(self.s2)
            if not self.st1:
                return 0
            else:
                return self.st1[0]
            
        return self.st2[len(self.st2)-1]

    def empty(self) -> bool:
        # 只要self.st2與st1都不存在的話才是True, 所以可簡化成 if not self.st2 and not self.st1 (optimized已改進)
        if not self.st2:
            if not self.st1:
                return True
            else:
                return False
        return False


#Optimized Answer
class MyQueue:

    def __init__(self):
        self.st1 = []
        self.st2 = []

    def push(self, x: int) -> None:
        self.st1.append(x)

    def pop(self) -> int:
        if not self.st2:  #len(self.s2)
            if not self.st1:
                return 0
            while self.st1:
                    self.st2.append(self.st1.pop())

        return self.st2.pop()

    def peek(self) -> int:
        if not self.st2:  #len(self.s2)
            if not self.st1:
                return 0
            else:
                return self.st1[0]
            
        return self.st2[len(self.st2)-1]

    def empty(self) -> bool:
        return not self.st2 and not self.st1