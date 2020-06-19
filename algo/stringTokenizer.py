def stringTokenizer(string, delimiter):
    result = []
    tmp = ''

    for ch in string:
        if ch in delimiter:
            # 두 자릿수 이상 숫자와 공백 처리
            if tmp != '':
                result.append(tmp)
                tmp = ''
            result.append(ch)
        else:
            tmp += ch
            if ch == string[-1]:
                result.append(tmp)
    
    return result

# 중위표기법(Infix) -> 후위표기법(Postfix)
def toPostfix(infix):
    expr = {
        '+' : 1, 
        '-' : 1,
        '*' : 2,
        '/' : 2, 
        '(' : 0
    }
    stack = []
    result = []
    for ch in infix:
        if ch == '(':
            stack.append(ch)
            
        elif ch in '+-*/^':
            if not stack:
                stack.append(ch)
            else:
                if expr[stack[-1]] >= expr[ch]:
                    result.append(stack.pop())
                    stack.append(ch)
                else:
                    stack.append(ch)
        elif ch == ')':
            while True:
                tmp = stack.pop()
                if tmp == '(':
                    break
                result.append(tmp)
        else:
            result.append(ch)
    
    while stack:
        result.append(stack.pop())
    
    # return ''.join(result)
    return result

def calculate(postfix):
    def calc(num1, operand, num2):
        if operand == '*':
            return num1 * num2
        elif operand == '/':
            return num1 / num2
        elif operand == '+':
            return num1 + num2
        else:
            return num1 - num2

    operand = []

    for token in postfix:
        if token not in '+-*/^':
            # float 타입 처리
            if '.' in token:
                operand.append(float(token))    
            else:
                operand.append(int(token))
        else:
            num2 = operand.pop()
            num1 = operand.pop()
            result = calc(num1, token, num2)
            operand.append(result)
    
    return operand.pop()

# string = '11+2*(3-4)'
# string = '11+2*3-4'
# string = '2+3*4'
# string = '2+5*(3+4)'
string = '11.5+2*(3-4)'

print(string, '계산 결과 :', eval(string))

infix = stringTokenizer(string, '+-*/(){}[]^')
print('중위표기법 :', infix)

postfix = toPostfix(infix)
print('후위표기법 :', postfix)

result = calculate(postfix)
print('후위표기법 계산 결과 :', result)