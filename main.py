""" Simple To Do List """

my_task: list = []

# Add a task
def addTask():
    """ Adding a Task """
    task: str = input('Please enter a task: ')
    my_task.append(task)
    print(f'Task, {task} has been added to the list!')

# List of tasks
def checkTask() -> None:
    """ Check the List of Tasks """
    if not my_task:
        print("There are no tasks currently.")
    else:
        print('Current Tasks:')
        for index, task in enumerate(my_task):
            print(f'Task #{index}. {task}')

# Delete a Task
def deleteTask():
    """ Delete a Task """
    checkTask()
    try:
        taskToDelete: int = int(input('Enter the # to delete: '))
        if taskToDelete >=0 and taskToDelete < len(my_task):
            my_task.pop(taskToDelete)
            print(f'Task {taskToDelete} has been removed.')
        else:
            print(f'Task #{taskToDelete} was not found.')
    except TypeError:
        print('Invalid input.')

# Create a list
print('Welcome to your To-Do List!')

while True:
    user_input: str = input('\nType what would you like to do?\n Add, Delete, Check, Quit > ').lower()

    # Check what the user wants to do.
    if user_input in ['add']:
        print('Adding a task!\n')
        addTask()
    elif user_input in ['delete']:
        print('Deleting a task!\n')
        deleteTask()
    elif user_input in ['check']:
        print(f'Here is the list!')
        checkTask()
    elif user_input in ['quit']:
        print('Program quit')
        break
    else:
        print('Invalid input.')
