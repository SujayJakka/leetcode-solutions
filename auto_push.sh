#!/bin/bash

# Navigate to your repo folder (update if your path is different)
cd ~/Documents/GitHub/leetcode-solutions

# Activate virtual environment
source .venv/bin/activate

# LeetCode session cookie (replace with your real cookie)
LEETCODE_SESSION="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiNjM3NzIxOSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImFsbGF1dGguYWNjb3VudC5hdXRoX2JhY2tlbmRzLkF1dGhlbnRpY2F0aW9uQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjAyOGQ1MmM2OTVhMDZhOWU3ZjAxYjVmMGY1MDIyNGI4YjY4NjliYjIyY2YyZjM4MjY0YzliZmRmMTAwZmY3ZGIiLCJzZXNzaW9uX3V1aWQiOiJhNDZhMzBkNSIsImlkIjo2Mzc3MjE5LCJlbWFpbCI6InN1amF5Lmpha2thQGdtYWlsLmNvbSIsInVzZXJuYW1lIjoidXNlcjAzNDN1IiwidXNlcl9zbHVnIjoidXNlcjAzNDN1IiwiYXZhdGFyIjoiaHR0cHM6Ly9hc3NldHMubGVldGNvZGUuY29tL3VzZXJzL2F2YXRhcnMvYXZhdGFyXzE2NTIzODI3OTMucG5nIiwicmVmcmVzaGVkX2F0IjoxNzUzNTQyNDgwLCJpcCI6IjIwNy45OC4xNDguOTkiLCJpZGVudGl0eSI6ImNlNjliODUxYzRlZGM3ZWViZmIzOTk4YWE5NGE3MTU3IiwiZGV2aWNlX3dpdGhfaXAiOlsiOTQ0NzE5MzFlMTk4N2Y0NjViMzk3NmQ1ZjljMzhhYjgiLCIyMDcuOTguMTQ4Ljk5Il19.dfOkho_h0gBH387qVVDYijaycQVfYWvGzm5-mAIDZ9E"

# Languages you want to export
LANGUAGES=("Python3" "C++" "Java" "Python" "JavaScript")

# Loop over each language and export into its own folder
for lang in "${LANGUAGES[@]}"; do
    echo "Exporting accepted $lang solutions..."
    mkdir -p "$lang"
    leetcode-export --leetcode-session "$LEETCODE_SESSION" --lang "$lang" --dir "$lang"
done

# Stage all changes
git add .

# Commit with timestamp
git commit -m "Auto update on $(date +'%Y-%m-%d %H:%M:%S')"

# Push to GitHub
git push origin main

# Deactivate the virtual environment
deactivate

