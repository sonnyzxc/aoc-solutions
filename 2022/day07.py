from __future__ import annotations
from typing import Optional
from utils.input_data import get_input_1d_str

data = get_input_1d_str("07")

class Node:
    def __init__(self, name: str, size: int, is_dir: bool, parent: Optional[Node]) -> None:
        self.name: str = name
        self.size: int = size
        self.is_dir: bool = is_dir
        self.parent: Optional[Node] = parent
        self.children: Optional[dict[str, Node]] = {} if is_dir else None

    def __repr__(self) -> str:
        num_children = 0 if not self.is_dir else len(self.children.values())
        return f"Node(name='{self.name}', size={self.size:,}, children_count={num_children})"

    def add_child(self, child_name: str, child_size: int, child_is_dir: bool):
        if child_name not in self.children:
            new_child = Node(name=child_name, size=child_size, is_dir=child_is_dir, parent=self)
            self.children[child_name] = new_child
            # propagte upwards
            if not child_is_dir:
                cur = self
                while cur:
                    cur.size += child_size
                    cur = cur.parent

    def get_child(self, child_name: str) -> Node:
        return self.children[child_name]


root = Node(name="/", size=0, is_dir=True, parent=None)
cur = root
for cmd in data:
    cmds = cmd.split()
    instr = cmds[0]
    match instr:
        case "dir":
            cur.add_child(child_name=cmds[1], child_size=0, child_is_dir=True)
        case "$":
            if cmds[1] == "ls":
                pass
            elif cmds[1] == "cd":
                dir = cmds[2]
                if dir == "/":
                    cur = root
                elif dir == "..":
                    cur = cur.parent
                else:
                    cur = cur.get_child(dir)
        case _: # must be a file
            cur.add_child(child_name=cmds[1], child_size=int(instr), child_is_dir=False)

# traverse (BFS)
free_space = 70_000_000 - root.size
required_space = 30_000_000 - free_space
print(free_space, required_space)
ans1, ans2 = 0, root.size
q = []
q.append(root)
while q:
    cur = q.pop(0)

    # part 1
    if cur.size <= 100_000:
        ans1 += cur.size

    # part 2
    if cur.is_dir and cur.size >= required_space:
        print(cur, cur.children.values())
        ans2 = min(ans2, cur.size)

    for child in cur.children.values():
        if child.is_dir:
            q.append(child)

print(f"Part 1: {ans1}")
print(f"Part 2: {ans2}")
