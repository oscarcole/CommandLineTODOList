import json
import requests

# manages the loading, saving, and posting all records
class DataManager:
    def __init__(self):
        self.file_path = "todoData.json"
        self.data = self.load_data()


    # loads json file
    def load_data(self):
        with open(self.file_path,'r') as file:
            return json.load(file)


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
    def create_new(self):
        pass

    def edit_record(self):
        pass

    def delete_record(self):
        pass

data_manager = DataManager()
data_manager.save_data(5, "Put up cord", "false")
data_manager.load_data()