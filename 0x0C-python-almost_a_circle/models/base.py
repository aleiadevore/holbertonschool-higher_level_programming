#!/usr/bin/python3
"""This module creates a base class"""
import json
import csv


class Base:
    """This is the base class for the project"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) < 1:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        with open(cls.__name__ + ".json", 'w') as f:
            lst = []
            if list_objs is not None and len(list_objs) > 0:
                for i in list_objs:
                    lst.append(i.to_dictionary())
            f.write(cls.to_json_string(lst))

    # returns list from JSON string
    @staticmethod
    def from_json_string(json_string):
        lst = []
        if json_string is None or len(json_string) < 1:
            return lst
        return json.loads(json_string)

    # returns new object from dictionary
    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            new = cls(1, 1, 0, 0)
        else:
            new = cls(1, 0, 0)
        new.update(**dictionary)
        return new

    # loads from JSON file, creates, and returns list of objects
    @classmethod
    def load_from_file(cls):
        jstr = ""
        with open(cls.__name__ + ".json", 'r') as f:
            for line in f:
                jstr += line
        jlst = cls.from_json_string(jstr)
        olst = []
        for i in jlst:
            olst.append(cls.create(**i))
        return olst

    @classmethod
    def save_to_file_csv(cls, list_objs):
        with open(cls.__name__ + ".csv", 'w') as f:
            lst = []
            if cls.__name__ == "Rectangle":
                csv_columns = ['id', 'width', 'height', 'x', 'y']
                for i in list_objs:
                    lst.append(i.to_dictionary())
                writer = csv.DictWriter(f, fieldnames=csv_columns)
                writer.writeheader()
                for data in lst:
                    writer.writerow(data)
            if cls.__name__ == "Square":
                csv_columns = ['id', 'size', 'x', 'y']
                for i in list_objs:
                    lst.append(i.to_dictionary())
                writer = csv.DictWriter(f, fieldnames=csv_columns)
                writer.writeheader()
                for data in lst:
                    writer.writerow(data)

    @classmethod
    def load_from_file_csv(cls):
        clist = []
        olist = []
        try:
            f = open(cls.__name__ + ".csv", 'r')
            for line in csv.DictReader(f):
                clist.append(line)
            for i in clist:
                for j in i:
                    i[j] = int(i[j])
                    olist.append(cls.create(**i))
            f.close()
            return olist
        except:
            return []
