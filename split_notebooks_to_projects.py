import os
import shutil

# Use an absolute path to the notebooks folder
notebooks_path = r"C:\Users\Family\DS_PRACTICE\ML_MODELS\notebooks"  # Update this to your absolute path

# Define the base directory where projects will be created
base_project_path = r"C:\Users\Family\DS_PRACTICE\ML_MODELS\projects"  # Update this to your absolute path

# Check if the notebooks path exists
if not os.path.exists(notebooks_path):
    print(f"Error: The path {notebooks_path} does not exist.")
else:
    # List all the files in the notebooks directory
    notebook_files = [f for f in os.listdir(notebooks_path) if f.endswith('.ipynb')]

    for notebook in notebook_files:
        # Remove the file extension to create the project folder name
        project_name = os.path.splitext(notebook)[0]
        
        # Create a new directory for the project
        project_dir = os.path.join(base_project_path, project_name)
        os.makedirs(project_dir, exist_ok=True)
        
        # Create subdirectories to replicate the project structure
        subdirs = ['data', 'notebooks', 'scripts', 'models', 'outputs']  # Adjust this list based on your preferred structure
        for subdir in subdirs:
            os.makedirs(os.path.join(project_dir, subdir), exist_ok=True)
        
        # Move the notebook into the new 'notebooks' subdirectory
        src = os.path.join(notebooks_path, notebook)
        dst = os.path.join(project_dir, 'notebooks', notebook)
        shutil.move(src, dst)
        
        print(f"Moved {notebook} to {project_dir}/notebooks")

    print("All notebooks have been organized into separate projects with their structures intact.")
