def main():
    folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
    print(removeSubfolders(folder))

def removeSubfolders(folder: list[str]):
    folder.sort()
    result = []

    for path in folder:
        if not result or not path.startswith(result[-1] + '/'):
            result.append(path)

    return result

if __name__ == "__main__":
    main() 