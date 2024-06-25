#!/usr/bin/bash

# Function to display content of Python files
display_python_files() {
  local directory=$1

  # Find all Python files excluding those in __pycache__ directories
  find "$directory" -type f -name "*.py" ! -path "*/__pycache__/*" -print0 | while IFS= read -r -d '' file; do
    echo "Displaying: $file"
    cat "$file"
    echo -e "\n-------------------------------\n"
  done
}

# The directory to search for Python files
project_directory="."

# Call the function with the project directory as argument
display_python_files "$project_directory"
