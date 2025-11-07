import numpy as np

end_of_range = 101 
selection = 10000

def game_v3(num: int=1) -> int:
    """The function guess random nomber for 20 trys, from 0 to 1048576.

    Args:
        num (int, optional): the hidden number. Defaults to 1.

    Returns:
        count int: the number of attempts.
    """
    num_lst = list(range(1,end_of_range))
    count = 0
    
    while len(num_lst) >= 4:
        mid_lst = int(len(num_lst)/2 - 1)
        count += 1
        
        if num >= num_lst[mid_lst]:
            num_lst = list(filter(lambda x: True if (x >= num_lst[mid_lst]) else False, num_lst)) 
        if num <= num_lst[mid_lst]:
            num_lst = list(filter(lambda x: True if (x <= num_lst[mid_lst]) else False, num_lst))
        
        if len(num_lst) == 3:
            if (num != num_lst[0]) and (num != num_lst[1]):
                return count
            elif (num != num_lst[0]) and (num != num_lst[2]):
                return count
            elif (num != num_lst[1]) and (num != num_lst[2]):
                return count
        elif len(num_lst) == 2:
            if num == num_lst[0]:
                return count
            elif num == num_lst[1]:
                return count

def score_game(test_function) -> float:
    """The function finds the mean value of attempts for the testing function's.

    Args:
        test_function (_type_): testing function's.
    Returns:
        mean_count float: the mean value of finding a random number.
    """
    np.random.seed(1)
    random_number_list = np.random.randint(1, end_of_range, size=selection)
    mean_count = round(np.mean(list(map(test_function, random_number_list))), 2)
    
    if mean_count:
        return mean_count
         
print(f"The function 'game_v3' guesses a random number in average of {score_game(game_v3)} attempts.")
