import functions
import FreeSimpleGUI as sg
import time

sg.theme('Dark Blue 2')
clock = sg.Text('', key='clock')

label = sg.Text('Type in a To-do:')
input_box = sg.Input(tooltip = 'Enter todo', key = 'todo')
add_button = sg.Button('Add',key = 'Add', size = 10)


list_box = sg.Listbox(values=functions.get_todos(), key = 'todos',enable_events = True, size =[45,10])
refresh_button = sg.Button('Refresh', key ='Refresh',size = 8)
edit_button = sg.Button('Edit',key ='Edit',size = 8)
delete_button = sg.Button('Delete',size = 8)

right_column_buttons = [[refresh_button],[edit_button],[delete_button]]
right_buttons = sg.Column(right_column_buttons)
exit_button = sg.Button('Exit',size = 8)

layout = [[clock],[label],[input_box,add_button],[list_box,right_buttons],[exit_button]]
window = sg.Window('To-do App',
                   layout=layout,
                   font=('Helvetica', 11))
while True:
    event, values = window.read(timeout = 200)
    window['clock'].update(value=time.strftime('%d %b %Y %H:%M:%S'))
    match event:
        case "Add":
             if values['todo'] == '':
                 sg.popup('Enter a To-do first', font=('Helvetica', 9))
             new_todo = values['todo'] + '\n'
             todos = functions.get_todos()
             if new_todo in todos:
                 sg.popup('To-do already exist',font=('Helvetica',9))
                 window['todo'].update('')
             elif new_todo !='\n':
                 todos.append(new_todo)
                 functions.write_todos(todos)
                 window['todos'].update(values=todos)
                 window['todo'].update('')
             functions.delete_blank_line(todos)
             window['todos'].update(values=todos)
        case "Edit":
            try:
                 todos = functions.get_todos()
                 #Store a Real-time user input in todo_to_edit
                 todo_to_edit = values['todos'][0]
                 index = todos.index(todo_to_edit)
                 todos_buffer = []
                 for index,item in enumerate(todos):
                     todos_buffer.append(item.strip('\n'))
                 new_todo = values['todo'] +'\n'
                 list_todo = new_todo.strip('\n')
                 if list_todo in todos_buffer:
                     sg.popup('To-do already exist',title='Information', font=('Helvetica', 9))
                 else:
                     new_todo = values['todo'] + '\n'
                     index = todos.index(todo_to_edit)
                     todos[index] = new_todo
                     functions.write_todos(todos)
                     #show in real-time the todo_edited in the listbox after file is updated
                     window['todos'].update(values=todos)
                 window['todo'].update('')
                 window['Add'].update(disabled=False)
            except IndexError:
                 sg.popup('Please select a To-do first.',font=('Helvetica',9))
            functions.delete_blank_line(todos)
            window['todos'].update(values=todos)
        case 'todos':
             if event == 'todos':
                window['Add'].update(disabled=True)
             #show a real-time todo_selection by user from listbox in the Add input_box
             window['todo'].update(value=values['todos'][0])
        case 'Delete':
             try:
                 todos = functions.get_todos()
                 todo_to_delete = values['todos'][0]
                 todos.remove(todo_to_delete)
                 functions.write_todos(todos)
                 window['todos'].update(values=todos)
                 window['todo'].update(value='')
                 window['Add'].update(disabled=False)
             except IndexError:
                 sg.popup('Please select a To-do first', font=('Helvetica', 9))
             except ValueError:
                 pass
        case "Refresh":
             todos = functions.get_todos()
             window['todo'].update(value='')
             if event == 'Refresh':
                window['Add'].update(disabled=False)
                window['todos'].update(values=todos)

    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
window.close()