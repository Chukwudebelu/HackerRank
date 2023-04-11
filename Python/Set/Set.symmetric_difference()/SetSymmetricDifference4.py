# Enter your code here. Read input from STDIN. Print output to STDOUT
def set_data() -> set:
    """Skip a line and read a set of space-delimited integers from STDIN."""
    input()
    return set(input().split(" "))


if __name__ == "__main__":
    print(len(set_data() ^ set_data()))
