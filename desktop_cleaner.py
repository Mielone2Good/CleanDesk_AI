import shutil
import os
from ai_sorting_algorithm import AiAlgorithm
from docs_reader import read_dir
from typing import List, Tuple
import pandas as pd


def create_dirs(groups: list, organized_path: str):
    for group in groups:
        final_dir = os.path.join(organized_path, str(group))
        if not os.path.exists(final_dir):
            os.makedirs(final_dir)


def group_raw_dir(cleaning_path: str, show_results: bool = False) -> Tuple[List, pd.DataFrame]:
    ai = AiAlgorithm()
    docs = read_dir(path = cleaning_path)
    ai.save_embeddings(docs)
    groups = ai.k_means_algorithm(show_chart = False)
    if show_results: print(ai.dataframe)

    return groups, ai.dataframe


def clean_dir(cleaning_path: str, organized_path: str):
    if not os.path.exists(cleaning_path): 
        return {'error': 'Dir does not exists', 'status':'error'}
    
    groups, dataframe = group_raw_dir(cleaning_path = cleaning_path, show_results=True)
    create_dirs(groups, organized_path = organized_path)

    for idx, row in dataframe.iterrows():
        raw_file_path = row['path']
        group = row['kmeans_result']
        final_dir = os.path.join(organized_path, str(group))
        shutil.copy(raw_file_path, final_dir) #.move
        



if __name__ == '__main__':
    clean_dir(cleaning_path='test_files',organized_path='ogranized')

