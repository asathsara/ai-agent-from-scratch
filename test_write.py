import functions.write_file as write_file

def main():
    working_dir = "calculator"
    write_file.write_file(working_dir, "pkg/test.txt", "Hello World")
    write_file.write_file(working_dir, "pkg2/test.txt", "Hello World")
    write_file.write_file(working_dir, "/pkg3/test.txt", "Hello World")

if __name__ == "__main__":
    main()