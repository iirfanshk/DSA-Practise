def product_of_non_zero(num):
    product = 1
    while num > 0:
        n = num % 10
        if n != 0:
            product*=n
        num = num//10
    return product
num =int(input("Enter the number: "))
print(product_of_non_zero(num))
