"""
нужно взять книгу и скопировать одну главу в другой файл
"""


def main():
    #read the file
    with open("alice.txt", 'r', encoding="utf-8") as file:
        #convert file into lists of lines
        contents = file.readlines()

    #see where start and end the chapter1
    chapter1 = contents[52:271]
    with open("chapter1.txt", 'w', encoding="utf-8") as f:
        for item in chapter1:
            f.writelines(item)


main()