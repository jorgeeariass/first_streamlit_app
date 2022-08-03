import streamlit as st

import pandas as pd

st.title('Retail Data Analysis')

st.header('Overall')

# Let's put a pick list here so they can pick the fruit they want to include 
# fruits_selected = st.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
# fruits_to_show = my_fruit_list.loc[fruits_selected]

retail_df = pd.read_csv('Retail_Sales.csv', index_col = 'DateTimeIndex')
retail_df.index.name = None

sales_ts = retail_df['Sales']
sales_ts.index = pd.to_datetime(sales_ts.index, format = '%Y-%m-%d')

# Display the table on the page.
st.text('Retail Data')
st.dataframe(retail_df)
