import streamlit as st
import pandas as pd
import yfinance as yf
from mongo import insert_user_name, find_user_name, update_user_name


def get_all_data(user_name: str):
    """Fetch data for a given username from the database."""
    data = find_user_name(user_name)
    return data


def run():
    st.title('User Management System')
    search_user_name = st.text_input("Enter a username to search:", key='search')

    if search_user_name:
        data = get_all_data(search_user_name)
        if data:  # Ensure data is not None or empty
            print(data)
            amount = data[0].get('amount', None)
            stock = data[0].get('stock', None)
            st.write(stock)
            if st.button('update'):
                update_user_name(user_name=search_user_name, new_amount=10)
            if amount is not None:
                st.write(f"Amount for user {search_user_name}: {amount}")
            else:
                st.write(f"No 'amount' key found for user: {search_user_name}")
        else:
            st.write(f"No data found for user: {search_user_name}")
