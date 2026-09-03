from serialization import Serialization

class Combined_data():
    def __init__(self, list_of, dict_of):
        self.list_of = list_of
        self.dict_of = dict_of


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

if __name__ == '__main__':
    main()
