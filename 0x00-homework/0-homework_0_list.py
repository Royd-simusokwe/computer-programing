def main():
  fun_of_dict()
  fun_of_list()
  fun_of_tuple()

def fun_of_list():
  # your code here
  my_list = ["apple","banana","cherry","date","elderberry"]
  print(len(my_list))
  print(my_list[2])
  my_list.remove("elderberry")
  my_list.insert(0, "fig")
  print(my_list)

def fun_of_tuple():
  # your code here
  my_tuple = (10,20,30,40,50)
  print(len(my_tuple))
  print(my_tuple[3])
  my_list = list(my_tuple)
  my_list[2] = 35
  my_tuple = tuple(my_list)
  print(my_tuple)

def fun_of_dict():
  # your code here
  my_dict = {
    "name": "john",
    "age": 25,
    "country": "USA"
  }
  print(my_dict["name"])
  my_dict["age"]= 26
  print(my_dict["country"])


if __name__ == "__main__":
  main()
