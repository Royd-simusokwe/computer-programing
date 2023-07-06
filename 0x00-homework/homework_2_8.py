def main():
    scores={
        "alice": 85,
        "bob": 92,
        "charlie": 78
    }

    #b
    print(scores["bob"])

    #c
    scores["david"]= 95

    #d
    if "eve" in scores:
        print("it exits")
    else:
        print("it doesnt exist")

    #e
    scores.pop("charlie")
    #f
    print(scores)
if __name__ == "__main__":
  main()