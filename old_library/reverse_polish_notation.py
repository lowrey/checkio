#Associativity constants for operators
LEFT_ASSOC = 0
RIGHT_ASSOC = 1
 
#Supported operators
OPERATORS = {
    '+' : (0, LEFT_ASSOC),
    '-' : (0, LEFT_ASSOC),
    '*' : (5, LEFT_ASSOC),
    '/' : (5, LEFT_ASSOC),
    '%' : (5, LEFT_ASSOC),
    '^' : (10, RIGHT_ASSOC)
}
 
#Test if a certain token is operator
def isOperator(token):
    return token in OPERATORS.keys()
 
#Test the associativity type of a certain token
def isAssociative(token, assoc):
    if not isOperator(token):
        raise ValueError('Invalid token: %s' % token)
    return OPERATORS[token][1] == assoc
 
#Compare the precedence of two tokens
def cmpPrecedence(token1, token2):
    if not isOperator(token1) or not isOperator(token2):
        raise ValueError('Invalid tokens: %s %s' % (token1, token2))
    return OPERATORS[token1][0] - OPERATORS[token2][0]    

def checkio(expression):
    'transform the expression'
    out = []
    stack = []
    for token in expression:
        if isOperator(token):
            # If token is an operator
            while len(stack) != 0 and isOperator(stack[-1]):
                if (isAssociative(token, LEFT_ASSOC)and cmpPrecedence(token, stack[-1]) <= 0) or (isAssociative(token, RIGHT_ASSOC) and cmpPrecedence(token, stack[-1]) < 0):
                    out.append(stack.pop())
                    continue
                break
            stack.append(token)
        elif token == '(':
            stack.append(token) 
        elif token == ')':
            while len(stack) != 0 and stack[-1] != '(':
                out.append(stack.pop())
            stack.pop()
        else:
            out.append(token)
    while len(stack) != 0:
        out.append(stack.pop())
    return "".join(out)

if __name__ == '__main__':
    assert checkio('a+b') == 'ab+', 'First'
    assert checkio('((a+b)*(z+x))') == 'ab+zx+*', 'Second'
    assert checkio('((a+t)*((b+(a+c))^(c+d)))') == 'at+bac++cd+^*', 'Third'
    assert checkio('a+b*c+d') == 'abc*+d+' , 'Fourth'
    print('All ok')
