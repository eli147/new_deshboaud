import streamlit as st
import pandas as pd
import yfinance as yf
from mongo import get_all_users


def run():
    st.title('Get all Users !')
    data = get_all_users()
    st.table(data)
