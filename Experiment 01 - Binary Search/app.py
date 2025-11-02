import os

def load_books():
    # Load file from same directory as script
    file_path = os.path.join(os.path.dirname(__file__), "books.txt")
    books = []
    with open(file_path, "r") as file:
        for line in file:
            books.append(line.strip())
    return books

def binary_search_recursive(books, target, low, high):
    if low > high:
        return -1  # book not found
    
    mid = (low + high) // 2
    
    if books[mid].lower() == target.lower():
        return mid
    elif target.lower() < books[mid].lower():
        return binary_search_recursive(books, target, low, mid - 1)
    else:
        return binary_search_recursive(books, target, mid + 1, high)

def main():
    print("\n===== Library Book Finder (Binary Search - Recursion) =====")
    books = load_books()
    target = input("\nEnter book title to search: ")

    index = binary_search_recursive(books, target, 0, len(books) - 1)

    if index != -1:
        print(f"\n✅ Book found at position {index + 1}: {books[index]}\n")
    else:
        print("\n❌ Book not found in library records.\n")

if __name__ == "__main__":
    main()
