# file_handle = open("sample.txt","xt")
# file_handle.write("This is sample text file\n")
# file_handle.write("It contains multiple line")
# file_handle.close()
import os
file_name= "C:/Users/lovep/PycharmProjects/PythonProject/sample.txt"
if os.path.exists(file_name):
    file_handle = open("sample.txt","rt")
    Line1 = file_handle.readline()
    Line2 = file_handle.readline()
    print(f"Line1:{Line1.strip('\n')}")
    print(f"Line2:{Line2.strip('\n')}")
else:
    print(f"Error: File 'sample.txt' does not exist")

