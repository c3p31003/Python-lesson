import streamlit as st
from modules import functions

#url http://localhost:8501/

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todo_list = functions.get_todos()
    todo_list.append(todo)
    functions.write_todos(todo_list)
    st.session_state["new_todo"]=""


todos = functions.get_todos()

#title function returns a title instance.
st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for todo in todos:
    st.checkbox(todo)



st.text_input(label="", placeholder="Add new todo... ", 
                         on_change=add_todo, key='new_todo')

st.session_state


    