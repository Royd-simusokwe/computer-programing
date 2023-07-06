def main():
    #a
    student = {
        "name": "john",
        "age": 20,
        "grade": "A"

    }
    #b
    print(student["age"])

    #c
    student["city"] = "new york"
    print(student)

    #d
    if "grade" in student:
        print("its there")

    #e
    student.pop("age")
    print(student)

    #f
    print(student.keys)

if __name__ == "__main__":
  main()