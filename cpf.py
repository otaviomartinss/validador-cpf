import re
cpf = str(input("Insira o CPF: "))
cpf = re.sub('[^0-9]', '', cpf)
cpf = list(map(int, str(cpf)))
f1 = cpf[0]*1 + cpf[1]*2 + cpf[2]*3 + cpf[3]*4 + cpf[4]*5 + cpf[5]*6 + cpf[6]*7 + cpf[7]*8 + cpf[8]*9
f2 = f1%11
if (f2 == 10): f2 = 0
f3 = cpf[0]*0 + cpf[1]*1 + cpf[2]*2 + cpf[3]*3 + cpf[4]*4 + cpf[5]*5 + cpf[6]*6 + cpf[7]*7 + cpf[8]*8 + f2*9
f4 = f3%11
if (f4 == 10): f4 = 0
if f2 == cpf[9] and f4 == cpf[10]: print("CPF VÁLIDO")
else: print("CPF INVÁLIDO")
