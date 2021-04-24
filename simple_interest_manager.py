import pandas as pd
import streamlit as st

# Language dictionary to allow more than one language
language_dictionary = {
    "English": {
        "sidebar_title": """
        ### Select your preferred language
        """,
        "app_title": "Investment calculator: fixed income",
        "app_intro": """

    Hello! This is a very simple investment calculator. 
    I developed this app as a way to practice my software skills (from back-end to front-end).
    Here you can perform simple simulations of a single investment through a limited number of periods, 
    which will be increased by a fixed interest rate and taxes will be paid over the rent recieved. 
    Try it out!
    """,
        "init_amount_body": """ ## Insert here the initial investment amount""",
        "init_amount_help": "Only positive values allowed",
        "init_amount_answ": "Initial amount inserted: US$ ",
        "periods_body": """ ## Insert here the number of months you intend to mantain your investment""",
        "periods_help": "Only positive values allowed",
        "periods_answ": "Number of months inserted: ",
        "deposits_body": """ ## Insert here the value of the monthly deposits - if there will be no monthly deposits, enter zero""",
        "deposits_help": "Only positive values allowed",
        "deposits_answ": "Monthly deposit inserted: ",
        "periodicity_radio_body": """ ### Is the interest rate added monthly or annual?""",
        "periodicity_anual_option": "Annual",
        "periodicity_month_option": "Monthly",
        "interest_rate_body": """ ## Insert here the interest rate (%) expected from your investment.""",
        "interest_rate_help": "Only positive values. Only numbers. If your expected interest rate is 10%, enter the number 10",
        "interest_rate_answ": "Interest rate inserted: ",
        "tax_rate_body": """ ### The tax rate is defined here accordingly to the number of periods the investment will be held.""",
        "tax_rate_help_title": "To better understand the tax rate, click here",
        "tax_rate_help": "The taxes collected over the revenue of fixed income assets in Brazil usually are regressive, meaning that the percentage of taxes charged decreases with time. Long term investments pays less taxes. The percentages by period of time are: until 6 months, 22.5%; From 7 to 12 months, 20%; From 13 to 24 months, 17.5%; Beyond 24 months, 15%",
        "tax_rate_answ": """ ### Tax rate to be collected: """,
        "calculate_buttom": "Calculate",
        "results_title": """
        # Results:
        """,
        "final_amount_title": """
        ### At the end, your final amount will be:
        """,
        "net_before_taxes_title": """ 
        ### Which means that your total revenue before taxes is:
        """,
        "total_taxes_title": """
        ### Then, you will have to pay the value below in the form of taxes
        """,
        "net_after_taxes_title": """
        ### Which means that you will have a total net amount after taxes of:
        """,
        "money": "US$ ",
    },
    "Português": {
        "sidebar_title": """
        ### Selecione seu idioma preferido
        """,
        "app_title": "Calculadora de investimentos: renda fixa",
        "app_intro": """

    Olá! Esta é uma calculadora de investimentos muito simples.
    Eu desenvolvi este app como uma forma de praticar minhas habilidades de software (do back-end ao front-end).
    Aqui você pode realizar simulações simples de um único investimento ao longo de um limitado número de períodos,
    o valor deste investimento crescerá segundo uma taxa de juros fixa e impostos serão pagos sobre o rendimento recebido.
    Experimente!
    """,
        "init_amount_body": """ ## Insira aqui o valor do investimento inicial""",
        "init_amount_help": "Apenas valores positivos são permitidos",
        "init_amount_answ": "Montante inicial inserido: R$ ",
        "periods_body": """ ## Insira aqui o número de meses que você pretende manter o valor investido""",
        "periods_help": "Apenas valores positivos são permitidos",
        "periods_answ": "Total de meses inseridos: ",
        "deposits_body": """ ## Insira aqui o valor do deposito mensal - se não houver depósito mensal, coloque zero""",
        "periods_help": "Only positive values allowed",
        "periods_answ": "Monthly deposit inserted: ",
        "periodicity_radio_body": """ ### A taxa de juros inserida é anual ou mensal?""",
        "periodicity_anual_option": "Anualmente",
        "periodicity_month_option": "Mensalmente",
        "interest_rate_body": """ ## Insira aqui a taxa de juros (%) esperada deste investimento.""",
        "interest_rate_help": "Apenas valores positivos. Apenas números. Se sua taxa de juros esperada for de 10%, insira o número 10",
        "interest_rate_answ": "Taxa de juros inserida: ",
        "tax_rate_body": """ ### O percentual de imposto é definido aqui de acordo com o número de meses que o investimento será mantido.""",
        "tax_rate_help_title": "Para melhor entender o percentual de imposto, clique aqui",
        "tax_rate_help": "Os percentuais do imposto cobrado sobre a renda de ativos de renda fixa no Brasil normalmente são regressivos, o que significa que o percentual das taxas cobradas se reduz com o tempo. Investimentos de longo prazo pagam menos imposto. Os percentuais por período de tempo são: até 6 meses, 22.5%; De 7 até 12 meses, 20%; De 13 até 24 meses, 17.5%; Acima de 24 meses, 15%",
        "tax_rate_answ": """ ### Percentual de imposto a ser cobrado: """,
        "calculate_buttom": "Calcular",
        "results_title": """
        # Resultados:
        """,
        "final_amount_title": """
        ### No final, seu valor total investido será:
        """,
        "net_before_taxes_title": """ 
        ### O que significa que seu rendimento total antes dos impostos será:
        """,
        "total_taxes_title": """
        ### Então, você terá que pagar o valor abaixo sob a forma de impostos:
        """,
        "net_after_taxes_title": """
        ### O que significa que você terá um ganho líquido após impostos de:
        """,
        "money": "R$ ",
    },
}

