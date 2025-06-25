
import transformers

import config

import src.data.interface


class Interface:
    """

    """

    def __init__(self):

        self.__configurations = config.Config()

    def exc(self):
        """

        :return:
        """

        # The tokenizer, vis-à-vis pre-trained architecture
        tokenizer = transformers.AutoTokenizer.from_pretrained(
            pretrained_model_name_or_path=self.__configurations.checkpoint)

