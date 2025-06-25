import logging
import typing

import datasets

import config
import src.elements.s3_parameters as s3p


class Interface:

    def __init__(self, s3_parameters: s3p):
        """

        :param s3_parameters: The overarching S3 parameters settings of this
                              project, e.g., region code name, buckets, etc.<br>
        """

        self.__s3_parameters: s3p.S3Parameters = s3_parameters

        # Configurations
        self.__configurations = config.Config()

        # The data
        dataset_path = 's3://' + self.__s3_parameters.internal + '/' + self.__configurations.prefix
        self.__data =  datasets.load_from_disk(dataset_path=dataset_path)

    def tags(self) -> typing.Tuple[dict, dict]:
        """

        :return:<br>
            id2label: dict<br>
            label2id: dict
        """

        values: datasets.Sequence = self.__data['train'].features['fine_ner_tags']
        id2label = dict(enumerate(values.feature.names))
        label2id = {value: key for key, value in id2label.items()}

        return id2label, label2id

    def data(self) -> datasets.DatasetDict:
        """

        :return:<br>
            data: datasets.DatasetDict
        """

        logging.info(self.__data)

        return self.__data
