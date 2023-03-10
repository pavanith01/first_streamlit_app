
import streamlit 
streamlit.title('My Parents New Healthy Dinner')
streamlit.header('Breakfast Favorites')
streamlit.text(' ð¥£ Omega 3 & Blueberry Oatmeal')
streamlit.text('ð¥ Kale,Spinach&Rocket Smoothie')
streamlit.text('ð Hard-Boiled Free-Range Egg')
streamlit.text('ð¥ðAvocado Toast')
streamlit.header('ðð¥­ Build Your Own Fruit Smoothie ð¥ð')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')


# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)


###Display fruityvice API
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)


#json version of response and normalize it  
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# putput it the screen as a table
streamlit.dataframe(fruityvice_normalized)
