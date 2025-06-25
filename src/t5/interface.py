import logging

import datasets
import transformers

import config
import src.elements.master as mr
import src.elements.s3_parameters as s3p
import src.t5.mappings


class Interface:
    """
    The interface to the T5 data tokenization steps
    """

    def __init__(self, s3_parameters: s3p):
        """

        :param s3_parameters: The overarching S3 parameters settings of this
                              project, e.g., region code name, buckets, etc.<br>
        """

        self.__s3_parameters = s3_parameters

        # Configurations
        self.__configurations = config.Config()
        self.__prefix = self.__configurations.destination + '/' + 'T5'

        # Logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)03d\n',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

    def __persist(self, packets: datasets.DatasetDict):
        """

        :param packets:
        :return:
        """

        dataset_dict_path = 's3://' + self.__s3_parameters.internal + '/' + self.__prefix
        packets.save_to_disk(dataset_dict_path=dataset_dict_path)

        self.__logger.info('The data tokens for T5 have been written to prefix: %s', self.__prefix)

    def exc(self, master: mr.Master):
        """

        :param master: The labels, and a DatasetDict of training (train), validation, and testing (test) data.
        :return:
        """

        # The tokenizer, vis-à-vis pre-trained architecture
        tokenizer = transformers.AutoTokenizer.from_pretrained(
            pretrained_model_name_or_path=self.__configurations.checkpoint)

        # Tokenization
        mappings = src.t5.mappings.Mappings(tokenizer=tokenizer, _id2label=master.id2label)

        try:
            packets = master.data.map(mappings.exc, batched=True)
        except RuntimeError as err:
            raise err from err

        self.__logger.info(packets)

        self.__persist(packets=packets)
