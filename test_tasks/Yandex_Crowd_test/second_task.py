def even_or_odd(arr: list):
    odd = 'Число нечётное!'
    even = 'Число чётное!'
    
    if len(arr) == 0:
        return "Ошибка: массив пустой!"
    
    elif len(arr) >= 1:
        for i in arr:
            if (i & 1) == 1:
                return odd
        return even

array = [2, 4, 5]
print(even_or_odd(array))   