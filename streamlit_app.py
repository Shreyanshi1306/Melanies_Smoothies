# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col
import requests

# Write directly to the app
st.title(":tropical_drink: Customize your Smoothie :tropical_drink:")
st.write(
    """Choose fruits you want in your custom SMOOTHIE!"
    """
)
cnx = st.connection("snowflake")
session = cnx.session()

Enter_Name = st.text_input('Name on Smoothie...!')
st.write('Name on the Smoothie will be : ', Enter_Name)
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)

ingredients_list = st.multiselect(
        'Choose upto 5 fruits :', my_dataframe, max_selections = 5)
if ingredients_list:
    #st.write('Fruits selected', ingredients_list)
    #st.text(ingredients_list)
    ingredients_string = ''
    for fruit_chosen in ingredients_list:
        ingredients_string += fruit_chosen + ' '
    #st.write(ingredients_string)

    my_insert_stmt = """ insert into smoothies.public.orders(ingredients,name_on_order)
            values ('""" + ingredients_string + """','"""+ Enter_Name + """')"""
    #st.write(my_insert_stmt)
    #st.stop

    if time_to_insert:
        session.sql(my_insert_stmt).collect()
        st.success('Your Smoothie is ordered! '+ Enter_Name+'.',icon="✅")


 # New section to display the Fruitvice Nutrition Information.
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
st.text(fruityvice_response)
