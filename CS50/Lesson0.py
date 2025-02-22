# def main():
#     text = input()
#     print(text.replace(" ", "...")+":)")
#


def convert(input_str):
    """
    Функция принимает строку и заменяет эмотиконы :) на эмодзи 🙂 и :( на 🙁.
    """
    # Заменяем :) на 🙂
    output_str = input_str.replace(":)", "🙂")
    # Заменяем :( на 🙁
    output_str = output_str.replace(":(", "🙁")
    return output_str

def main():
    str = input()
    print(convert(str))

main()
