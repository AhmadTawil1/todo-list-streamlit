import streamlit as st
import functions


# Get todos from the file
todos = functions.get_todos()

# Function to add a new _todo
def add_todo():
    new_todo = st.session_state["new_todo"].strip()
    if new_todo:
        todos.append(new_todo + "\n")
        functions.write_todos(todos)
        st.session_state["new_todo"] = "" # Clear input field
        st.success(f"Task '{new_todo}' added!")  # Show success message for added task


# Streamlit App UI
st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")


# Display todos with checkboxes
for index,todo in enumerate(todos):
    if st.checkbox(todo.strip(), key=f"todo_{index}"):
        todos.pop(index)
        functions.write_todos(todos)
        st.rerun() # Rerun the app to update the list



# Input box to add new todos
st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')
