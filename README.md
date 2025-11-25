# AI-Based Inference System for Concrete Compressive Strength: Multi-dataset Analysis of Optimized Machine Learning Algorithms

## Abstract

The prediction of concrete compressive strength (CS, MPa) is fundamental in experimental civil engineering, as it enables the optimization of mix design and complements laboratory testing through predictive tools.  
This study presents a systematic and reproducible methodology for comparing eight regression algorithms — including linear models, neural networks, and *boosting* methods — applied to three experimental datasets that represent different types of concrete: high-performance concrete (HPC), conventional concrete, and recycled-aggregate concrete (RAC).  
Through hyperparameter optimization using `RandomizedSearchCV` and homogeneous cross-validation, the metrics RMSE, MAE, MAPE, R², and nRMSE were evaluated.  
The *boosting* methods achieved the best performance, with CatBoost standing out by reaching R² values between 0.92–0.95 and RMSE between 3.4–4.4 MPa, confirming its inter-dataset stability and generalization capability.  
These results indicate consistent predictive accuracy across concretes of different compositions and production contexts.  
As an applied contribution, three interactive inference systems were developed in Google Colab to estimate compressive strength from mix parameters, promoting reproducibility, open access, and practical use in quality-control processes.

---

## Methodology

The research was conducted following a structured, systematic, and reproducible methodology comprising **seven main stages**:  
1. Collection and integration of three public experimental concrete datasets.  
2. Review and selection of the most widely used regression algorithms for predicting concrete properties, based on their frequency of use and reported performance in recent literature.  
3. Preprocessing, normalization, and statistical analysis of the input variables.  
4. Training and optimization of eight supervised regression algorithms through random hyperparameter search (`RandomizedSearchCV`).  
5. Comparative evaluation of model performance within each dataset using standardized metrics (RMSE, MAE, MAPE, R², nRMSE).  
6. Stability and global ranking analysis across datasets to identify the most consistent and generalizable models.  
7. Implementation of an interactive inference system based on the best-performing models.

Figure below summarizes the proposed workflow, highlighting the main stages of the study and the iterative processes applied individually to each dataset.  
*Blue lines* group the iterative steps applied individually to each dataset, whereas *black lines* indicate the global stages performed once for the entire study.  
This methodological design ensured result traceability, algorithm and dataset comparability, and the practical transfer of knowledge toward the experimental validation of the developed inference system.

![Research Design and Workflow](results/Methodology/Method_diagram.png)


### Evaluated Models
- **Linear Regression**
- **Support Vector Regression (SVR)**
- **K-Nearest Neighbors (KNN)**
- **Random Forest**
- **Multilayer Perceptron (MLP)**
- **XGBoost**
- **LightGBM**
- **CatBoost**

### Optimization
- Hyperparameter tuning with `RandomizedSearchCV`
- 5-fold cross-validation
- Evaluation metrics: RMSE, MAE, MAPE (%), R², and nRMSE (%)

## Datasets Used

The study employs **three independent, publicly available experimental datasets** representing different concrete production and compositional contexts.  
All datasets are open-access and properly cited below:

