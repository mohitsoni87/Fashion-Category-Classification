#!/bin/bash

# Step 1: Run pytest
echo "Running pytest..."
pytest
if [ $? -ne 0 ]; then
  echo "Tests failed. Exiting..."
  exit 1
fi
echo "Tests passed."

# Step 2: Start the Flask server
echo "Starting the Flask server..."
#exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app

exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
