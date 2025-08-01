import unittest
from ai_sorting_algorithm import AiAlgorithm
from docs_reader import read_dir, read_document

test_files = 'test_files'
print('AI Init --------------------------------')
ai = AiAlgorithm()
print('AI Initialized --------------------------------')


class DesktopCleanerTests(unittest.TestCase):

    def test_file_reading(self):
        data = read_document(f'{test_files}/school_test.pdf')
        self.assertIsNotNone(data, "Dane nie powinny być None")

    def test_silhouette_algorithm(self):
        n_clusters = ai.calculate_n_clusters(ai.get_embeddings())
        self.assertIn(n_clusters, [4, 5, 6], "Result should be around: 4, 5, 6")

    def test_k_means_algorithm(self):
        """
        You can turn on show_chart = True, 
        it will show debug charts, but it will freeze test time.
        """
        docs = read_dir(path = test_files)
        ai.save_embeddings(docs)
        groups = ai.k_means_algorithm(show_chart = False)
        self.assertIsNotNone(groups, "Groups shouldnt be empty")

unittest.main()