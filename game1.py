import numpy as np
def random_predict(number: int=1) -> int:
    """Угадываем число

    Args:
        number (int, optional): Загаданное число будет от 1 до 100. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    limit1 = 1
    limit2 = 101
    predict_number = np.random.randint(limit1, limit2)
    
    while number != predict_number:
        count += 1
        if number > predict_number:
            limit1 = number
        elif number < predict_number:
            limit2 = number
    return count
print(random_predict(7))