
#
# def print_with_indent(value, indent = 0):
#     indentation = " " * indent
#     print(indentation + str(value))
#
# def test_print(indent):
#     print_with_indent("Stas", indent = indent)
#     if indent <10:
#         test_print(indent+1)
# test_print(0)
#
# print('-----------------------------------------------')
#

# import os
# """
# метод показывает соддержимое папки"""
#
# def list_content(folder, depth =0):
#     for item in os.listdir(folder):
#         full_path = os.path.join(folder, item)
#         print(depth, full_path)
#         if os.path.isdir(full_path):
#             list_content(full_path, depth +1 )
# # depth - глубина рекурсии
# list_content('D:\Stas\PYTHON')

print('-----------------------------------------------')


def print_recursively(files):
    print(files['path'])
    for i in files['content']:
        print_recursively(i)


filesystem = {
    'path': 'C:',
    'content': [
        {
            'path': 'documents',
            'content': [
                {
                    'path': 'pictures',
                    'content': [
                        {
                            'path': 'me.png',
                            'content': [],
                        },
                        {
                            'path': 'keks.png',
                            'content': [],
                        }
                    ]
                }
            ]
        }
    ]
}

print_recursively(filesystem)

print('-----------------------------------------------')
#
# def print_recursively(new_list):
#     for item in new_list:
#         if isinstance(item, list):
#             print_recursively(item)
#         else:
#             print(item)
#
#
# list_of_lists = [10, [[1, [2, 3, [1]]], [1, [2]]]]
#
# print_recursively(list_of_lists)
#
# print(isinstance(list_of_lists[0], list))
# print(isinstance(list_of_lists[1], list))