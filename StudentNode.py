class StudentNode:
    def __init__(self, student):
        self.left = None
        self.right = None
        self.parent = None
        self.data = [student]
        self.key = student.average

    def add_new_node(self, new_student):
        if len(self.data):
            if new_student.average < self.key:
                if self.left is None:
                    self.left = StudentNode(new_student)
                    self.left.parent = self
                else:
                    self.left.add_new_node(new_student)
            elif new_student.average > self.key:
                if self.right is None:
                    self.right = StudentNode(new_student)
                    self.right.parent = self
                else:
                    self.right.add_new_node(new_student)
            else:
                self.data.append(new_student)
        else:
            self.data.append(new_student)

    @staticmethod
    def find_max(node):
        while node.right:
            node = node.right
        return node

