from pathlib import Path

path_input = "C:\Users\eepie\Documents\text_files"
count = 0
path = Path(path_input)
for file in path.glob('*.txt'):    #allows us search for all txt files in the emails directory directories
    count += 1
    #print(file)
print(f'Total .txt file count = {count}')

#path.glob('*.txt') creates a generator objects