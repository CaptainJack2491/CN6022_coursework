# Project Overview

This is a university Big Data Analytics coursework project for 2024/25 focusing on Apache Spark for large-scale data processing and machine learning. The project consists of 4 main tasks:

*   **Task 1: Understanding the Data**: Load and explore the dataset, understand its structure, and report on data quality.
*   **Task 2: Big Data Analysis using Spark SQL**: Implement three Spark SQL queries to analyze the data and create visualizations.
*   **Task 3: Machine Learning using Spark MLlib**: Implement two ML algorithms to predict flight cancellations/delays or delay times, including feature selection, preprocessing, and model evaluation.
*   **Task 4: Presentation**: Present the findings and demonstrate an understanding of Big Data concepts.

# Technology Stack

*   **Primary Framework**: Apache Spark (PySpark recommended)
*   **Language**: Python 3
*   **Spark SQL**: For data analysis and querying
*   **Spark MLlib**: For machine learning implementations
*   **Optional**: Databricks for cloud-based Spark development

# Development Setup

### Prerequisites

*   Python 3.x
*   Apache Spark
*   PySpark Python library
*   Jupyter notebooks (recommended for exploratory analysis)

### Local Setup

```bash
# initialize a virtual environment
uv venv
source .venv/bin/activate
# Install dependencies
uv add -r requirements.txt
```

# Development Workflow

1.  **Data Management**:
    *   Place raw datasets in the `data/` directory (which is gitignored).
    *   The dataset can be downloaded from [https://tinyurl.com/mwxnxnkb](https://tinyurl.com/mwxnxnkb).

2.  **Code Organization**:
    *   Each task has its own directory under `src/`.
    *   It is recommended to use Jupyter notebooks (`.ipynb`) for exploratory work and convert the final code to Python scripts (`.py`).

3.  **Implementation Guidelines**:
    *   **Spark SQL Tasks**: Use the DataFrame API and Spark SQL syntax, and optimize queries for large datasets.
    *   **MLlib Tasks**: Start with proper data preprocessing, split data into train/validation/test sets, and implement feature engineering as appropriate.

# Key Files to Reference

*   `mats/coursework.pdf`: Complete coursework specification and requirements.
*   `docs/notes/06_tue.md`: Marking scheme and requirements.
*   `README.md`: Project overview and setup instructions.
