# -*- coding: utf-8 -*-
import sys
import os
sys.path.append('..')
sys.path.append(os.path.join(sys.path[0], '../../'))

import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
from src.utils import save_as_pickle
from features import *


@click.command()
@click.option('--input_filepath',       type=click.Path(exists=True))
@click.option('--output_data_filepath', type=click.Path())
def main(input_filepath, output_data_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')

    build_all_features(input_filepath, output_data_filepath)

    logger.info(f'Target saved to {output_data_filepath}')

if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()