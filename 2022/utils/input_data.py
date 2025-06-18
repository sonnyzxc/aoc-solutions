from pathlib import Path

def get_input(day: str) -> str:
    input_dir = f"{Path(__file__).parent.parent}/day{day}.txt"
    with open(input_dir) as f:
        data = f.read()
    return data

def get_input_lines(day: str) -> str:
    input_dir = f"{Path(__file__).parent.parent}/day{day}.txt"
    with open(input_dir) as f:
        data = [line.strip() for line in f]
    return data