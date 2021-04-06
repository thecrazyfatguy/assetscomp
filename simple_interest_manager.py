import pandas as pd
import streamlit as st



language = st.sidebar.selectbox("", ['Português', 'English'])
if language == 'English':
    st.sidebar.write(
        """
        ### Select your preferred language
        """
        )

if language == 'Português':
    st.sidebar.write(
        """
        ### Selecione seu idioma preferido
        """
        )

if language == 'English':
    """
    # Investment calculator

    Hello! This is a very simple investment calculator. 
    I developed this app as a way to practice my software skills (from back-end to front-end).
    Here you can perform simple simulations of a single investment through a limited number of periods, 
    which will be increased by a fixed interest rate and taxes will be paid over the rent recieved. 
    Try it out!
    """

if language == 'Português':
    """
    # Calculadora de investimentos

    Olá! Esta é uma calculadora de investimentos muito simples.
    Eu desenvolvi este app como uma forma de praticar minhas habilidades de softwar (do back-end ao front-end).
    Aqui voce pode realizar simulações simples de um único investimento ao longo de um limitado número de períodos,
    o valor deste investimento crescerá segundo uma taxa de juros fixa e impostos serão pagos sobre o rendimento recebido.
    Experimente
    """

if language == 'English':
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

if language == 'Português':
    init_amount = st.number_input(
        "Insira aqui o valor do investimento inicial",
        min_value=0.00,
        step=0.01,
        help="Apenas valores positivos são permitidos",
    )
    periods = st.number_input(
        "Insira aqui o número de períodos que você pretende manter o valor investido",
        min_value=0,
        step=1,
        help="Apenas valores positivos são permitidos",
    )
    interest_rate = st.number_input(
        "Insira aqui a taxa de juros (%) esperada neste investimento para cada período.",
        min_value=0.0,
        step=0.1,
        help="Apenas valores positivos. Apenas números. Se sua taxa de juros esperada for de 10%, insira o número 10",
    )
    tax_rate = st.number_input(
        "Insira aqui a taxa do imposto a ser cobrado sobre o rendimento do investimento",
        min_value=0.0,
        step=0.1,
        help="Apenas valores positivos são permitidos. Se o percentual de imposto esperado for de 20%, insira 20",
    )

total_interest = (1 + (interest_rate / 100)) ** periods

final_amount = init_amount * total_interest

net_before_taxes = final_amount - init_amount

total_taxes = net_before_taxes * (tax_rate / 100)

net_after_taxes = net_before_taxes - total_taxes

final_amount = round(final_amount,2)
net_before_taxes = round(net_before_taxes,2)
total_taxes = round(total_taxes,2)
net_after_taxes = round(net_after_taxes,2)

if language == 'English':
    left_column, right_column = st.beta_columns(2)
    pressed = left_column.button('Calculate?')
    if pressed:

        """
        # Results:
        """

        """
        ### At the end, your final amount will be:
        """
        f'US$ {final_amount}'

        """ 
        ### Which means that your total gain (final - initial) is:
        """
        f'US$ {net_before_taxes}'

        """
        ### Then, you will have to pay the value below in the form of taxes
        """
        f'US$ {total_taxes}'

        """
        ### Which means that you will have a total net amount after taxes of:
        """
        f'US$ {net_after_taxes}'

if language == 'Português':
    left_column, right_column = st.beta_columns(2)
    pressed = left_column.button('Calcular?')
    if pressed:

        """
        # Resultados:
        """

        """
        ### No final, seu valor total investido será:
        """
        f'R$ {final_amount}'

        """ 
        ### O que significa que seu rendimento total será:
        """
        f'R$ {net_before_taxes}'

        """
        ### Então, você terá que pagar o valor abaixo sob a forma de impostos:
        """
        f'R$ {total_taxes}'

        """
        ### O que significa que você terá um ganho líquido após impostos de:
        """
        f'R$ {net_after_taxes}'