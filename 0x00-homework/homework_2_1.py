def main():
    def  factorial(n):
        if(n==0):
            return 1
        else:
        
            return n * factorial(n-1)
    num = 1
    print(factorial(num))

if __name__ == "__main__":
  main()