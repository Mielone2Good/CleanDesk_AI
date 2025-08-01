from sentence_transformers import SentenceTransformer
from docs_reader import read_document, read_dir
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from typing import Union
import os

class AiAlgorithm:
    def __init__(self):
        """
        Load Embedding model (cached & local, needs to be downloaded first)
        Create pandas dataframe for holding files data.
        Kmeans algorithm settings.
        """
        self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
        self.dataframe = pd.DataFrame(columns=['path', 'embedding', 'file_name'])
        self.k_means_settings = dict(
            init='k-means++',
            n_init=10,
            max_iter=300,
            tol=1e-4,
            random_state=42,
            algorithm='lloyd',
            copy_x=True,
            verbose=0
        )

    def create_embedding(self, document_text: str) -> np.ndarray:
        """
        Create document embedding using SentenceTransformer.
        """
        embedding = self.embedding_model.encode(document_text)
        return embedding

    def save_embeddings(self, files: dict):
        """
        Save documents embeddings to pandas dataframe for quick access.
        """
        for file_name, file_data in files.items():
            file_text = file_data[0]
            file_path = file_data[1]
            file_embedding = self.create_embedding(document_text = file_text)

            new_row = {'path': file_path, 'embedding': file_embedding, 'file_name': file_name, 'kmeans_result': None}
            self.dataframe = pd.concat([self.dataframe, pd.DataFrame([new_row])], ignore_index=True)

    def get_embeddings(self) -> list:
        """
        Return all document embeddings from pandas dataframe.
        """
        return np.stack(self.dataframe['embedding'].values)
    
    def k_means_algorithm(self, n_clusters: Union[int, None] = None, show_chart: bool = False) -> list:
        """
        Group embeddings using K-Means Machine Learning algorithm.

        1. Get embeddings from pandas dataframe
        2. Calculate number of groups using Silhouette Algorithm or set manually.
        3. Predict groups using Kmeans.
        4. save results to dataframe and return groups in list.

        You can also view result chart if you set show_chart to True
        """
        embeddings = self.get_embeddings()
        if not n_clusters:
            n_clusters = self.calculate_n_clusters(embeddings = embeddings, show_chart = show_chart)

        kmeans_params = self.k_means_settings.copy()
        kmeans_params['n_clusters'] = n_clusters
        kmeans = KMeans(**kmeans_params)
        result = kmeans.fit_predict(embeddings)
        self.dataframe['kmeans_result'] = result

        if show_chart:
            self.show_k_means_chart(kmeans = kmeans, embeddings = embeddings)

        return result.tolist()
    
    def show_k_means_chart(self, kmeans: KMeans, embeddings: list):
        """
        Method to transform kmeans into readable 2d chart and display 
        it with files names.
        """
        transformed_embeddings = PCA(n_components=2).fit_transform(embeddings)
        embedding_x = transformed_embeddings[:, 0]
        embedding_y = transformed_embeddings[:, 1]
        plt.scatter(embedding_x, embedding_y, c=kmeans.labels_)

        for i, file_name in enumerate(self.dataframe['file_name']):
            plt.annotate(os.path.basename(file_name), (embedding_x[i], embedding_y[i]), fontsize=7, alpha=1.0)
        
        plt.show()

    def calculate_n_clusters(self, embeddings: list, show_chart: bool = False) -> int:
        """
        Calculate how much groups we need for k-means, using Silhouette Algorithm.
        You can also view result chart by setting show_chart to True.
        """
        results = []
        for n_clusters in range(2, len(embeddings)):
            kmeans_params = self.k_means_settings.copy()
            kmeans_params['n_clusters'] = n_clusters
            kmeans = KMeans(**kmeans_params)
            predict_kmeans = kmeans.fit_predict(embeddings)
            s_score = silhouette_score(embeddings, predict_kmeans)
            results.append(s_score)

        best_result = np.argmax(results) + 2 
        
        if show_chart:
            plt.plot(range(2, len(embeddings)) , results, marker='.')
            plt.xlabel('k')
            plt.ylabel('score')
            plt.show()

        return best_result





if __name__ == '__main__':
    ai = AiAlgorithm()
    docs = read_dir('test_files')
    ai.save_embeddings(docs)
    k_means = ai.k_means_algorithm(show_chart = True)
    print(ai.dataframe)
        
    