# Selectbox for language choosing and selected language message
container = st.sidebar.beta_container()
language = st.sidebar.selectbox("", ["Português", "English"])
container.write(language_dictionary[language]["sidebar_title"])

# Title and introduction for the app
st.title(language_dictionary[language]["app_title"])
st.write(language_dictionary[language]["app_intro"])

"===================================================="

# Inserting the initial amount of investment
language_dictionary[language]["init_amount_body"]
init_amount = st.number_input(
    "",
    min_value=0,
    step=100,
    help=language_dictionary[language]["init_amount_help"],
)
st.write(
    language_dictionary[language]["init_amount_answ"],
    "{:,}".format(round(init_amount, 2)),
)

"\n"
"\n"
"\n"
# Inserting the number of periods the investment will take place
language_dictionary[language]["periods_body"]
periods = st.number_input(
    "",
    min_value=0,
    step=1,
    help=language_dictionary[language]["periods_help"],
)
st.write(language_dictionary[language]["periods_answ"], "{:,}".format(periods))

"\n"
"\n"
"\n"

# Inserting the value of monthly deposits
language_dictionary[language]["deposits_body"]
periods = st.number_input(
    "",
    min_value=0,
    step=1,
    help=language_dictionary[language]["deposits_help"],
)
st.write(language_dictionary[language]["deposits_answ"], "{:,}".format(periods))

"\n"
"\n"
"\n"
# Inserting the interest rate
language_dictionary[language]["interest_rate_body"]
interest_rate = st.number_input(
    "",
    min_value=0.0,
    step=0.1,
    help=language_dictionary[language]["interest_rate_help"],
)
st.write(
    language_dictionary[language]["interest_rate_answ"],
    "{:,}".format(round(interest_rate, 2)),
    "%",
)

# Choosing if the interest rate will be calculated monthly or anually
language_dictionary[language]["periodicity_radio_body"]
interest_choice = st.radio(
    "",
    [
        language_dictionary[language]["periodicity_anual_option"],
        language_dictionary[language]["periodicity_month_option"],
    ],
)

"\n"
"\n"
"\n"
# Setup buttom to calculate
left_column, right_column = st.beta_columns(2)
pressed = left_column.button(language_dictionary[language]["calculate_buttom"])


if pressed:
    # Define tax rate based on the number of periods
    if periods <= 6:

        tax_rate = 0.225

    elif (periods > 6) & (periods <= 12):

        tax_rate = 0.2

    elif (periods > 12) & (periods <= 24):

        tax_rate = 0.175

    else:

        tax_rate = 0.15

    # Transform the interest rate into index number
    interest_rate = interest_rate / 100

    # If the inserted interest rate is anual, transform it into monthly
    if interest_choice == language_dictionary[language]["periodicity_anual_option"]:

        interest_rate = ((interest_rate + 1) ** (1 / 12)) - 1

    # Calculate the total interest
    total_interest = (1 + interest_rate) ** periods

    # Calculate the final amount of money
    final_amount = init_amount * total_interest

    # Calculate the income achieved in the investment
    net_before_taxes = final_amount - init_amount

    # Calculate total taxes that will be paid over the investment
    total_taxes = net_before_taxes * tax_rate

    # Calculate the net (after taxes) income
    net_after_taxes = net_before_taxes - total_taxes

    # Rounds the resulting values
    final_amount = round(final_amount, 2)
    net_before_taxes = round(net_before_taxes, 2)
    total_taxes = round(total_taxes, 2)
    net_after_taxes = round(net_after_taxes, 2)

    # Show results - title
    language_dictionary[language]["results_title"]

    # Show results - final amount
    language_dictionary[language]["final_amount_title"]
    st.write(language_dictionary[language]["money"], final_amount)

    # Show results - amount before taxes
    language_dictionary[language]["net_before_taxes_title"]
    st.write(language_dictionary[language]["money"], net_before_taxes)

    # Show results - tax rate
    st.write(
        language_dictionary[language]["tax_rate_answ"],
        round(tax_rate, 4) * 100,
        "%",
    )

    # Informative about the tax rate
    # language_dictionary[language]["tax_rate_body"]

    with st.beta_expander(language_dictionary[language]["tax_rate_help_title"]):

        st.write(language_dictionary[language]["tax_rate_help"])

    # Show results - amount paid in taxes
    language_dictionary[language]["total_taxes_title"]
    st.write(language_dictionary[language]["money"], total_taxes)

    # Show results - amount after taxes
    language_dictionary[language]["net_after_taxes_title"]
    st.write(language_dictionary[language]["money"], net_after_taxes)