| # | Dataset | Description | DOI / Link |
|:-:|:--|:--|:--|
| **1** | *Concrete Compressive Strength* (Yeh, 1998) | High-Performance Concrete (HPC) mixes tested at National Chiao Tung University, Taiwan. | [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/165/concrete+compressive+strength) |
| **2** | *Concrete Compressive Strength and Slump Dataset* (Ke--Qiu, 2024) | Normal concrete (NC) mixes used in highway engineering; includes compressive strength and slump data. | [Mendeley Data — DOI: 10.17632/zrsbhndz9f.1](https://data.mendeley.com/datasets/zrsbhndz9f/1) |
| **3** | *Recycled Aggregate Concrete with Fly Ash, GGBS, and Metakaolin* (Biswal et al., 2022) | Experimental dataset from IIT Bhubaneswar, India, including recycled aggregates and supplementary cementitious materials. | [Mendeley Data — DOI: 10.17632/5wkxzmzwnz.2](https://data.mendeley.com/datasets/5wkxzmzwnz/2) |

> *No new experimental data were generated in this study. All datasets are freely available through the corresponding repositories above.*

## Reproducibility

This project was developed and executed in **Google Colab**, using the **Python programming language** and open-source scientific and machine learning libraries.

### Environment Versions
| Library | Version |
|----------|----------|
| Python | 3.12.12 |
| pandas | 2.2.2 |
| numpy | 2.0.2 |
| matplotlib | 3.10.0 |
| seaborn | 0.13.2 |
| scikit-learn | 1.6.1 |
| xgboost | 3.1.1 |
| lightgbm | 4.6.0 |
| catboost | 1.2.8 |
| scipy | 1.16.3 |

> *For full reproducibility, it is recommended to install the dependencies listed above using a virtual environment or via a `requirements.txt` file.*

## Repository Structure

- `data/` → Contains the experimental datasets used in this study:  
  - **Concrete_Data** — Dataset 1: *Concrete Compressive Strength* (Yeh, 1998)  
  - **CSSNC** — Dataset 2: *Concrete Compressive Strength and Slump of Normal Concrete* (Ke & Lu, 2024)  
  - **CCSPIIT** — Dataset 3: *Recycled Aggregate Concrete with Fly Ash, GGBS, and Metakaolin* (Biswal et al., 2022)

- `notebooks/AI-Based Inference System for Concrete Compressive Strength — Multi-Dataset Analysis of Optimized Machine Learning Algorithms.ipynb` →  
  Main Google Colab Notebook containing the complete workflow for data preprocessing, model training, hyperparameter optimization, and comparative performance analysis.

- `results/` →  
  Directory containing all output files, organized by category for clarity and reproducibility:  
  - **histograms/** — Target variable distributions  
  - **metrics/** — Model performance tables and bar plots  
  - **methodology/** — Diagrams illustrating the research workflow  
  - **ranks/** — Ranking and stability analysis  
  - **feature_importance/** — Variable importance plots  
  - **inference_systems/** — Screenshots and UI components of the developed inference systems

- `requirements.txt` →  
  List of all Python libraries and versions required to reproduce the results.  
  To install the environment locally or on Google Colab, run:  
  ```bash
  pip install -r requirements.txt
   ```

## Citation

- **MDPI and ACS Style**
Olvera-Mayorga, C.E.; López-Martínez, M.d.J.; Rodríguez-Rodríguez, J.A.; Vázquez-Reyes, S.; Solís-Sánchez, L.O.; de la Rosa-Vargas, J.I.; Duarte-Correa, D.; González-Aviña, J.V.; Olvera-Olvera, C.A. AI-Based Inference System for Concrete Compressive Strength: Multi-Dataset Analysis of Optimized Machine Learning Algorithms. Appl. Sci. 2025, 15, 12383. https://doi.org/10.3390/app152312383

- **AMA Style**
Olvera-Mayorga CE, López-Martínez MdJ, Rodríguez-Rodríguez JA, Vázquez-Reyes S, Solís-Sánchez LO, de la Rosa-Vargas JI, Duarte-Correa D, González-Aviña JV, Olvera-Olvera CA. AI-Based Inference System for Concrete Compressive Strength: Multi-Dataset Analysis of Optimized Machine Learning Algorithms. Applied Sciences. 2025; 15(23):12383. https://doi.org/10.3390/app152312383

- **Chicago/Turabian Style**
Olvera-Mayorga, Carlos Eduardo, Manuel de Jesús López-Martínez, José A. Rodríguez-Rodríguez, Sodel Vázquez-Reyes, Luis O. Solís-Sánchez, José I. de la Rosa-Vargas, David Duarte-Correa, José Vidal González-Aviña, and Carlos A. Olvera-Olvera. 2025. "AI-Based Inference System for Concrete Compressive Strength: Multi-Dataset Analysis of Optimized Machine Learning Algorithms" Applied Sciences 15, no. 23: 12383. https://doi.org/10.3390/app152312383

- **APA Style**
Olvera-Mayorga, C. E., López-Martínez, M. d. J., Rodríguez-Rodríguez, J. A., Vázquez-Reyes, S., Solís-Sánchez, L. O., de la Rosa-Vargas, J. I., Duarte-Correa, D., González-Aviña, J. V., & Olvera-Olvera, C. A. (2025). AI-Based Inference System for Concrete Compressive Strength: Multi-Dataset Analysis of Optimized Machine Learning Algorithms. Applied Sciences, 15(23), 12383. https://doi.org/10.3390/app152312383