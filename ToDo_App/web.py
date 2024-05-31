import streamlit as st
import functions as func

todos = func.get_todos()
def add_todo():
    if st.session_state['new_todo'] != '':
        todo = st.session_state['new_todo'] + '\n'
        todos.append(todo)
        func.write_todos(todos)


st.title('My ToDo App')
st.subheader('This is my todo app')
st.write('This app is to increase your productivity')


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        func.write_todos(todos)
        del st.session_state[todo]
        st.rerun()
    st.session_state['new_todo'] = ''


st.text_input(label='Enter a todo', label_visibility='hidden', placeholder='Add a new todo...',
              on_change=add_todo, key='new_todo')
st.session_state
