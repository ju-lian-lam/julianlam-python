students = int(input("Enter the number of students: "))
books = int(input("Enter the number of books: "))
print("The number of books each is:", books // students)
print("The number left over is:", books % students)