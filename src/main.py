import datetime
import logging
import os
import sys

import boto3


def main():
    """
    Entry po

    :return:
    """

    logger: logging.Logger = logging.getLogger(__name__)
    logger.info('Starting: %s', datetime.datetime.now().isoformat(timespec='microseconds'))

    master: mr.Master = src.data.interface.Interface(s3_parameters=s3_parameters).exc()


if __name__ == '__main__':

    # Paths
    root = os.getcwd()
    sys.path.append(root)
    sys.path.append(os.path.join(root, 'src'))

    # Logging
    logging.basicConfig(level=logging.INFO,
                        format='\n\n%(message)s\n%(asctime)s.%(msecs)03d\n',
                        datefmt='%Y-%m-%d %H:%M:%S')

    # Classes
    import src.data.interface
    import src.elements.master as mr
    import src.elements.s3_parameters as s3p
    import src.elements.service as sr
    import src.functions.cache
    import src.preface.interface

    connector: boto3.session.Session
    s3_parameters: s3p
    service: sr.Service
    connector, s3_parameters, service = src.preface.interface.Interface().exc()

    main()