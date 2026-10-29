# Programming for Machine Learning: Course Labs

Lab work from the **Programming for ML** course in my M.Sc. in Applied AI at Luleå University of Technology (LTU). Four labs take a path from basic data statistics to regression, clustering and image processing, with an emphasis on implementing things by hand before reaching for libraries.

## The labs

| Lab | Topic | What I built |
|-----|-------|--------------|
| **Lab 1** (`Lab1.py`) | Data and statistics | Explored the California housing dataset with my own mean and median functions, grouped by ocean proximity, plotted histograms and interpreted the results |
| **Lab 2** (`Lab2.ipynb`) | Linear and polynomial regression | CSV loader written without pandas, linear regression on Swedish income-by-age data (MSE/RMSE), gradient descent implemented by hand, polynomial regression with hyperparameter tuning |
| **Lab 3** (`Lab3.ipynb`) | K-Means clustering | K-Means classifier written from scratch with OOP, grid search for the best number of clusters, classification of new data points on a rent dataset |
| **Lab 4** (`Lab4/`) | Image processing | With scikit-image: loading images, grayscale conversion, resizing, histogram thresholding, and template matching (library version and a manual MSE version) |

## Repository structure

```
ProgrammingML/
├── Lab1.py            # Lab 1 solution
├── Lab2.ipynb         # Lab 2 solution
├── Lab3.ipynb         # Lab 3 solution
├── Lab4/              # Lab 4 solutions (task1.py to task6.py) and images
├── lections.py        # Exercises from the lectures: statistics, sorting, OOP, K-Means
├── main.py            # Life satisfaction vs GDP linear regression
├── datasets/          # Data used by each lab
├── labtasks/          # The original lab descriptions (PDF)
├── other/             # Self-study notebooks on linear models (Hands-On ML, chapter 4)
└── requirements.txt
```

## Tech stack

Python, NumPy, pandas, scikit-learn, scikit-image, Matplotlib, Jupyter

## Getting started

```bash
git clone https://github.com/antluqmol1/ProgrammingML.git
cd ProgrammingML
pip install -r requirements.txt scikit-image jupyter

python Lab1.py            # Lab 1
jupyter notebook          # Labs 2 and 3
cd Lab4 && python task1.py   # Lab 4 (run from inside Lab4/ so the images are found)
```

## About me

**Antonio Manuel Luque Molina**: Computer Engineering graduate (University of Seville), now studying Applied AI in Sweden.

- GitHub: [@antluqmol1](https://github.com/antluqmol1)
