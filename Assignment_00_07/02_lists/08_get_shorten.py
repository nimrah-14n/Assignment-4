MAX_LENGTH = 3  # Define the maximum allowed length

def shorten(lst):
    while len(lst) > MAX_LENGTH:  # Jab tak list ka size MAX_LENGTH se bada hai
        removed_item = lst.pop()  # Last element remove karo
        print("Removed:", removed_item)  # Remove kiya hua item print karo

def main():
    lst = []  #
    
    # collect an input list from a user
    n = int(input("Enter number of elements in the list: "))
    for _ in range(n):
        value = input("Enter a value: ")
        lst.append(value)

    print("Original list:", lst)  # Print first list
    shorten(lst)  # call a shorten function
    print("Shortened list:", lst)  # print a final list


if __name__ == '__main__':
    main()