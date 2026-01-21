import re

def sum_numbers_in_string(input_string: str) -> int:
    """
    Находит все целые числа в строке и возвращает их сумму.
    
    Args:
        input_string: Строка, в которой нужно найти числа.
        
    Returns:
        Сумма всех найденных целых чисел.
    """
    total = 0
    current_number = ""
    
    for char in input_string:
        if char.isdigit():
            # Если символ - цифра, добавляем к текущему числу
            current_number += char
        else:
            # Если символ не цифра, заканчиваем текущее число
            if current_number:
                total += int(current_number)
                current_number = ""
    
    # Не забываем про последнее число в строке
    if current_number:
        total += int(current_number)
    
    return total


def sum_numbers_in_string_regex(input_string: str) -> int:
    """
    Находит все целые числа в строке и возвращает их сумму.
    
    Args:
        input_string: Строка, в которой нужно найти числа.
        
    Returns:
        Сумма всех найденных целых чисел.
    """
    numbers = re.findall(r'\d+', input_string)
    return sum(int(num) for num in numbers)