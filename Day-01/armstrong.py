def is_armstrong(num):
    original = num
    cube_sum = 0
    while num>0:
        digit = num % 10
        cube_sum+=digit**3
        num = num//10
    return cube_sum == original
num = int(input("Enter the number: "))
if is_armstrong(num):
    print("Armstrong")
else:
    print("Not Armstrong")