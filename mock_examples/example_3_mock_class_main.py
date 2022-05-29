from mock_examples.example_3_mock_class import DataSet


def init_data():
    dataset = DataSet()
    return dataset.load_data()