import pickle

class TreeNode:
    def __init__(self, value):
        self.value = value  # Значение узла
        self.left = None  # Левый потомок
        self.right = None  # Правый потомок

    def __repr__(self):
        return f"TreeNode({self.value})"


class Serialization:
    # Класс для (де)сериализации списков и словарей в файл и обратно

    @staticmethod
    def serialize_to_file(data, filename):
        with open(filename, mode='wb') as file:
            pickle.dump(data, file)

    @staticmethod
    def deserialize_from_file(filename):
        with open(filename, mode='rb') as file:
            data = pickle.load(file)

        return data


    @staticmethod
    def print_tree(root, level=0, prefix="Root: "):
        if root is None:
            print("  " * level + "└── None")
            return

        print("  " * level + prefix + str(root.value))
        if root.left or root.right:
            Serialization.print_tree(root.left, level + 1, "L: ")
            Serialization.print_tree(root.right, level + 1, "R: ")

    @staticmethod
    def create_sample_tree():
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.right = TreeNode(15)
        root.left.left = TreeNode(2)
        root.left.right = TreeNode(7)
        root.right.left = TreeNode(12)
        root.right.right = TreeNode(20)
        return root


