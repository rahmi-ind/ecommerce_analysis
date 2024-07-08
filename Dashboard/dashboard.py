import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

# Load cleaned data
sum_order_items_df = pd.read_csv("sum_order_items.csv")
mean_review_score_df = pd.read_csv("mean_review_score.csv")
monthly_orders_df = pd.read_csv("monthly_orders.csv")
highest_orders_city_df = pd.read_csv("highest_orders_city.csv")
customer_segment_df = pd.read_csv("customer_segment.csv")