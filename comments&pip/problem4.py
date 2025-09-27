import os

def print_directory(path='.'):
    """
    Print all files and directories inside the given path.
    If no path is given, it uses the current directory.
    """
    try:
        entries = os.listdir(path)
    except FileNotFoundError:
        print(f"Directory not found: {path}")
        return
    except NotADirectoryError:
        print(f"Not a directory: {path}")
        return
    except PermissionError:
        print(f"Permission denied: {path}")
        return

    print(f"Contents of '{path}':")
    for name in entries:
        print(name)

if __name__ == "__main__":
    # You can change this to any directory
    dir_path = input("Enter directory path (or press enter for current directory): ").strip()
    if not dir_path:
        dir_path = '.'
    print_directory(dir_path)
