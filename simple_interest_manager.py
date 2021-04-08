import pandas as pd
import streamlit as st


language_dictionary = {
    "English": {
        'sidebar_title': """
        ### Select your preferred language
        """,
        'app_title': "Investment calculator",
        'app_intro':"""

    Hello! This is a very simple investment calculator. 
    I developed this app as a way to practice my software skills (from back-end to front-end).
    Here you can perform simple simulations of a single investment through a limited number of periods, 
    which will be increased by a fixed interest rate and taxes will be paid over the rent recieved. 
    Try it out!
    """,
    'init_amount_body':""" ## Insert here the initial investment amount""",
    'init_amount_help':"Only positive values allowed",
    'init_amount_answ':'Initial amount inserted: US$ ',
    'periods_body':""" ## Insert here the number of months you intend to mantain your investment""",
    'periods_help':"Only positive values allowed",
    'periods_answ':'Number of months inserted: ',
    'interest_rate_body':""" ## Insert here the monthly interest rate (%) expected from your investment.""",
    'interest_rate_help':"Only positive values. Only numbers. If your expected interest rate is 10%, enter the number 10",
    'interest_rate_answ':'Interest rate inserted: ',
    'tax_rate_body':""" ## Insert here the tax rate expected to be collected from your investment's revenue""",
    'tax_rate_help':"Only positive values allowed. Only numbers. If the expected tax rate is 20%, enter 20",
    'tax_rate_answ':"Tax rate inserted: ",
    'calculate_buttom':'Calculate',
    'results_title':"""
        # Results:
        """,
    'final_amount_title':"""
        ### At the end, your final amount will be:
        """,
    'net_before_taxes_title':""" 
        ### Which means that your total revenue is:
        """,
    'total_taxes_title':"""
        ### Then, you will have to pay the value below in the form of taxes
        """,
    'net_after_taxes_title':"""
        ### Which means that you will have a total net amount after taxes of:
        """,
    'money':"US$ ",
    },
    "Português": {
        'sidebar_title': """
        ### Selecione seu idioma preferido
        """,
        'app_title': "Calculadora de investimentos",
        'app_intro': """

    Olá! Esta é uma calculadora de investimentos muito simples.
    Eu desenvolvi este app como uma forma de praticar minhas habilidades de software (do back-end ao front-end).
    Aqui você pode realizar simulações simples de um único investimento ao longo de um limitado número de períodos,
    o valor deste investimento crescerá segundo uma taxa de juros fixa e impostos serão pagos sobre o rendimento recebido.
    Experimente!
    """,
    'init_amount_body':""" ## Insira aqui o valor do investimento inicial""",
    'init_amount_help':"Apenas valores positivos são permitidos",
    'init_amount_answ':'Montante inicial inserido: R$ ',
    'periods_body':""" ## Insira aqui o número de meses que você pretende manter o valor investido""",
    'periods_help':"Apenas valores positivos são permitidos",
    'periods_answ':'Total de meses inseridos: ',
    'interest_rate_body':""" ## Insira aqui a taxa de juros (%) esperada deste investimento para cada período.""",
    'interest_rate_help':"Apenas valores positivos. Apenas números. Se sua taxa de juros esperada for de 10%, insira o número 10",
    'interest_rate_answ':'Taxa de juros inserida: ',
    'tax_rate_body':""" ## Insira aqui a taxa do imposto a ser cobrado sobre o rendimento do investimento""",
    'tax_rate_help':"Apenas valores positivos são permitidos. Se o percentual de imposto esperado for de 20%, insira 20",
    'tax_rate_answ':"Taxa de imposto inserida: ",
    'calculate_buttom':'Calcular',
    'results_title':"""
        # Resultados:
        """,
    'final_amount_title':"""
        ### No final, seu valor total investido será:
        """,
    'net_before_taxes_title':""" 
        ### O que significa que seu rendimento total será:
        """,
    'total_taxes_title':"""
        ### Então, você terá que pagar o valor abaixo sob a forma de impostos:
        """,
    'net_after_taxes_title':"""
        ### O que significa que você terá um ganho líquido após impostos de:
        """,
    'money':"R$ ",
    },
}

language = st.sidebar.selectbox("", ['Português', 'English'])
st.sidebar.write(
        language_dictionary[language]['sidebar_title']
        )


st.title(language_dictionary[language]['app_title'])
st.write(language_dictionary[language]['app_intro'])

"===================================================="
language_dictionary[language]['init_amount_body']
init_amount = st.number_input(
    '',
    min_value=0,
    step=100,
    help=language_dictionary[language]['init_amount_help'],
)
st.write(language_dictionary[language]['init_amount_answ'], "{:,}".format(round(init_amount, 2)))

"\n"
"\n"
"\n"
language_dictionary[language]['periods_body']
periods = st.number_input(
    '',
    min_value=0,
    step=1,
    help=language_dictionary[language]['periods_help'],
)
st.write(language_dictionary[language]['periods_answ'], "{:,}".format(periods))

"\n"
"\n"
"\n"
language_dictionary[language]['interest_rate_body']
interest_rate = st.number_input(
    '',
    min_value=0.0,
    step=0.1,
    help=language_dictionary[language]['interest_rate_help'],
)
st.write(language_dictionary[language]['interest_rate_answ'], "{:,}".format(round(interest_rate, 2)),"%")

"\n"
"\n"
"\n"
language_dictionary[language]['tax_rate_body']
tax_rate = st.number_input(
    '',
    min_value=0.0,
    step=0.1,
    help=language_dictionary[language]['tax_rate_help'],
)
st.write(language_dictionary[language]['tax_rate_answ'], "{:,}".format(round(tax_rate, 2)),'%')

total_interest = (1 + (interest_rate / 100)) ** periods

final_amount = init_amount * total_interest

net_before_taxes = final_amount - init_amount

total_taxes = net_before_taxes * (tax_rate / 100)

net_after_taxes = net_before_taxes - total_taxes

final_amount = round(final_amount,2)
net_before_taxes = round(net_before_taxes,2)
total_taxes = round(total_taxes,2)
net_after_taxes = round(net_after_taxes,2)

"\n"
"\n"
"\n"
left_column, right_column = st.beta_columns(2)
pressed = left_column.button(language_dictionary[language]['calculate_buttom'])

if pressed:

    language_dictionary[language]['results_title']

    language_dictionary[language]['final_amount_title']
    st.write(language_dictionary[language]['money'],final_amount)

    language_dictionary[language]['net_before_taxes_title']
    st.write(language_dictionary[language]['money'],net_before_taxes)

    language_dictionary[language]['total_taxes_title']
    st.write(language_dictionary[language]['money'],total_taxes)

    language_dictionary[language]['net_after_taxes_title']
    st.write(language_dictionary[language]['money'],net_after_taxes)