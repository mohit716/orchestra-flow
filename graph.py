class Graph:
    def __init__(self):
        self.tasks = {}
        self.edges = []  # (upstream, downstream)

    def add(self, fn, *deps):
        self.tasks[fn.__name__] = fn
        for dep in deps:
            self.edges.append((dep.__name__, fn.__name__))

    def run(self):
        remaining = {name: 0 for name in self.tasks}
        children = {name: [] for name in self.tasks}
        for up, down in self.edges:
            remaining[down] += 1
            children[up].append(down)

        ready = [name for name, n in remaining.items() if n == 0]
        while ready:
            name = ready.pop(0)
            self.tasks[name]()
            for child in children[name]:
                remaining[child] -= 1
                if remaining[child] == 0:
                    ready.append(child)


graph = Graph()


def print_1():
    print("1")


def print_2():
    print("2")


def print_3():
    print("3")


def print_4():
    print("4")


def print_5():
    print("5")


# print_1 → print_2 → print_3 → print_4 → print_5
graph.add(print_1)
graph.add(print_2, print_1)
graph.add(print_3, print_2)
graph.add(print_4, print_3)
graph.add(print_5, print_4)

graph.run()
