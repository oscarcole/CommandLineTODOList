import json
from tabulate import tabulate

# manages the loading, saving, and posting all records
class DataManager:
    def __init__(self):
        self.file_path = "todoData.json"
        self.data = self.load_data()


    # loads json file
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
    def create_new(id_number, todo_task, mark_completed):
        cn_data_manager = DataManager()
        cn_data_manager.save_data(id_number, todo_task, mark_completed)

    def edit_record(self):
        pass

    def delete_record(self):
        pass


data_manager = DataManager()
print(data_manager.format_todos())