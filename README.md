
<!-- Improved compatibility of back to top link -->
<a id="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<br />
<div align="center">
  <a href="https://github.com/Mielone2Good/CleanDesk_AI">
    <img src="https://www.python.org/static/community_logos/python-logo.png" alt="Python Logo" height="80">
  </a>

  <h3 align="center">CleanDesk_AI - Smart Local File Organizer</h3>

  <p align="center">
    Automatically clusters and organizes your desktop files using ML Algorithms and K-Means clustering.
    <br />
    <a href="https://github.com/Mielone2Good/CleanDesk_AI"><strong>Explore the code »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Mielone2Good/CleanDesk_AI">View Demo</a>
    ·
    <a href="https://github.com/Mielone2Good/CleanDesk_AI/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/Mielone2Good/CleanDesk_AI/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>

---

## 📌 About The Project

**CleanDesk_AI** is a smart desktop/file organizer that uses semantic embeddings and unsupervised learning to cluster similar files into groups, based on their **content**, not filenames. This means your desktop or folder can be cleaned and structured automatically using AI/ML — no manual sorting needed.

💡 Built for researchers, developers, and productivity geeks who want to bring structure to their chaotic folders.

### Version 1.1

📁 Automatic file clustering via **K-Means Algorithms**  
🧠 Embeddings extracted using: `SentenceTransformer('all-MiniLM-L6-v2')`  
📈 Automatic cluster number estimation using **Silhouette Score Algorithms**  
📄 Moving files into organized dirs (only numeric dirs for now, see screenshots below)
🧪 Unit tests included  
📊 Optional debug visualizations for clusters and embeddings  

---

## 🔍 How It Works

1. **Text extraction** from supported files using `docs_reader.py`
2. **Embedding generation** for each file using local(downloaded) SentenceTransformer
3. **Clustering** with K-Means AI/ML Algorithm (optimal number of clusters is auto-detected)
4. **Sorting and saving** organized results to labeled folders
5. **Moving Files** - Moves files into organized dirs.
6. Optionally, enable charts and debug output for insights during processing

---

## ⚙️ Structure

- `ai_sorting_algorithm.py`:  
   Core AI logic including embedding generation, clustering (K-Means Algorithm), and cluster number estimation (Silhouette Score Algorithm)
  
- `desktop_cleaner.py`:  
   Main execution file, orchestrates the entire workflow

- `docs_reader.py`:  
   Parses and reads text content from files (PDFs, TXT, etc.)

- `unit_tests.py`:  
   A full suite of tests to validate the clustering and embedding pipeline

🛠️ **Pro tip**: Pass `show_chart=True` or `debug=True` to many core functions to visualize embeddings or cluster allocations.

---

## 🚀 Built With

* [![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
* [Sentence Transformers](https://www.sbert.net/)
* [Scikit-learn](https://scikit-learn.org/)
* [Matplotlib](https://matplotlib.org/)

---

## 🧪 Unit Tests

CleanDesk_AI includes unit tests to ensure the accuracy of clustering logic and file processing components.

Run them with:

```bash
python unit_tests.py
````

All major pipeline stages are tested. Visual debug output can be enabled for more granular testing.

---

## 🚫 License

This project is licensed under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/).
That means:

* ✅ Free for **non-commercial** use
* ✅ Attribution required
* ❌ **Commercial use is not allowed**

Author: **Mikołaj Jaros (aka MixDevv)**
[![LinkedIn](https://img.shields.io/badge/-Mikołaj%20Jaros-blue?style=flat\&logo=Linkedin\&logoColor=white)](https://www.linkedin.com/in/mikolajjaros/)

---

## 🙏 Acknowledgments

* [Sentence Transformers](https://www.sbert.net/)
* [Scikit-learn](https://scikit-learn.org/)
* [Python Software Foundation](https://www.python.org/)
* [Matplotlib](https://matplotlib.org/)

---

## 📷 Screenshots

### 2D Chart view - K-means algorithm, Each color is each group. (it reads context inside, not file names)
<img width="1100" alt="Zrzut ekranu 2025-08-01 195911" src="https://github.com/user-attachments/assets/b5eefec6-19b1-4b20-9f50-fc49a2aa6edc" />

### 2D Chart view - Silhouette Score Algorithm (it predicts number of groups for best results.)
<img width="1100" alt="Zrzut ekranu 2025-08-01 195859" src="https://github.com/user-attachments/assets/f258efd5-2efc-4489-ae9a-2f74ccc0e26b" />

---

### Tests - Ready-To-Test files.
<img width="300" alt="Zrzut ekranu 2025-08-01 195834" src="https://github.com/user-attachments/assets/fec62421-8612-4933-9dab-2c206a67322e" />

### Tests - Files after segregation.
<img width="300" alt="Zrzut ekranu 2025-08-01 195945" src="https://github.com/user-attachments/assets/2c61ddc3-37c9-4dc4-a045-572023ae1227" />

---

### Tests - Pandas Dataframe Example
<img width="1100" alt="Zrzut ekranu 2025-08-01 200001" src="https://github.com/user-attachments/assets/55f73d6f-d361-4469-91cd-72aa56225f4a" />

---


<!-- MARKDOWN LINKS & IMAGES -->

[contributors-shield]: https://img.shields.io/github/contributors/Mielone2Good/CleanDesk_AI.svg?style=for-the-badge
[contributors-url]: https://github.com/Mielone2Good/CleanDesk_AI/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Mielone2Good/CleanDesk_AI.svg?style=for-the-badge
[forks-url]: https://github.com/Mielone2Good/CleanDesk_AI/network/members
[stars-shield]: https://img.shields.io/github/stars/Mielone2Good/CleanDesk_AI.svg?style=for-the-badge
[stars-url]: https://github.com/Mielone2Good/CleanDesk_AI/stargazers
[issues-shield]: https://img.shields.io/github/issues/Mielone2Good/CleanDesk_AI.svg?style=for-the-badge
[issues-url]: https://github.com/Mielone2Good/CleanDesk_AI/issues
[license-shield]: https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey?style=for-the-badge
[license-url]: https://creativecommons.org/licenses/by-nc/4.0/
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/mikolajjaros/




