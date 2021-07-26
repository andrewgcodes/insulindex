import streamlit as st
import streamlit_analytics

with streamlit_analytics.track():
    st.title("The Insulindex")
    st.write("Find out how much of anything you could buy with one vial of Humalog 50/50 insulin!")
    st.write("Inspired by Senator Amy Klobuchar's book, ANTITRUST and the Big Mac Economic Index.")

    item = st.selectbox('Which item do you want to compare?',('Big Mac','Movie Ticket', 'Month of Spotify Premium','AirPods Pro', 'Custom'))
    price = 0
    customItem = False
    if len(item) != 0:
        if(item == 'Big Mac'):
            st.write("According to The Economist, the average price of a Big Mac in 2021 is $5.65.")
            price = 565
        if(item == 'Movie Ticket'):
            st.write("According to the-numbers.com, the average price of a movie ticket in 2021 is $9.16.")
            price = 916
        if(item == 'Month of Spotify Premium'):
            st.write("According to Spotify, the price of one month of Spotify Premium in 2021 is $9.99.")
            price = 999
        if(item == 'AirPods Pro'):
            st.write("According to Apple, the price of AirPods Pro in 2021 is $249.00")
            price = 24900
        if(item == 'Custom'):
            customItem = True
            itemName = st.text_input("What is your item called?")
            price = st.text_input("How much does your item cost?", 5.00)
        st.write("According to drugs.com, Humalog 50/50, a popular insulin product, costs $307 per 10 milliliter vial.")

        st.write("Let's do the math. With the money needed to buy one vial of Humalog 50/50, you could get:")

        if(customItem == False):
            cost = round(30700/price,2)

            st.write(str(cost) + " " + item+"s!")
        else:
            price2 = price.replace(".", "")

            cost = round(307/float(price),2)
            st.write(str(cost) + " " + itemName+"s!")
    st.markdown(
    """<a href="https://andrewgao.dev/">Made by Andrew Gao</a>""", unsafe_allow_html=True)
