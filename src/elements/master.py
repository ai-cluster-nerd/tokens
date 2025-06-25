import typing

import datasets


class Master(typing.NamedTuple):

    id2label: dict
    label2id: dict
    data: datasets.DatasetDict
