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


'''lab1
class Combined_data():
    def __init__(self, list_of, dict_of):
        self.list_of = list_of
        self.dict_of = dict_of

class Window_size():
    def __init__(self, height, length):
        self.height = height
        self.length = length

def main():
    list_of = [1, 2, 3, 4, 5]
    dict_of = {
        'user1': 'example@gmail.com',
        'user2': 'scg2211@gmail.com',
        'John123': 'ddr99@gmail.com'
    }

    combined_obj = Combined_data(list_of, dict_of)

    print(combined_obj, combined_obj.list_of, combined_obj.dict_of)
    Serialization.serialize_to_file(combined_obj, "file_sample.pkl")

    loaded_data = Serialization.deserialize_from_file("file_sample.pkl")
    print(loaded_data, loaded_data.list_of, loaded_data.dict_of)



    tree = Serialization.create_sample_tree()
    print("\n\nИсходное дерево:")
    Serialization.print_tree(tree)

    Serialization.serialize_to_file(tree, "tree.pkl")
    restored_tree = Serialization.deserialize_from_file("tree.pkl")
    print("\n\nЗагруженное дерево:")
    Serialization.print_tree(restored_tree)


    current_win = Window_size(300, 400)
    Serialization.serialize_to_file(current_win, "current_win.pkl")
    loaded_win = Serialization.deserialize_from_file("current_win.pkl")
    print(f"\n\nLoaded window size:{current_win.height}x{current_win.length}")
'''
