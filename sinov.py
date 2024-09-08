def list_sum(l1, l2):
    # Ro'yxatlarni stringga aylantirib, ularni sondan foydalanamiz
    num1 = int(''.join(map(str, l1[::-1])))
    num2 = int(''.join(map(str, l2[::-1])))

    # Sonlarni qo'shamiz
    total = num1 + num2

    # Natijani ro'yxat ko'rinishida qaytaramiz
    return [int(i) for i in str(total)][::-1]

# Inputlar
l1 = [2, 4, 3]
l2 = [5, 6, 4]

# Funksiyani chaqirish
result = list_sum(l1, l2)
print(result)  # [7, 0, 8]
