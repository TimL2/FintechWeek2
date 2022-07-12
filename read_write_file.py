from pathlib import Path

print(f'Current working directory: {Path.cwd()}')



filepath = Path('C:/Users/sarob/Desktop/FinTech/coding-boot-camp/Wk2/output.txt')

with open(filepath, 'r') as file:
    text = file.read()
    print(text)
    
    line_num = 1
    for line in file:
        print(f"line {line_num}: {line}")
        line_num += 1

        
output_path = Path("output.txt")


with open(output_path, 'w') as file:
    file.write("This is an output file.\n")
    file.write(text)