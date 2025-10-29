# Fungsi untuk memeriksa apakah sebuah bilangan genap
def is_even(num):
    return num % 2 == 0

# Tes fungsi
print(is_even(4))   # True
print(is_even(7))   # False

# Fungsi untuk menghitung faktorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        hasil = 1
        for i in range(2, n + 1):
            hasil *= i
        return hasil

# Tes fungsi
print(factorial(5))  # 120
print(factorial(0))  # 1