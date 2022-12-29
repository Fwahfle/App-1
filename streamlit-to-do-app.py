import streamlit as lit
from functions_todoapp import get_todos, write_todos

todos = get_todos()


def add_todo():
    todo = lit.session_state["new_todo"] + "\n" # A dictionary representing events on a webpage
    todos.append(todo)
    write_todos(todos)


# Title of app, sub-headers and description: order in which codes are written affects the order of the texts on the site
lit.title("todo-less")
lit.subheader("Do more, then do less.")
lit.write("Plan your day by writing things to do here.")

# Making widgets like checkboxes
for index, todo in enumerate(todos):
    checkbox = lit.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        write_todos(todos)
        del lit.session_state[todo]
        lit.experimental_rerun()

lit.text_input(label="Enter below:", placeholder="Add a to-do",
               on_change=add_todo, key='new_todo')  # First argument must be put to represent the label, onchange is a callback function
