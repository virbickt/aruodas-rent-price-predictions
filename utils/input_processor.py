import numpy as np
import json


class Input:
    """
    Validates the inputs and returns them in a form of a list
    """
    def __init__(self, data: dict) -> None:
        if "number_of_rooms" not in data:
            raise ValueError("Mandatory field 'Number of rooms' is missing")
        self.number_of_rooms = data["number_of_rooms"]
        if "area" not in data:
            raise ValueError("Mandatory field 'Area' is missing")
        self.area = data["area"]
        if "floor_on" not in data:
            raise ValueError("Mandatory field 'Floor on' is missing")
        self.floor_on = data["floor_on"]
        if "floors_total" not in data:
            raise ValueError("Mandatory field 'Total floors' is missing")
        self.floors_total = data["floors_total"]

    def to_list(self) -> list:
        "Returns the input values in a form of a list"
        return [self.number_of_rooms, self.area, self.floor_on, self.floors_total]


def process_input(request_data: str) -> np.array:
    """
    Decodes the data in json format that it is supplied with as an argument, extract the values of the key "inputs" within
    the file and returns it in a form of np.array
    :param request_data: the input values in a form of a json format
    :return: np.array
    """
    input_data = json.loads(request_data)["inputs"]
    requests = []

    for input_datum in input_data:
        requests.append(Input(input_datum).to_list())

    return np.asarray(requests)