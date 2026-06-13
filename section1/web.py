import streamlit as st
from modules import functions

#url http://localhost:8501/

todos = functions.get_todos()

#title function returns a title instance.
st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for todo in todos:
    st.checkbox(todo)
# st.checkbox("Buy grocery")
# st.checkbox("Throw the trash.")


new_todo = st.text_input(label="", placeholder="Add new todo... ")
todos = functions.get_todos()
todos.append(new_todo)

functions.write_todos(todos)
    