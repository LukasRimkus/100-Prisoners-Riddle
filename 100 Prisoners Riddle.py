import random


PRISONERS = 100
LIMIT = PRISONERS//2 + 1
NUMBER_OF_EXPERIMENTS = 100


"""
The main method which performs the experiment a give number of times.  
"""
def main():
    numbers = list(range(1, PRISONERS + 1))
    
    results = {True: 0, False: 0}

    # go through some number of times
    for _ in range(NUMBER_OF_EXPERIMENTS):
        random.shuffle(numbers)
        escaped = execute_strategy(numbers)
        results[escaped] += 1
    
    
    print(f"Escaped {results[True]} times, while failed {results[False]}")
    print(f"The percentage of escapes should be about 30%, while it is in this case: {results[True]/NUMBER_OF_EXPERIMENTS*100:.2f}%")


"""
The solution is to pick firstly a number of pa prisoner, then follow where the found number says, etc. It is 
calculated that a probability to finally for all prisoners to escape is about 30%. 

This probability is quite high, because now the probabilities of escaping for each prisoner are not independent (compared
to the random case), as those numbers are going to construct the loops. So if there are no loops bigger than 50 in the original
case or just more than a half of all numbers, then the prisoners are going to escape. 
"""
def execute_strategy(shuffled_numbers):
    # go for each prisoner
    for i in range(1, PRISONERS + 1):
        times = 1
        success = False
        found_number = i

        # it is going to terminate when either a limit is reached or a prisoner escaped
        while times < LIMIT and not success:
            found_number = shuffled_numbers[found_number-1]

            if found_number == i:
                success = True
            
            times = times + 1
        
        # if at least one failed, then all failed 
        if not success:
            return False
    
    return True


if __name__ == "__main__":
    main()