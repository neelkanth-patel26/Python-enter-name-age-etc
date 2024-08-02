def data(fn, ln, age):
    print("First name:", fn)
    print("Last name:", ln)
    print("Age:", age)
    print("====================")

while True:
    fn = input("Enter first name: ")
    ln = input("Enter last name: ")
    age = input("Enter age: ")
    
    data(fn, ln, age)
    print("____________________")
    more = input("Would you like to add another name? (yes/no): ").strip().lower()
    if more != 'yes':
        break
