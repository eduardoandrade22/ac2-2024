#ano bisexto

def é_bisexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False

ano = int(input("ano: "))
if é_bisexto(ano):
    print(f"{ano} é bisexto.")
else:
    print(f"{ano} não é bisexto.")


    #salario

def calculate_salary(horas_trabalhadas, salário_por_hora,irpf=0.275):
    salário_pretaxa = horas_trabalhadas * salário_por_hora
    salario_total = salário_pretaxa * irpf
    salário_final = salário_pretaxa - salario_total
    return salário_final


horas = float(input("Tempo de trabalho, em horas no mês: "))
salário_por_hora = float(input("salário por hora: "))
total = calculate_salary(horas, salário_por_hora)
print(f"salário: ${total:.2f}")



#eq seg grau

def eq_seg_grau():
    # Pede os coeficientes da equação
    a = float(input("Digite o coeficiente 'a' da equação: "))
    b = float(input("Digite o coeficiente 'b' da equação: "))
    c = float(input("Digite o coeficiente 'c' da equação: "))

    # discriminante
    delta = b**2 - 4*a*c

    # checa se tem raízes reais
    if delta < 0:
        return "Não existem raízes reais para esta equação"
    elif delta == 0:
        # Se delta igual a 0, tem somente uma raiz real
        raiz = -b / (2*a)
        return raiz
    else:
        # Se delta menor que 0, temo duas raízes reais
        raiz1 = (-b + delta**0.5) / (2*a)
        raiz2 = (-b - delta**0.5) / (2*a)
        return raiz1, raiz2


raizes = eq_seg_grau()
print("Raízes da equação:", raizes)