import math

print("\nEste programa calcula a área de um triângulo.")

try:
    escolha_usuario = int(input("\nDigite um número (1 - Lados | 2 - Coordenadas): "))

    if escolha_usuario == 1:
        lado_a = float(input("\nDigite o lado a: "))
        lado_b = float(input("Digite o lado b: "))
        lado_c = float(input("Digite o lado c: "))

        if (lado_a + lado_b > lado_c) and (lado_a + lado_c > lado_b) and (lado_b + lado_c > lado_a):
            semi_perimetro = (lado_a + lado_b + lado_c) / 2
            area = math.sqrt(semi_perimetro * (semi_perimetro - lado_a) * (semi_perimetro - lado_b) * (semi_perimetro - lado_c))
            print(f"\nA triangle with sides ({lado_a:.2f}, {lado_b:.2f}, and {lado_c:.2f}) has an area of {area:.2f}.")
        else:
            print("\nOs valores informados não podem formar um triângulo.")

    elif escolha_usuario == 2:
        try:
            x0, y0 = map(float, input(f"x0, y0 = ").split())
            x1, y1 = map(float, input(f"x1, y1 = ").split())
            x2, y2 = map(float, input(f"x2, y2 = ").split())

            lado_a = math.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2) 
            lado_b = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) 
            lado_c = math.sqrt((x0 - x2) ** 2 + (y0 - y2) ** 2) 

            if (lado_a + lado_b > lado_c) and (lado_a + lado_c > lado_b) and (lado_b + lado_c > lado_a):
                semi_perimetro = (lado_a + lado_b + lado_c) / 2
                area = math.sqrt(semi_perimetro * (semi_perimetro - lado_a) * (semi_perimetro - lado_b) * (semi_perimetro - lado_c))
                print(f"\nA triangle with vertices ({x0}, {y0}), ({x1}, {y1}), and ({x2}, {y2}) has an area of {area:.2f}.")
            else:
                print("Os valores informados não podem formar um triângulo.")
                
        except ValueError:
            print("\nEntrada inválida. Digite os dois números separados por um espaço. Exemplo: (10 20)")
    else:
        print("\nOpção inválida. Por favor, digite 1 ou 2.")
except ValueError:
    print("\nEntrada inválida. Por favor, digite um número inteiro.")