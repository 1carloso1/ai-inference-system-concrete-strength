# Comparación de Algoritmos de Regresión con Optimización de Hiperparámetros usando RandomizedSearchCV

Este proyecto evalúa y compara el rendimiento de ocho algoritmos de **regresión** aplicados al dataset público *Concrete Compressive Strength*.  
La optimización de hiperparámetros se realizó utilizando **RandomizedSearchCV** para cada modelo, buscando maximizar el rendimiento y reducir el error.

## Algoritmos evaluados
- Linear Regression
- Ridge Regression
- Lasso Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor
- XGBoost Regressor
- K-Nearest Neighbors Regressor

## Metodología
1. Preprocesamiento de datos (normalización, manejo de outliers, división train/test).
2. Optimización de hiperparámetros con **RandomizedSearchCV** y validación cruzada.
3. Evaluación con métricas:
   - RMSE
   - MAE
   - MAPE (%)
   - R²
4. Comparación visual con gráficas de barras y dispersión.

## Contenido
- `data/concrete_data.xls` → Dataset utilizado.
- `notebooks/Comparación_Inferencia_Algoritmos_en_resistencia_concreto.ipynb` → Notebook con el código de entrenamiento y análisis.
- `resultados/` → Métricas finales, gráficas.
