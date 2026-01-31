from functions.get_files_info import get_files_info

def main():
    working_dir = "calculator"
    root_content = get_files_info(working_dir)
    print(root_content)

    pkg_content = get_files_info(working_dir, "pkg")
    print(pkg_content)

    outside_dir_content = get_files_info(working_dir, "/bin")
    print(outside_dir_content)

    other_dir_content = get_files_info(working_dir, "../")
    print(other_dir_content)



if __name__ == "__main__":
    main()
    