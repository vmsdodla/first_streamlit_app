import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
streamlit.title('MyParents new Healthy Diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page.
streamlit.dataframe(fruits_to_show)
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
#create the repeatable code block(called afunction)
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+this_fruit_choice)
  #fruityvice_response = requests.get("http://fruityvice.com/api/fruit/"+this_fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized
#import requests
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    #fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
    #streamlit.text(fruityvice_response.json())
    # write dat to screen? 
    #fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    # Output in screen as table
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
except URLError as e:
    streamlit.error()


streamlit.stop()
#import snowflake.connector

streamlit.header("The FRUIT LOAD LIST contains")
#snowflake-related functions
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur
       my_cur.execute("SELECT * from FRUIT_LOAD_LIST")
       return my_cur.fetchall()  
#add a button to load the fruit
if streamlit.button('get_fruit_load_list'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  #my_cur = my_cnx.cursor()
  #my_data_rows = my_cur.fetchall()
  streamlit.dataframe(my_data_rows)
fruit_choice1 = streamlit.text_input('What fruit would you like to add?','jackfruit')
streamlit.write('Thanks for adding ', fruit_choice1)
my_cur.execute("insert into FRUIT_LOAD_LIST values ('from streamlit')")
