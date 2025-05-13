from functions import get_todos, write_todos
import time

now = time.strftime('%d %b %Y %H:%M:%S')
print('Date:',now[0:11],'\tTime:',now[12:])
while True:
    # Get user input and strip space characters from it
    user_action = input('Type Add, Show, Delete, Edit or Exit : ').lower()
    user_action = user_action.strip()

    if user_action.startswith('add'):
         new_todo = user_action[4:] + '\n'
         new_todo = new_todo.title()
         todos = get_todos()
         if new_todo not in todos:
            todos.append(new_todo)
            write_todos(todos)
         else:
              print("Todo already exist")
    elif user_action.startswith('show'):
        todos = get_todos()
        for index,todo in enumerate(todos):
             todo = todo.strip('\n')
             print(f'{index+1}-{todo}')
    elif user_action.startswith('edit'):
         try:
             number = int(user_action[5:])
             number = number - 1
             todos = get_todos()
             index = todos.index(todos[-1])
             if number > index :
                 print('Todo of this number does not exist in a List')
             else:
                 new_todo =  input("Enter a new Todo: ")
                 new_todo = new_todo.title()
                 if new_todo in todos:
                      print("New Todo already exist in a list")
                 else:
                      todos[number] = new_todo + '\n'
                      write_todos(todos)
         except ValueError:
               print('Your command is not valid.')
    elif user_action.startswith('delete'):
         try:
             number = int(user_action[7:])
             number = number - 1
             todos = get_todos()
             no_todo = todos[number].strip('\n')
             todos.pop(number)
             write_todos(todos)
             message = f'Todo {no_todo} is removed from the List'
             print(message)
         except IndexError:
              print('There is no item with that number')
    elif user_action.startswith('exit'):
         break
    else:
         print('Command is not valid')





