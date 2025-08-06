#n = int(input("Digite um valor: R$"))
#cont100 = 0;
#cont50 = 0;
#cont10 = 0;
#cont1 = 0;

#cont100 = n//100;
#n = n%100;
#cont50 = n//50;
#n = n%50;
#cont10 = n//10;
#n = n%10;
#cont1 = n//1;
#n = n%1;

#print("Notas de 100 reais: ", cont100);
#print("Notas de 50 reais: ", cont50);
#print("Notas de 10 reais: ", cont10);
#print("Notas de 1 reais: ", cont1);

#----------

#t = int(input("Digite o tempo total em segundos: "))

#segundos = t%60;
#t //= 60;
#minutos = t%60
#t //= 60;
#horas = t;
#print("Horas: ", horas, "\nMinutos: ", minutos, "\nSegundos: ", segundos);

#n1 = float(input("Número 1: "))
#n2 = float(input("Número 2: "))

#print(n1, " + ", n2, ": ", n1+n2);
#print(n1, " - ", n2, ": ", n1-n2);
#print(n1, " x ", n2, ": ", n1*n2);
#print(n1, " / ", n2, ": ", n1/n2);

#----------

#print("FATORIAL DE 9 (9!)\n")
#n = 8;
#fat = 9;
#for i in range (8):
#    fat *= n;
#    print("9 x ", n, ": ", fat)
#    n -= 1;

#print ("Valor final: ", fat)

#----------

#print("FATORIAL DE 9 (9!)\n")
#contador = 8;
#fat = 9;

#while contador > 0:
#    fat = fat*contador;
#    contador -= 1;

#print("Valor final: ", fat);

#----------
print("CALCULADORA\n1- Adição\n2- Subtração\n3- Multiplicação\n4- Divisão")
op = int(input("Digite a opção: "))

match op:
    case 1:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print(num1, " + ", num2, " = ", num1+num2)
    case 2:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print(num1, " - ", num2, " = ", num1-num2)    
    case 3:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print(num1, " x ", num2, " = ", num1*num2)    
    case 4:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print(num1, " / ", num2, " = ", num1/num2)    
    case _:
        print("Opção invalida.")
