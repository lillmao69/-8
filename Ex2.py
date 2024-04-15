def reverse_number(num):
    # Преобразование числа в строку, затем переворот строки и возврат обратно в числовой формат
    return int(str(num)[::-1])

def is_palindrome(num):
    # Преобразование числа в строку и проверка на равенство оригинального числа и его перевернутой версии
    return str(num) == str(num)[::-1]

def process_numbers(nums):
    processed_nums = []
    for num in nums:
        reversed_num = reverse_number(num)
        if is_palindrome(num):
            print(f"{num} является палиндромом!")
        processed_nums.append(reversed_num)
    return processed_nums

# Пример использования
numbers = [123, 456, 121, 555]
processed = process_numbers(numbers)
print("Перевернутые числа:", processed)
