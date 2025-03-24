
def main():
    greeting = input("Greeting: ").lower().strip()
    print(f"${value(greeting)}")

def value(ans):
    if ans.startswith('hello'):
        return 0
    elif ans.startswith("h",0,1):
        return 20
    else:
        return 100

if __name__ == '__main__':
    main()
