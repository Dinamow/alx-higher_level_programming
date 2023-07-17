#!/usr/bin/python3
"""Define a Base"""
import json


class Base:
    """
    Base: a classe named base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Arguemtns
        ---------
        id: a unique id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """to json"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """rites the JSON string representation of list_objs"""
        with open(cls.__name__ + ".json", "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [ele.to_dictionary() for ele in list_objs]
                f.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Square":
                new_ins = cls(1)
            else:
                new_ins = cls(2, 2)
            new_ins.update(**dictionary)
            return new_ins

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        try:
            with open(cls.__name__ + ".json", "r") as f:
                list_dicts = Base.from_json_string(f.read())
                return [cls.create(**dicty) for dicty in list_dicts]
        except IOError:
            return []
