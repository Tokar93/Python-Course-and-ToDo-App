import streamlit as st
import functions as func

todos = func.get_todos()

st.title('My ToDo App')
st.subheader('This is my todo app')
st.write('This app is to increase your productivity')

for todo in todos:
    st.checkbox(todo)


st.text_input(label='Enter a todo', label_visibility='hidden', placeholder='Add a new todo')

print('Hello')