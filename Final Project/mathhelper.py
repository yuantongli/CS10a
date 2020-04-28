PI = 3.14

PRIORITY = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
}

class Stack:
    def __init__(self):
        self.stack = []
        self.top = 0

    def push(self, element):
        if self.top >= len(self.stack):
            self.stack += [element]
        else:
            self.stack[self.top] = element
        self.top += 1

    def pop(self):
        if self.top == 0:
            return None
        self.top -= 1
        return self.stack[self.top]

    def peek(self):
        return self.stack[self.top - 1]

    def __len__(self):
        return self.top

    def __str__(self):
        return str.join(' ', [str(self.stack[i]) for i in range(self.top)])

def extract_tokens(expression):
    tokens = []
    current_token = ''
    previous_is_digit = True

    for ch in expression:
        if ch == ' ':
            continue

        if ch.isdigit() or ch == '.':
            if previous_is_digit:
                current_token += ch
            else:
                tokens.append(current_token)
                current_token = ch
                previous_is_digit = True
        else:
            tokens.append(current_token)
            current_token = ch
            previous_is_digit = False

    tokens.append(current_token)
    return tokens

def convert_postfix(expression):
    prefix_tokens = extract_tokens(expression)

    PRIORITY_PARENS = 100
    base_priority = 0

    postfix_tokens = []

    operands = Stack()
    operators = Stack()

    for token in prefix_tokens:
        if token.replace('.', '').isdigit():
            postfix_tokens.append(token)
        elif token == '(':
            base_priority += PRIORITY_PARENS
        elif token == ')':
            base_priority -= PRIORITY_PARENS
        else:
            while len(operators) != 0 and PRIORITY[token] + base_priority <= PRIORITY[operators.peek()]:
                postfix_tokens.append(operators.pop())
            operators.push(token)

    while len(operators) != 0:
        postfix_tokens.append(operators.pop())

    return str.join(' ', postfix_tokens)

def calculate(expression):
    def do_calc(op1, op2, operator):
        if operator == '+':
            return op1 + op2
        elif operator == '-':
            return op1 - op2
        elif operator == '*':
            return op1 * op2
        elif operator == '/':
            return op1 / op2

    try:
        tokens = convert_postfix(expression).split(' ')
        operands = Stack()

        for token in tokens:
            if token.replace('.', '').isdigit():
                operands.push(float(token))
            else:
                #print(token)
                op2 = operands.pop()
                op1 = operands.pop()
                operands.push(do_calc(op1, op2, token))
            #print(operands)
        return operands.pop()
    except Exception:
        return None

def area_triangle(base, height):
    try: 
        return float(base) * float(height) / 2
    except Exception:
        return None

def area_circle(r):
    try:
        r = float(r)
        return PI * r * r
    except Exception:
        return None

def area_trapezoid(top, bottom, height):
    try:
        return (float(top) + float(bottom)) * float(height) / 2
    except Exception:
        return None

