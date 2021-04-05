import pandas as pd
import numpy as np

def total_interest_calculator(periods, interest_rate):

    total_interest = ((1+ interest_rate)**periods)

    return total_interest

def final_amount_calculator(total_interest, init_amount):

    final_amount = init_amount * total_interest

    return final_amount


if __name__=="__main__":
    init_amount = 1000

    periods = 6

    interest_rate = 0.1

    total_interest = total_interest_calculator(periods = periods, interest_rate = interest_rate)

    print(f"The final calculated amount of the investment is: ,{total_interest-1}")

    final_amount = final_amount_calculator(total_interest = total_interest, init_amount = init_amount)

    print(f"The final calculated amount of the investment is: ,{final_amount}")