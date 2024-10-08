import json
import os

class Exercise3():
    def __init__(self, file_path):
        try:
            path = os.path.join(os.getcwd(), file_path)
            with open(path, 'r') as file:
                self.jsonfile = json.loads(file.read())
        except json.JSONDecodeError as e:
            print(f"JSONDecodeError: {e}")
            exit()
        except FileNotFoundError:
            print("The file was not found.")
            exit()
        except Exception as e:
            print(f"An error occurred: {e}")
            exit()
    
    def get_username(self):
        return self.jsonfile["username"]

    def get_time_remaining(self):
        return self.jsonfile["time_remaining"]

    def add_hour(self):
        self.jsonfile["time_remaining"] += 60

    def get_items(self):
        item_list = []
        for item, price in self.jsonfile["shopping_cart"].items():
            item_list.append(item)
        return item_list

    def get_total(self):
        total_cost = 0
        for item, price in self.jsonfile["shopping_cart"].items():
            total_cost += price
        return total_cost

'''
x = Exercise3('example.json')
print(x.get_username())
print(x.get_time_remaining())
x.add_hour()
print(x.get_time_remaining())
print(x.get_items())
print(x.get_total())
''' 