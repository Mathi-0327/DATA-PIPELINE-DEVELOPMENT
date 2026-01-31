import pandas as pd
import yaml

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer

from logger import setup_logger

# Load configuration
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

def validate_data(df, logger):
    """Validate raw data"""
    logger.info("Starting data validation")

    # 1. Empty dataset check
    if df.empty:
        logger.error("Validation failed: Dataset is empty")
        raise ValueError("Dataset is empty")

    # 2. Required columns check
    required_columns = {"Age", "Salary", "Department", "Gender"}
    missing_columns = required_columns - set(df.columns)
    if missing_columns:
        logger.error(f"Missing required columns: {missing_columns}")
        raise ValueError(f"Missing required columns: {missing_columns}")

    # 3. Missing values check
    missing_count = df.isnull().sum().sum()
    if missing_count > 0:
        logger.warning(f"Dataset contains {missing_count} missing values")

    # 4. Data type sanity check
    logger.info(f"Data types:\n{df.dtypes}")
    logger.info("Data validation completed successfully")

def extract_data(path, logger):
    """Extract data from CSV"""
    logger.info(f"Extracting data from {path}")
    df = pd.read_csv(path)
    logger.info(f"Data extracted successfully. Shape: {df.shape}")

    # Validate data after extraction
    validate_data(df, logger)
    return df

def transform_data(df, logger):
    """Transform data using pipelines"""
    logger.info("Starting data transformation")

    # Identify numeric and categorical columns
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns
    categorical_cols = df.select_dtypes(include=["object"]).columns

    logger.info(f"Numeric columns: {list(numeric_cols)}")
    logger.info(f"Categorical columns: {list(categorical_cols)}")

    # Numeric pipeline
    numeric_pipeline = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy=config["preprocessing"]["numeric_imputation"])),
        ("scaler", StandardScaler())
    ])

    # Categorical pipeline
    categorical_pipeline = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy=config["preprocessing"]["categorical_imputation"])),
        ("encoder", OneHotEncoder(handle_unknown="ignore", sparse_output=False))
    ])

    # Combine pipelines
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_pipeline, numeric_cols),
            ("cat", categorical_pipeline, categorical_cols)
        ]
    )

    # Transform data
    transformed_array = preprocessor.fit_transform(df)

    # Feature names
    feature_names = list(numeric_cols) + \
        list(preprocessor.named_transformers_["cat"]
             .named_steps["encoder"]
             .get_feature_names_out(categorical_cols))

    # Convert to DataFrame
    transformed_df = pd.DataFrame(transformed_array, columns=feature_names)
    logger.info(f"Transformation completed. Output shape: {transformed_df.shape}")

    return transformed_df
