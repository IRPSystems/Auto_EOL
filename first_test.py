import subprocess
import glob
import os
import shutil


# Get base directory path (main application folder)
#base_dir = input("Enter the main folder path: ").replace("<username>", os.getlogin())
base_dir = r"C:\Users\ilyar\Desktop\Tester Package - NG_v1.0.7 Configuration"

# Path to the Sequence folder in the new location
sequence_dir = r"C:\Users\ilyar\PycharmProjects\Automation\Sequence"  # Corrected path2

# Mapping of project names to folder names
project_folders = {
    "MZG (Zor-Grand)": "Zor_Grand",
    "MNGP (NewGen)": "New_Gen",
    "TI": "TI",
    "Gensol": "Gensol",
    "Treo": "Treo",
    "Silence": "Silence"
}


def create_reports_directory():
    # Define the path for the Reports directory
    reports_dir = os.path.join(base_dir, "Reports")
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)
        print(f"Created 'Reports' directory at {reports_dir}")
    else:
        print("'Reports' directory already exists.")

    # Return the path of the created or existing Reports directory
    return reports_dir


def show_menu():
    print("Select a mode:\n1. EOL mode\n2. FT mode\n3. Exit")


def show_project_menu(mode):
    print(f"Select a project for {mode}:")
    for i, project in enumerate(project_folders.keys(), 1):
        print(f"{i}. {project}")
    choice = int(input("Enter the project number: "))
    if 1 <= choice <= len(project_folders):
        project_name = list(project_folders.keys())[choice - 1]
        print(f"Running {mode} for project: {project_name}")
        replace_files_with_project_files(mode, project_folders[project_name])
        run_app(mode)  # Pass mode to differentiate EOL or FT
    else:
        print("Invalid choice. Please try again.")


def replace_files_with_project_files(mode, project_folder_name):
    project_path = os.path.join(sequence_dir, project_folder_name)

    if not os.path.exists(project_path):
        print(f"Project folder '{project_folder_name}' does not exist.")
        return

    target_dirs = [
        os.path.join(base_dir, "FunctionalTester_Script"),
        os.path.join(base_dir, "EOL_Script"),
        os.path.join(base_dir, "TP_ProjectFiles")
    ]

    # Delete old .json files in the target directories before replacing
    for target_dir in target_dirs:
        if os.path.isdir(target_dir):
            for file_name in os.listdir(target_dir):
                file_path = os.path.join(target_dir, file_name)

                # Delete only .json files, excluding PackageConfigs.json
                if file_name.endswith(".json") and not file_name.startswith("PackageConfigs") and os.path.isfile(
                        file_path):
                    os.remove(file_path)
                    print(f"Deleted old .json file: {file_path}")
        else:
            print(f"Target directory {target_dir} does not exist. Skipping file deletion.")

    # Replace files in the target directories
    for file_name in os.listdir(project_path):
        if file_name.endswith(".json"):  # Replace this condition with the appropriate file type if needed
            source_file = os.path.join(project_path, file_name)

            for target_dir in target_dirs:
                if os.path.isdir(target_dir):
                    target_file = os.path.join(target_dir, file_name)

                    if os.path.isfile(source_file):
                        shutil.copy2(source_file, target_file)
                        print(f"Replaced {target_file} with {source_file}")
                else:
                    print(f"Target directory {target_dir} does not exist. Skipping file replacement.")


def run_app(mode):
    user_config_path = os.path.join(base_dir, "EOL_App", "user.config")
    if os.path.exists(user_config_path):
        os.remove(user_config_path)
        print(f"Deleted {user_config_path}")
    else:
        print("user.config file not found.")

    # Debugging: Print the directory being searched
    exe_dir = os.path.join(base_dir, "EOL_App")
    print(f"Searching for executables in: {exe_dir}")


    # Define the executable file pattern
    exe_file = None
    if mode == "EOL mode":
        exe_file = glob.glob(os.path.join(exe_dir, "EOL_Tester_*.exe"))
    # elif mode == "FT mode":
    #     exe_file = glob.glob(os.path.join(exe_dir, "EOL_Tester_*.exe"))
    exe_path = "C:/Users/ilyar/Desktop/Tester Package - NG_v1.0.7 Configuration/EOL_App/EOL_Tester_v2.0.41.exe"
    process = subprocess.Popen([exe_path])
    process.wait()

    # Print the list of files found for debugging
    print(f"Files found for {mode}: {exe_file}")

    # Run the executable file if found
    if exe_file:
        print(f"Running {exe_file[0]}")
        subprocess.run(exe_file[0], check=True)
    else:
        print(f"No executable found for {mode}.")

# Create the 'Reports' directory and save the path in 'path_report'
path_report = create_reports_directory()

# Print the path to the Reports directory
print(f"Reports directory is located at: {path_report}")

while True:
    show_menu()
    choice = input("Enter your choice (1/2/3): ")
    if choice == '1':
        show_project_menu("EOL mode")
    elif choice == '2':
        show_project_menu("FT mode")
    elif choice == '3':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")
