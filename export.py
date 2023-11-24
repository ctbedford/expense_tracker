import json
import os

def list_files(directory, extensions, exclude):
    """
    List all files in a directory structure, skipping specified directories.
    Only files with the given extensions are listed.
    """
    file_structure = {}
    for root, dirs, files in os.walk(directory, topdown=True):
        # Exclude specified directories
        dirs[:] = [d for d in dirs if d not in exclude]

        # Add files to the file structure
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                path = os.path.relpath(os.path.join(root, file), directory)
                file_structure[path] = None  # Initialize with None; content to be added if required

    return file_structure

def add_file_content(file_structure, root_directory):
    """
    Add the content of the files to the file structure dictionary.
    """
    for file_path in file_structure:
        try:
            with open(os.path.join(root_directory, file_path), 'r', encoding='utf-8') as file:
                file_structure[file_path] = file.read()
        except Exception as e:
            print(f"Error reading file {file_path}: {e}")

def main():
    # Configuration
    root_directory = '.'  # Start from the current directory
    relevant_extensions = ('.py', '.js', '.jsx', '.css', '.html', '.txt', '.md', 'Dockerfile', '.yml')
    directories_to_exclude = {
        '__pycache__', 'node_modules', '.git', 
        'build', 'dist', 'coverage', 'migrations', 
        'env', 'venv', '.vscode', '.idea'
    }

    # List all relevant files
    file_structure = list_files(root_directory, relevant_extensions, directories_to_exclude)

    # Uncomment the next line if you want to include the content of the files in the JSON
    add_file_content(file_structure, root_directory)

    # Export the file structure to a JSON file
    json_filename = 'project_structure.json'
    with open(json_filename, 'w', encoding='utf-8') as json_file:
        json.dump(file_structure, json_file, indent=4)

    print(f"Project structure has been saved to {json_filename}")

if __name__ == "__main__":
    main()