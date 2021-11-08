import os

selected = 0
tasklist = []
task_data_file = 'tasklist.txt'

def unimplemented():
    raise Exception('Unimplemented functionality')

def get_the_tasks():
    global tasklist

    if tasklist == []:
        with open(task_data_file, "r") as f:
            fileLines = f.read().splitlines()

            for line in fileLines:
                splitResult = line.split("\x1f")
                tasklist += [[bool(int(splitResult[0])), splitResult[1]]]
    result = []

    for line in fileLines:
        splitResult = line.split("\x1f")
        result += [[bool(int(splitResult[0])), splitResult[1]]]

    return tasklist

def elicit_user_input():
    print('Commands: (Q)uit, (A)dd, (N)ext, Mark (D)one\n> ', end='')
    return input()

def add_task():
    global tasklist

    print('Input a new task: ', end='')
    some_input = input()

    tasklist += [[False, some_input]]

def save_tasks():
    with open(task_data_file, "a") as f:
        for task in tasklist:
            f.write(str(int(task[0])) + "\x1f" + task[1] + "\n")

def next_task():
    global selected
    
    tasks = get_the_tasks()

    while True:
        selected += 1
        selected %= len(tasks)

        if not tasks[selected][0]:
            break;

# Returns a boolean describing whether the user chose to quit the application
def handle_user_input(userInput):
    if userInput == 'q':
        return True
    elif userInput == 'a':
        add_task()
    elif userInput == 'n':
        next_task()
    elif userInput == 'd':
        tasklist[selected][0] = True
        next_task()
    else:
        print('Invalid input')

    return False

def strikeout(text):
    new_text = ""

    for t in text:
        new_text += t + u"/u0336"

    return new_text

# Tasks is an array of strings
def list_tasks(tasks):
    for t in tasks:
        if t[0]:
            print(strikeout(t[1]), end = '')
        else:
            print("  ", end = '')
        print(t[1])

def delete_done_tasks_at_start():
    global selected
    global tasklist

    while len(tasklist) > 0 and tasklist[0][0]:
        # Remove it from the list
        tasklist = tasklist[1:]
        # Subtract 1 from selected
        selected -= 1

def event_loop():
    quit = False

    while not quit:
        os.system("clear")

        delete_done_tasks_at_start()

        tasks = get_the_tasks()
        list_tasks(tasks)

        elicited_input = elicit_user_input()
        quit = handle_user_input(elicited_input)

    save_tasks()
        
event_loop()
print('Bye!')
