# Running the Project

## Running Locally
1. **Run the Python script:**
   ```bash
   python script.py
   ```

## Running with Docker
1. **Build the Docker image:**
     ```bash
     docker build -t project-image .
     ```
2. **Run the Docker container:**
     ```bash
     docker run --rm -e GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service-account-key.json" project-image
     ```
