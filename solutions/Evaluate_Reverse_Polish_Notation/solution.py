#My Original Answer (Recursive)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for token in tokens:
            if token not in ['+','-','*','/']:
                st.append(int(token))
            else:
                if st:
                    num_1 = st.pop()
                    num_2 = st.pop()
                    total = 0
                match token:
                    case '+':
                        total = num_2 + num_1
                    case '-':
                        total = num_2 - num_1
                    case '*':
                        total = num_2 * num_1
                    case '/':
                        total = int(num_2 / num_1)
                    
                st.append(total)

        return st[0] if st else 0
    
## Time Complexity:O(n)
## Space complexity:O(n)

#My Original Answer

import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': lambda x, y: int(x / y)  # lambda等於"隱藏宣告"的函數, 等於[註1]。
        }

        for token in tokens:
            if token not in ops:
                st.append(int(token))
            else:
                b, a = st.pop(), st.pop()
                st.append(ops[token](a,b))

        return st[0]
    
## Time Complexity:O(n)
## Space complexity:O(n)

'''
註1:

def /(x,y):
    return int(x/y)
'''