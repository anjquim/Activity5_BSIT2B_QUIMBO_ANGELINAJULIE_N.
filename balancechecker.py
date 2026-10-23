# balance checker

from array_stack import ArrayStack

def is_balanced(expression):
    stack = ArrayStack(len(expression))

    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for ch in expression:
        if ch in "([{":
            stack.push(ch)

        elif ch in ")]}":
            if stack.is_empty():
                return False

            if stack.pop() != pairs[ch]:
                return False

    return stack.is_empty()


expr = "{[()]}"
print(is_balanced(expr))
