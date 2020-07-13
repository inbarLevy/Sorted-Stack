from StudentNode import *

class SortedStack:
    def __init__(self):
        self.root = None
        self.students_count = 0
        self.max_node = None

    def is_empty(self):
        return not bool(self.root)

    def size(self):
        return self.students_count

    def push(self, student):
        self.students_count += 1
        if self.root is None:
            self.root = StudentNode(student)
            self.max_node = self.root
        else:
            self.root.add_new_node(student)
            if student.average == self.max_node.key:
                self.max_node.data.append(student)
            elif student.average > self.max_node.key:
                self.max_node = self.max_node.right

    def pop(self):
        if self.max_node is None:
            print('SortedStack is empty')
            return
        # more than 1 student has the highest average
        if len(self.max_node.data) > 1:
            self.students_count -= 1
            return self.max_node.data.pop()
        else:
            # only 1 student has the highest average
            if self.max_node.left is None:
                self.students_count -= 1
                # no left, yes parent
                if self.max_node.parent:
                    temp = self.max_node.data.pop(0)
                    self.max_node.parent.right = None
                    self.max_node = self.max_node.parent
                    return temp
                # no left, no parent
                self.root = None
                return self.max_node.data.pop(0)
            self.students_count -= 1
            # yes left, yes parent
            if self.max_node.parent:
                temp = self.max_node.data.pop(0)
                self.max_node.left.parent = self.max_node.parent
                self.max_node.parent.right = self.max_node.left
                self.max_node = StudentNode.find_max(self.max_node.left)
                return temp
            # yes left, no parent
            temp = self.max_node.data.pop(0)
            self.root = self.max_node.left
            self.max_node.left.parent = None
            self.max_node = StudentNode.find_max(self.max_node.left)
            return temp

    def top(self):
        if self.root:
            return self.max_node.data[-1]
        print('SortedStack is empty')
        return



