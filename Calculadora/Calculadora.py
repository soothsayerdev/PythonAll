def catch_num():
    n1 = float(input("Say a first number: "))
    n2 = float(input("Say a second number: "))

def sum_(n1,n2):
        return n1 + n2

def sub(n1,n2):
    return n1 - n2

def division(n1,n2):
    if n2 != 0:
        return n1 / n2
    else:
         return "Erro: Divisao por zero."

def mult(n1,n2):
     return n1 * n2

def operation(operator,n1,n2):
     operators = {
          "+": sum_,
          "-": sub,
          "/": division,
          "*": mult
     } 
operator = input("Say the operator: ")

def verify_procedure(operators,n1,n2):
    if operator in operators:
        return operation[operator](n1,n2)
    else:
         return "Operation Error"

def result(n1,n2):
    result = operation(operator=operator, n1=n1, n2=n2)
    print("Result: ", result)


catch_num()
verify_procedure(operators= "+",n1=5, n2= 10)
result()




