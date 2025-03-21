
def main():
    greeting = input("Greeting: ").lower().strip()
    value(greeting)

def value(ans):
    if ans.startswith('hello'):
        print("$0")
    elif ans.startswith("h",0,1):
        print("$20")
    else:
        print("$100")

if __name__ == '__main__':
    main()
