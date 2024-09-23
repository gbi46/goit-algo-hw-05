import re

def generator_numbers(text: str):
    pattern = r'[-+]?\d*\.?\d+'

    for number in re.finditer(pattern, text):
        yield number.group()

def sum_profit(text: str, func: callable):
    total_profit = 0
    for number in generator_numbers(text):
        total_profit = total_profit + float(number)

    return total_profit

text = "Загальний дохід працівника складається з декількох частин: 1000.05 як основний дохід, доповнений додатковими надходженнями 27.47 і 324.01 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
