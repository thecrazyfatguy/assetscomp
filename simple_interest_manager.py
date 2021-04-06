import pandas as pd
import numpy as np


def total_interest_calculator(periods, interest_rate):

    total_interest = (1 + interest_rate) ** periods

    return total_interest


def final_amount_calculator(total_interest, init_amount):

    final_amount = init_amount * total_interest

    return final_amount


def net_income_calculator(final_amount, init_amount, tax_rate):

    net_before_taxes = final_amount - init_amount

    total_taxes = net_before_taxes * tax_rate

    net_after_taxes = net_before_taxes - total_taxes

    result = {
        "net_before_taxes": net_before_taxes,
        "net_after_taxes": net_after_taxes,
        "total_taxes": total_taxes,
    }

    return result


if __name__ == "__main__":
    init_amount = 2000

    periods = 12

    interest_rate = 0.01

    tax_rate = 0.225

    total_interest = total_interest_calculator(
        periods=periods, interest_rate=interest_rate
    )

    print(
        f"The final interest rate during the whole period is: {(total_interest-1)*100}%"
    )

    final_amount = final_amount_calculator(
        total_interest=total_interest, init_amount=init_amount
    )

    print(f"The final calculated amount of the investment is: {final_amount}")

    result = net_income_calculator(
        final_amount=final_amount, init_amount=init_amount, tax_rate=tax_rate
    )

    print(f"The profit of the investment before taxes is: {result['net_before_taxes']}")

    print(f"The profit of the investment after taxes is: {result['net_after_taxes']}")

    print(f"The total taxes paid to the government will be: {result['total_taxes']}")
