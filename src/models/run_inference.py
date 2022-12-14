# -*- coding: utf-8 -*-
import sys
import os
sys.path.append('..')
sys.path.append(os.path.join(sys.path[0], '../../'))

import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
from src.utils import load_as_pickle
import pandas as pd



@click.command()
@click.option('--input_filepath', type=click.Path(exists=True))
@click.option('--input_model_filepath', type=click.Path())
@click.option('--csv_outputh_path', type=click.Path())

def main(input_filepath, input_model_filepath, csv_outputh_path):
    logger = logging.getLogger(__name__)
    logger.info('run inference')

    model = load_as_pickle(input_model_filepath)

    pd.DataFrame(model.predict(load_as_pickle(input_filepath))).to_csv(csv_outputh_path,index=False)
    logger.info('saved to file {}'.format(csv_outputh_path))
    
if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()