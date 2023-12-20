import random

# İlkin siyahını yaratmaq və fayla yazmaq
lst = [random.randint(0, 101) for _ in range(5)]
print("lst = ", lst)

with open('Memmed.txt', 'w') as f:
    f.write(str(len(lst)) + '\n')
    f.write(' '.join(map(str, lst)))

# Fayldan oxumaq və 3-ə bölünən ədədləri tapmaq
with open('file.txt', 'r') as f:
    f.readline()  # Birinci sətiri oxuyub atmaq
    lst2 = list(map(int, f.readline().split()))

# 3-ə bölünən ədədlərin siyahısını və hasilini hesablamaq
    divisible_by_3 = [x for x in lst2 if x % 3 == 0]
    product_of_divisible_by_3 = 1
for num in divisible_by_3:
    product_of_divisible_by_3 *= num

# Nəticələri yeni fayla yazmaq
with open('Netice.txt', 'w') as f:
    f.write(' '.join(map(str, divisible_by_3)) + '\n')
    f.write(str(product_of_divisible_by_3))

print('3-ə bölünən ədədlər:', divisible_by_3)
print('Hasil:', product_of_divisible_by_3)