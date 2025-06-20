from typing import List, Tuple
from pathlib import Path

def get_input_str(day: str) -> str:
    input_dir = f"{Path(__file__).parent.parent}/day{day}.txt"
    with open(input_dir) as f:
        data = f.read()
    return data

def get_input_1d_str(day: str) -> List[str]:
    input_dir = f"{Path(__file__).parent.parent}/day{day}.txt"
    with open(input_dir) as f:
        data = [line.strip() for line in f]
    return data

def get_input_2d_int(day: str) -> List[List[int]]:
    input_dir = f"{Path(__file__).parent.parent}/day{day}.txt"
    with open(input_dir) as f:
        data = [[int(digit) for digit in line.strip()] for line in f]
    return data

def get_input_2d_str_int(day: str) -> List[Tuple[str, int]]:
    intput_dir = f"{Path(__file__).parent.parent}/day{day}.txt"
    with open(intput_dir) as f:
        data = [(line.split()[0], int(line.split()[1])) for line in f.readlines()]
    return data
