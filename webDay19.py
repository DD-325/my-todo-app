import streamlit as st

import functions as ft



todos =ft.get_todos()


def add_todo():
    # session state is like a dictionary where it stores the entered data
        todo = st.session_state["new_todo"] + '\n'
        # take the ew data and append the existing list
        todos.append(todo)
        # use the function to write out the changes
        ft.write_todos(todos)


st.title('My Todo App')
st.subheader("This is my todo app")
st.write("This is to increase productivity")



for index, todo in enumerate(todos):
    # adding the key here gives each item its own reference we can use from session state data
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        ft.write_todos(todos)
        # deletes the selected item from the session state
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label="", placeholder="Add new todo", on_change=add_todo, key='new_todo')
