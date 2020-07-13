
class Node:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.vertex_dict = {}

    def add_new_node(self, vertex, weight):
        new_node = Node(vertex, weight)
        new_node.next = self.head
        self.head = new_node
        if vertex not in self.vertex_dict:
            self.vertex_dict[vertex] = ''

    def del_vertex_from_dict(self, vertex):
        del self.vertex_dict[vertex]

    def print_list(self):
        temp = self.head
        while temp is not None:
            print('vertex=' + str(temp.vertex) + '  weight=' + str(temp.weight))
            temp = temp.next

