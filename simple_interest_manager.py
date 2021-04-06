import pandas as pd
import streamlit as st

"""
# Investment calculator

Hello! This is a very simple investment calculator. 
I developed this app as a way to practice my software skills (from back-end to front-end).
Here you can perform simple simulations of a single investment through a limited number of periods, 
which will be increased by a fixed interest rate and taxes will be paid over the rend recieved. 
Try it out!
"""
init_amount = st.number_input(
    "Insert here the initial investment amount",
    min_value=0.00,
    step=0.01,
    help="Only positive values allowed",
)
periods = st.number_input(
    "Insert here the number of periods you intend to mantain your investment",
    min_value=0,
    step=1,
    help="Only positive values allowed",
)
interest_rate = st.number_input(
    "Insert here the interest rate (%) expected from your investment. This rate will be applied to your initial amount for each period of investment",
    min_value=0.0,
    step=0.1,
    help="Only positive values. Only numbers. If your expected interest rate is 10%, enter the number 10",
)
tax_rate = st.number_input(
    "Insert here the tax rate expected to be collected from your investment's revenue",
    min_value=0.0,
    step=0.1,
    help="Only positive values allowed. Only numbers. If the expected tax rate is 20%, enter 20",
)

total_interest = (1 + (interest_rate / 100)) ** periods

final_amount = init_amount * total_interest

net_before_taxes = final_amount - init_amount

total_taxes = net_before_taxes * (tax_rate / 100)

net_after_taxes = net_before_taxes - total_taxes

"""
# Results:
"""

"""
## At the end, your final amount will be:
"""
final_amount

""" 
## Which means that your total gain (final - initial) is:
"""
net_before_taxes

"""
## Then, you will have to pay the value below in the form of taxes
"""
total_taxes

"""
## Which means that you will have a total net amount after taxes of:
"""
net_after_taxes