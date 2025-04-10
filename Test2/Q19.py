class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks  # Private attribute

    
    def get_marks(self):
        return self.__marks

    
    def set_marks(self, new_marks):
        if 0 <= new_marks <= 100:
            self.__marks = new_marks
        else:
            print("invalid marks! Please enter a value between 0 and 100.")

    def show_info(self):
        print(f"Name: {self.name}, Marks: {self.__marks}")
