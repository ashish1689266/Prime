with open("sample.txt", "r") as file1:
    
    line_no = 1
    while True:
        data = file1.readline()
        if "python" in data:
            print(f"The string 'python' is in line {line_no}")
            break
        line_no += 1
    