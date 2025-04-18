import random
import os

def add_random_number_to_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return

    modified_lines = []
    for line in lines:
        random_number = random.randint(1, 100)  # Generate a random number between 1 and 100
        modified_line = line.strip() + f" {random_number}\n"
        modified_lines.append(modified_line)

    with open(filename, 'w') as file:
        file.writelines(modified_lines)

if __name__ == "__main__":
    file_path = os.environ.get('FILE', '/redhat/materials/numbers.txt')  # Replace with the actual path to your text file
    add_random_number_to_file(file_path)
    print(f"Random numbers added to each line in '{file_path}'.")