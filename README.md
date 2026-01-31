#DATA PIPELINE DEVELOPMENT

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: MATHIYAZHAGAN M 

*INTERN ID*: CTIS4317

*DOMAIN*: DATA SCIENCE

*DURATION*: 4 WEEEKS

*MENTOR*: NEELA SANTOSH

# DESCRIPTION
Data Pipeline Development Project

This project demonstrates the development of a data pipeline for preprocessing, transformation, and loading (ETL) of structured datasets. The main goal is to create a robust pipeline capable of handling raw data, performing validation, cleaning, transformation, and generating processed datasets ready for analysis or machine learning. The pipeline is implemented using Python, with libraries including Pandas, scikit-learn, and PyYAML, emphasizing modularity, configurability, and reproducibility.

The dataset simulates a small human resources (HR) dataset with columns like Age, Salary, Department, and Gender, containing missing values in numeric and categorical fields. Numeric features are standardized using StandardScaler, while categorical variables are one-hot encoded using OneHotEncoder. Missing values are handled using configurable imputation strategies, ensuring clean, machine-readable data.

The project structure is modular and maintainable:

Data Extraction (pipeline.py) – Reads raw CSV data into a Pandas DataFrame.

Data Validation – Checks for empty datasets, missing columns, missing values, and verifies data types. Validation steps are logged for transparency.

Data Transformation (pipeline.py) – Implements pipelines for numeric and categorical features with imputation, scaling, and encoding. Outputs a processed DataFrame with proper feature names.

Logging (logger.py) – Tracks all ETL steps, recording extraction, validation, transformation, and errors.

Configuration (config.yaml) – Allows easy adjustment of preprocessing parameters without changing code.

The project also includes a Jupyter Notebook (ETL_Pipeline.ipynb) demonstrating the full ETL workflow interactively, from raw data extraction to processed dataset inspection.

This pipeline is reproducible, configurable, and scalable, suitable for various structured datasets. It provides a professional foundation for building more advanced ETL systems and integrating into data engineering or machine learning workflows.

#OUTPUT
<img width="804" height="603" alt="Image" src="https://github.com/user-attachments/assets/b6eef4ad-56cb-4890-8948-cd8a6d57f136" />

<img width="864" height="613" alt="Image" src="https://github.com/user-attachments/assets/bfd249cc-f160-496b-b253-8b895596cad8" />

<img width="824" height="620" alt="Image" src="https://github.com/user-attachments/assets/49265497-2b8d-44d1-bf7d-966379d23618" />

<img width="749" height="602" alt="Image" src="https://github.com/user-attachments/assets/1f21dd5c-a10c-4abf-9a21-773f5f26c594" />

<img width="789" height="602" alt="Image" src="https://github.com/user-attachments/assets/8f37c91c-4e55-4235-8441-f2c0b4609d56" />

<img width="813" height="606" alt="Image" src="https://github.com/user-attachments/assets/c618909a-78bc-43df-a14c-29c196710c0c" />

<img width="1140" height="856" alt="Image" src="https://github.com/user-attachments/assets/39547207-671f-44b6-a0ae-686af8574ef0" />
