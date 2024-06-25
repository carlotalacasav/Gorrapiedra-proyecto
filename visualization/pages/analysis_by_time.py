import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import calendar
import seaborn as sns

# Read the CSV file
@st.cache_data
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

# Function to calculate average percentage_docks_available per month and year
def average_percentage_docks_available_per_month_year(df):
    df['date'] = pd.to_datetime(df[['year', 'month']].assign(day=1))
    avg_percentage = df.groupby('date')['percentage_docks_available'].mean()
    return avg_percentage

# Function to calculate average percentage_docks_available per day of the week
def average_percentage_docks_available_per_day_of_week(df):
    df['date'] = pd.to_datetime(df[['year', 'month', 'day']])
    df['day_of_week'] = df['date'].dt.day_name()
    avg_percentage = df.groupby('day_of_week')['percentage_docks_available'].mean()
    return avg_percentage

# Function to calculate average percentage_docks_available per month (across all years)
def average_percentage_docks_available_per_month(df):
    df['date'] = pd.to_datetime(df[['year', 'month']].assign(day=1))
    avg_percentage = df.groupby(df['date'].dt.month)['percentage_docks_available'].mean()
    return avg_percentage

# Streamlit configuration
st.set_page_config(
    page_title="Data Analysis by Time",
    page_icon="👋",
)

st.title("Data Analysis")

# File upload and processing

df = load_data("../full_dataframe.csv")
st.write("Dataset Loaded.")

# Calculate average percentage_docks_available per month and year
avg_percentage_per_month_year = average_percentage_docks_available_per_month_year(df)

# Calculate average percentage_docks_available per day of the week
avg_percentage_per_day_of_week = average_percentage_docks_available_per_day_of_week(df)

# Calculate average percentage_docks_available per month (across all years)
avg_percentage_per_month = average_percentage_docks_available_per_month(df)

# Plotting
fig1, ax1 = plt.subplots(figsize=(8, 6))
ax1.plot(avg_percentage_per_month_year.index, avg_percentage_per_month_year.values, marker='o', color='skyblue')
ax1.set_xlabel('Date')
ax1.set_ylabel('Average Percentage Docks Available')
ax1.set_title('Average Percentage Docks Available per Month and Year')
plt.xticks(rotation=45)
st.pyplot(fig1)

fig2, ax2 = plt.subplots(figsize=(8, 6))
avg_percentage_per_day_of_week = avg_percentage_per_day_of_week.reindex(list(calendar.day_name))  # Convert to list
ax2.bar(avg_percentage_per_day_of_week.index, avg_percentage_per_day_of_week.values, color='skyblue')
ax2.set_xlabel('Day of the Week')
ax2.set_ylabel('Average Percentage Docks Available')
ax2.set_title('Average Percentage Docks Available per Day of the Week')
st.pyplot(fig2)

fig3, ax3 = plt.subplots(figsize=(8, 6))
ax3.bar(avg_percentage_per_month.index, avg_percentage_per_month.values, color='skyblue')
ax3.set_xlabel('Month')
ax3.set_ylabel('Average Percentage Docks Available')
ax3.set_title('Average Percentage Docks Available per Month (All Years)')
ax3.set_xticks(range(1, 13))
ax3.set_xticklabels(calendar.month_name[1:], rotation=45)
st.pyplot(fig3)

# Pivot table to calculate average docks availability by hour and day
pivot_table = df.pivot_table(index='hour', columns='day_of_week', values='percentage_docks_available', aggfunc='mean')

# Plotting heatmap
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(pivot_table, cmap='YlGnBu', annot=True, fmt='.1f', cbar_kws={'label': 'Average Percentage Docks Available'}, ax=ax)
ax.set_title('Average Percentage Docks Available by Hour and Day of the Week')
ax.set_xlabel('Day of the Week')
ax.set_ylabel('Hour of the Day')
st.pyplot(fig)
