import json
from tabulate import tabulate

# manages the loading, saving, and posting all records
class DataManager:
    def __init__(self):
        self.file_path = "todoData.json"
        self.data = self.load_data()


    # loads in json file for stand-alone access when needed
    def load_data(self):
        with open(self.file_path,'r') as file:
            return json.load(file)


    def format_todos(self):
        formatted_data = [
            [todo["id"], "[X]" if todo["completed"] else "[ ]", todo["task"]]
            for todo in self.data  # Now it uses self.data directly
        ]
        return tabulate(formatted_data, headers=["ID", "Status", "Task"], tablefmt="rounded_grid")


    # saves json file
    def save_data(self, id_number, todo_task, mark_completed):
        new_data = {"id": id_number,
                    "task": todo_task,
                    "completed": mark_completed}

        # appends new data before writing
        self.data.append(new_data)

        # writes to json file
        with open(self.file_path, 'w') as file:
            json.dump(self.data, file, indent=4)



class Record:
    @staticmethod
    def create_new():
        cn_data_manager = DataManager()

        task = input("Enter the task description: ").strip()

        while True:
            completed_input = input("Is this task completed? Y/N:").strip().lower()
            if completed_input in ["y", "n"]:
                completed = True if completed_input =="y" else False
                break
            else:
                print("Invalid input. Please enter 'Y' or 'N'.")
        new_id = len(cn_data_manager.data) + 1

        cn_data_manager.save_data(new_id, task, completed)
        print(f"New task added successfully! ID: {new_id}")

    def edit_record(self):
        pass

    def delete_record(self):
        pass


# contains the "navigation and actions" for the to-do list
class Menu:
    def __init__(self, data_manager):
        self.data_manager = data_manager

    def display_menu(self):
        print(f"\n**Menu**")
        print(f"1. Add a new task")
        print(f"2. Edit a task")
        print(f"3. Mark a task completed")
        print(f"4. Delete a task")
        print(f"5. Exit")

        while True:
            try:
                user_choice = int(input("What would you like to do? "))

                if user_choice == 1:
                    Record.create_new()
                elif user_choice == 2:
                    print("Editing a task -- Feature coming soon")
                elif user_choice == 3:
                    print("Marking a task 'complete' -- Feature coming soon")
                elif user_choice == 4:
                    print("Deleting a task -- Feature coming soon")
                else:
                    print("Invalid choice, please try again")

                if 1 <= user_choice <= 5:
                    return user_choice
                else:
                    print("Invalid number, please enter a number between 1 and 5.")
            except ValueError:
                print("Invalid input, please enter a number.")


data_manager = DataManager()
print(data_manager.format_todos())

menu = Menu(data_manager)
menu.display_menu()