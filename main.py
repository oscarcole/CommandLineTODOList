import json
from tabulate import tabulate



# manages the loading, saving, and posting all records
class DataManager:
    def __init__(self):
        self.file_path = "todoData.json"
        self.data = self.load_data()


    # loads in JSON file for stand-alone access when needed
    def load_data(self):
        with open(self.file_path,'r') as file:
            return json.load(file)

    # displays all records
    def display_todos(self):
        print(self.format_todos())  # Just prints the formatted list


    def format_todos(self):
        formatted_data = [
            [todo["id"], "[X]" if todo["completed"] else "[ ]", todo["task"]]
            for todo in self.data  # Now it uses self.data directly
        ]
        return tabulate(formatted_data, headers=["ID", "Status", "Task"], tablefmt="rounded_grid")

    # writes to JSON file
    def save_to_file(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.data, file, indent=4)


    # saves JSON file
    def save_data(self, id_number, todo_task, mark_completed):
        new_data = {"id": id_number,
                    "task": todo_task,
                    "completed": mark_completed}

        # appends new data before writing
        self.data.append(new_data)

        self.save_to_file()


class Record:
    def __init__(self, data_manager):
        self.data_manager = data_manager

    # Creates a new record in the JSON file
    def create_new(self):
        task = input("Enter the task description: ").strip()
        completed = False
        new_id = len(self.data_manager.data) + 1

        self.data_manager.save_data(new_id, task, completed)
        print(f"New task added successfully! ID: {new_id}")

    # marks record in JSON file as completed/True
    def mark_complete(self):
        print(f"Here is your current TODO list, what would you like to mark complete?:")
        data_manager.display_todos()
        try:
            user_choice = int(input())
        except ValueError:
            print("Invalid input, Please enter a number.")
            return

        for todo in self.data_manager.data:
            if todo["id"] == user_choice:
                todo["completed"] = True
                self.data_manager.save_to_file()
                print(f"Marking Task ID {user_choice} as complete!")
                data_manager.display_todos()
                return

        print(f"{user_choice} is not in the to-do list.")

    # removes record from JSON file
    def delete_record(self):
        print(f"Here is your current TODO list, what record would you like to delete?:")
        data_manager.display_todos()
        user_choice = int(input())
        for todo in self.data_manager.data:
            if todo["id"] == user_choice:
                self.data_manager.data.remove(todo)
                self.data_manager.save_to_file()
                print(f"Removed Record ID: {user_choice}")
                data_manager.display_todos()
                return



# contains the "navigation and actions" for the to-do list
class Menu:
    def __init__(self, data_manager):
        self.data_manager = data_manager

    def display_menu(self):
        print(f"\n**Menu**")
        print(f"1. Add a new task")
        print(f"2. Mark a task completed")
        print(f"3. Delete a task")
        print(f"4. Exit")

        while True:
            try:
                user_choice = int(input("What would you like to do? "))

                if user_choice == 1:
                    record = Record(self.data_manager)
                    record.create_new()
                elif user_choice == 2:
                    record = Record(self.data_manager)
                    record.mark_complete()
                elif user_choice == 3:
                    record = Record(self.data_manager)
                    record.delete_record()
                else:
                    print("Invalid choice, please try again")


                if 1 <= user_choice <= 5:
                    return user_choice
                else:
                    print("Invalid number, please enter a number between 1 and 5.")
            except ValueError:
                print("Invalid input, please enter a number.")



data_manager = DataManager()
data_manager.display_todos()



data_manager = DataManager()
menu = Menu(data_manager)
menu.display_menu()

