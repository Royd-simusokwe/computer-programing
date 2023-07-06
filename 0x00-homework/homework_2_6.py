def main():
    #a
    contacts={
        "john": "john@gm,com",
        "jane": "jane@g.com",
        "bob": "bob"
    }
    #b
    print(contacts["jane"])

    #c
    contacts.update({"john": "john.doe@g.com"})

    #d
    if "alice" in contacts:
        print("its in ")
    else:
        print("it doesnt exist")

    #e
    contacts.pop("bob")

    #f
    print(contacts)
if __name__ == "__main__":
  main()