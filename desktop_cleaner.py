import shutil
import os
from ai_sorting_algorithm import AiAlgorithm
from docs_reader import read_dir
from typing import List, Tuple
import pandas as pd


def create_dirs(groups: list, organized_path: str):
    """
    create dir for each group (numbers only for now)
    """
    for group in groups:
        final_dir = os.path.join(organized_path, str(group))
        if not os.path.exists(final_dir):
            os.makedirs(final_dir)


def group_raw_dir(cleaning_path: str, show_results: bool = False) -> Tuple[List, pd.DataFrame]:
    """
    Use alorithm to group files based on their context inside.
    """
    ai = AiAlgorithm()
    docs = read_dir(path = cleaning_path)
    ai.save_embeddings(docs)
    groups = ai.k_means_algorithm(show_chart = show_results)
    if show_results: print(ai.dataframe)

    return groups, ai.dataframe


def clean_dir(cleaning_path: str, organized_path: str, debug_chart: bool = False):
    """
    Main function, use it to sort one dir and move sorted files to another.
    you should set shutil.move instead of shutil.copy, its for testing.
    """
    if not os.path.exists(cleaning_path): 
        return {'error': 'Dir does not exists', 'status':'error'}
    
    groups, dataframe = group_raw_dir(cleaning_path = cleaning_path, show_results = debug_chart)
    create_dirs(groups, organized_path = organized_path)

    for idx, row in dataframe.iterrows():
        raw_file_path = row['path']
        group = row['kmeans_result']
        final_dir = os.path.join(organized_path, str(group))
        shutil.copy(raw_file_path, final_dir) # .move, Should be set to .move but its on copy for tests.
        



if __name__ == '__main__':
    """
    Fast test.
    """
    clean_dir(cleaning_path='test_files',organized_path='ogranized', debug_chart = True)

