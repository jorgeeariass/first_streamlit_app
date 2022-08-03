import streamlit as st

import pandas as pd

# import matplotlib.pyplot as plt

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

lbls = ['2012','','','','','','','','','','','',
        '2013','','','','','','','','','','','',
        '2014','','','','','','','','','','','',
        '2015','','','','','','','','','','','',
        '2016','','','','','','','','','','','',
        '2017','','','','','','','','','','','',
        '2018','','','','','','','','','','','',
        '2019','','','','','','','','','','','',
        '2020','','','','','','','','','','','',
        '2021','','','','','','','','','','','']

# fig, axs = plt.subplots(nrows = 1,
#                         ncols = 1, 
#                         figsize=(20, 8))

# axs.set_xticklabels(lbls, rotation = 45)
# axs.plot(sales_ts)
# axs.set_title('Total Retail Sales TS', fontweight ="bold");

# st.pyplot(fig)
