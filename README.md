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

## Additional Notes
Add any additional notes, troubleshooting tips, or caveats here.
- Replace `<repository_url>` and `<repository_directory>` with the appropriate values.
- Also, make sure to replace `/path/to/your/service-account-key.json` with the actual path to your service account key file.
