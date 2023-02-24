num = int(input())
num1 = num//100
num2 = (num%100)//10
num3 = ((num%100)%10)//1

if num1 < num2 and num2 < num3:
    print(f'O número {num} é ascendente')
else:
    print(f'O número {num} não é ascendente')