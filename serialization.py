import pickle

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

