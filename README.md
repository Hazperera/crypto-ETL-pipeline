
# Crypto-ETL-Data Pipeline 

## Setup and Run Data Pipeline:

### Running Locally

1. **Environment Setup:**
   - Make sure you have Python 3.12 installed on your system.
   - Set up a virtual environment for the project to manage dependencies.
   - Install Poetry, a dependency management tool:
     ```bash
     pip install poetry
     ```

2. **Clone the Repository:**
   - Use the following commands to clone the repository and change to the directory:
     ```bash
     git clone <repository_url>
     cd <repository_directory>
     ```

3. **Install Dependencies:**
   - Install project dependencies with Poetry:
     ```bash
     poetry install
     ```

4. **Run the Data Pipeline:**
   - To execute the main Python script:
     - First, activate the Poetry shell:
     ```bash
     poetry shell 
     ```
     - Set the environment variable for Google credentials:
     ```bash
     export GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/service-account-key.json
     ```
     - Run the script:
     ```bash
     python bq_to_parquet.py
     ```
     
## System Architecture Diagram:

Draft Workflow](images/sys_architecture_diagram.png)
