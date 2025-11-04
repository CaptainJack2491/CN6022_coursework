## Project Overview

This is a university **Big Data Analytics coursework** project for 2024/25 focusing on Apache Spark for large-scale data processing and machine learning. The project consists of 4 main tasks with a total of 120 marks.

## Project Structure

```
├── data/           # Dataset files (gitignored, add your data here)
├── docs/
│   └── notes/      # Course notes and marking scheme
├── src/
│   ├── 01_task - Understanding the data (25 marks)
│   ├── 02_task - Big Data analysis using Spark SQL (25 marks)
│   ├── 03_task - Machine Learning using Spark MLlib (35 marks)
│   └── 04_task - Presentation (35 marks)
├── mats/
│   └── coursework.pdf  # Full coursework specification
└── structure.md   # Directory structure reference
```

## Task Breakdown

### Task 1: Understanding the Data 
- Load and explore the dataset
- Understand data structure, schema, and characteristics
- Report on data quality and any preprocessing needed

### Task 2: Big Data Analysis using Spark SQL 
- Implement three Spark SQL queries to analyze the data
- Provide explanations for each query
- Create visualizations (plots or tables) to present findings

### Task 3: Machine Learning using Spark MLlib 
- Implement two ML algorithms with:
  - Feature selection and preprocessing
  - Handling class imbalance
  - Proper model configuration
- Explain algorithms and configurations used
- Evaluate and compare model performance
- Create visualizations for results

### Task 4: Presentation 
- Express understanding of Big Data concepts
- Demonstrate relevant and supportive statements
- Respond clearly to questions

## Technology Stack

- **Primary Framework**: Apache Spark (PySpark recommended)
- **Language**: Python 3
- **Spark SQL**: For data analysis and querying
- **Spark MLlib**: For machine learning implementations
- **Optional**: Databricks for cloud-based Spark development

## Development Setup

### Prerequisites
- Python 3.x
- Apache Spark (version compatible with coursework requirements)
- PySpark Python library
- Jupyter notebooks (recommended for exploratory analysis)

### Local Setup
```bash
# initialize a virtual environment
uv venv
source .venv/bin/activate
# Install dependencies
uv add -r requirements.txt
```

## Development Workflow

### 1. Data Management
- Place raw datasets in the `data/` directory
- The `data/` directory is gitignored to prevent committing large datasets
- Create processed/cleaned data outputs as needed within task folders

### 2. Code Organization
- Each task has its own directory under `src/`
- Recommended: Use Jupyter notebooks (.ipynb) for exploratory work
- Convert final code to Python scripts (.py) for production
- Include clear documentation and comments

### 3. Implementation Guidelines

**For Spark SQL Tasks:**
- Use DataFrame API and Spark SQL syntax
- Optimize queries for large datasets
- Include data validation and error handling
- Create meaningful aggregations and joins

**For MLlib Tasks:**
- Start with proper data preprocessing
- Split data into train/validation/test sets
- Implement feature engineering as appropriate
- Handle class imbalance using techniques like:
  - SMOTE (Synthetic Minority Oversampling)
  - Class weights
  - Stratified sampling
- Tune hyperparameters using Spark's cross-validation
- Compare multiple algorithms with proper evaluation metrics

### 4. Visualization Requirements
- Generate plots and tables to support findings
- Use matplotlib, seaborn, or Spark's built-in visualization
- Ensure visualizations are clear and informative
- Include proper labels, titles, and legends

## Documentation

- Read `docs/notes/06_tue.md` for the marking scheme
- Read `mats/coursework.pdf` for complete assignment details
- Document your approach in each task folder
- Include a README in each task directory explaining:
  - What the code does
  - How to run it
  - Expected outputs
  - Any dependencies

## Performance Considerations

When working with large datasets:
- Use Spark's distributed processing capabilities
- Monitor job progress in Spark UI
- Optimize data formats (Parquet is recommended)
- Use appropriate file sizes and partitioning
- Avoid collecting large datasets to driver
- Use efficient serialization (Kryo)

## Submission

Each task should include:
- Source code (Python scripts or notebooks)
- Output files (if applicable)
- Documentation explaining approach and findings
- Visualizations (plots, charts, tables)

## Key Files to Reference

- `mats/coursework.pdf` - Complete coursework specification and requirements
- `docs/notes/06_tue.md` - Marking scheme and requirements
- `structure.md` - Directory structure layout

---

**Note**: This is an academic project focused on learning Big Data concepts with Apache Spark. Prioritize correctness, clarity, and proper Spark usage over premature optimization.
