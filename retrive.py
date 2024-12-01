def romanizer(numbers):
    # Add 1000 ('M') to the list to handle numbers >= 1000
    roman_numerals = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    ]

    result_list = []
    for num in numbers:
        result = []
        for value, symbol in roman_numerals:
            while num >= value:
                result.append(symbol)
                num -= value
        result_list.append(''.join(result))

    return result_list


# Example usage
if __name__ == '__main__':
    numbers = [1, 49, 10, 100, 1000]
    print(romanizer(numbers))  # Output: ['I', 'XLIX', 'X', 'C', 'M']
