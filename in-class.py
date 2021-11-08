the_tasks = []

task_data_file = 'tasklist.txt'

def unimplemented():
    raise Exception('Unimplemented functionality')

def get_the_tasks():
    with open(task_data_file, "r") as f:
        return f.read().splitlines()

def elicit_user_input():
    print('Commands: (Q)uit, (A)dd\n> ', end='')
    return input()

def add_task():
    print('Input a new task: ', end='')
    some_input = input()

    with open(task_data_file, "a") as f:
        f.write(some_input + "\n")

# Returns a boolean describing whether the user chose to quit the application
def handle_user_input(userInput):
    if userInput == 'q':
        return True
    elif userInput == 'a':
        add_task()
    else:
        print('Invalid input')

    return False

# Tasks is an array of strings
def list_tasks(tasks):
    for t in tasks:
        print(t)

def event_loop():
    quit = False
    while not quit:
        tasks = get_the_tasks()
        list_tasks(tasks)

        elicited_input = elicit_user_input()
        quit = handle_user_input(elicited_input)
        
event_loop()
print('Bye!')
