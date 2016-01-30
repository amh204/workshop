books = ("Tale of Two Cities", "Harry Potter", "Lord of the Rings", "Stranger in a Strange Land")
nums = range(10)

for b in (nums):  # select the pointer for the list of nums
    print(books[b]) # print from the list of books with the pointer from b
    print(b)