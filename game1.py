import numpy as np
def random_predict(number: int=1) -> int:
    """Машина угадывает число

    Args:
        number (int, optional): Загаданное число будет от 1 до 100. Defaults to 1.

    Returns:
        int: Число попыток машины угадать число
    """
    count = 0
    limit1 = 1
    limit2 = 101
    predict_number = np.random.randint(limit1, limit2)
        
    while number != predict_number:
        print(f'number: {number}, predict_number: {predict_number} limit1: {limit1}, limit2: {limit2}')
        # Поскольку дебагинг не освоен в должным образом, можем отслеживать как ведёт себя рандом случайных чисел
        count += 1
        if limit1 == limit2:
            predict_number = limit1
            break
        predict_number = np.random.randint(limit1, limit2)
        if number > predict_number:
            limit1 = predict_number + 1
        else:
            limit2 = predict_number - 1
    
    print(f'Ваше число {predict_number} угадано за {count} попыток (-ки, -у)')     
    return count 
   
print(random_predict(np.random.randint(1, 101)))
