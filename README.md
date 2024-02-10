# Data Pipeline Setup and Documentation

## Setup and Run Data Pipeline:

1. **Environment Setup:**
   - Make sure you have Python 3.12 installed on your system.
   - Set up a virtual environment for the project to manage dependencies.
   - Install Poetry, a dependency management tool, using the following command:
     ```bash
     pip install poetry
     ```

2. **Clone the Repository:**
     ```bash
     git clone <repository_url>
     cd <repository_directory>


3. **Install Dependencies:**
   - Run the following command to install project dependencies:
     ```bash
     Copy code
     poetry install

4. **Run the Data Pipeline:**
   - Execute the main Python script to run the data pipeline:
     ```bash
     Copy code
     poetry run python bq_to_parquet.py
