import os

def count_text_files(directory):
    count = 0
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            count += 1
    return count

if __name__ == "__main__":
    directory_path = input("Enter the directory path: ")
    if os.path.isdir(directory_path):
        num_files = count_text_files(directory_path)
        print(f"Number of text files in '{directory_path}': {num_files}")
    else:
        print("Invalid directory path.")
