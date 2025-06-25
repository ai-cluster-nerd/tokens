
import transformers

import config

import src.elements.s3_parameters as s3p
import datasets


class Interface:
    """

    """

    def __init__(self, s3_parameters: s3p):
        """

        :param s3_parameters: The overarching S3 parameters settings of this
                              project, e.g., region code name, buckets, etc.<br>
        """

        self.__s3_parameters = s3_parameters

        self.__configurations = config.Config()

    def exc(self, data: datasets.DatasetDict):
        """

        :param data: A DatasetDict of training (train), validation, and testing (test) data
        :return:
        """


        # The tokenizer, vis-à-vis pre-trained architecture
        tokenizer = transformers.AutoTokenizer.from_pretrained(
            pretrained_model_name_or_path=self.__configurations.checkpoint)

