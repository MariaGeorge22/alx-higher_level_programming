#!/usr/bin/python3
"""
the “base” of all other classes in this project.
"""


import csv
from genericpath import exists
import json
import turtle


class Base:
    """
    The Base Class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializing
        """
        new_id = id
        if new_id is None:
            Base.__nb_objects += 1
            new_id = Base.__nb_objects
        self.id = new_id

    @staticmethod
    def reset_before_tests():
        """
        Resets The __nb_objects

        FOR TESTING ONLY
        """
        Base.__nb_objects = 0

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """
        list_to_json = list_dictionaries or []
        return json.dumps(list_to_json)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        """
        list_to_json = list(
            map(lambda obj: obj.to_dictionary(), list_objs)) \
            if list_objs else []
        file_name = f"{cls.__name__}.json"
        with open(file_name, "w") as file:
            file.write(Base.to_json_string(list_to_json))

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        """
        def square_csv(square): return [
            square.id, square.size, square.x, square.y]

        def rectangle_csv(rectangle): return [
            rectangle.id, rectangle.width,
            rectangle.height, rectangle.x, rectangle.y]
        list_to_json = list(
            map(lambda obj: square_csv(obj)
                if cls.__name__ == "Square"
                else rectangle_csv(obj), list_objs)) \
            if list_objs else []
        file_name = f"{cls.__name__}.csv"
        with open(file_name, "w") as file:
            writer = csv.writer(file, lineterminator="\n")
            writer.writerows(list_to_json)

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        """
        list_to_return = []
        if json_string:
            list_to_return = json.loads(json_string)
        return list_to_return

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set
        """
        # TODO: find better initializing method
        dummy = cls(1) \
            if cls.__name__ == "Square"\
            else cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def create_csv(cls, *dictionary):
        """
        returns an instance with all attributes already set
        """
        # TODO: find better initializing method
        dummy = cls(1) \
            if cls.__name__ == "Square"\
            else cls(1, 1)
        dictionary = list(map(lambda i: eval(i), dictionary))
        dummy.update(*dictionary)
        return dummy

    @classmethod
    def load_from_file_csv(cls):
        """
        returns a list of instances
        """
        list_of_instances = []
        if exists(f"{cls.__name__}.csv"):
            with open(f"{cls.__name__}.csv") as file:
                reader = csv.reader(file)
                for row in reader:
                    list_of_instances.append(cls.create_csv(*row))
        return list_of_instances

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances
        """
        list_of_instances = []
        if exists(f"{cls.__name__}.json"):
            with open(f"{cls.__name__}.json") as file:
                string = file.read()
                list_of_instances = Base.from_json_string(string)
                if list_of_instances:
                    list_of_instances = list(map(
                        lambda i: cls.create(**i), list_of_instances))
        return list_of_instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        opens a window and draws all the Rectangles and Squares
        """
        window = turtle.Screen()
        t = turtle.Turtle()

        t.pencolor("red")
        for rect in list_rectangles:
            t.penup()
            t.setposition(rect.x, rect.y)
            t.pendown()
            t.forward(rect.width)
            t.right(90)
            t.forward(rect.height)
            t.right(90)
            t.forward(rect.width)
            t.right(90)
            t.forward(rect.height)
            t.right(90)

        t.pencolor("blue")
        for rect in list_squares:
            t.penup()
            t.setposition(rect.x, rect.y)
            t.pendown()
            t.forward(rect.size)
            t.right(90)
            t.forward(rect.size)
            t.right(90)
            t.forward(rect.size)
            t.right(90)
            t.forward(rect.size)
            t.right(90)

        window.mainloop()