class Node:
    def __init__(self, data, parent=None) -> None:
        self.children: list[Node] = []
        self.parent: Node | None = parent

        self.data = data
    
    def add_child(self, data):
        self.children.append(Node(data, self))

class Tree:
    ...