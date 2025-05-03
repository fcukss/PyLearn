# ===========================  Regular Expression (ReExp)

import re

text = ('Use our game-changing fully managed development environment '
        'Vertex AI Vision to create your own computer vision applications '
        'or derive insights from images and videos with pre-trained APIs,  AutoML, or custom models.'
        'Easily build, deploy and manage computer vision applications for your unique business needs '
        'with pre-trained APIs, AutoML and custom models.'
        'Whether you need plug and play analytics via APIs or the ability to use custom ML models '
        'or an end to end development environment, our vision portfolio has a solution.'
        'Benefit from Google\'s investments in vision across our portfolio. Google\'s vision '
        'offerings have received the highest ratings from several analyst firms.')

# pattern = r"[a-mo-zA-PW-Z]"
# pattern = r"\s[a-z]\s"
# pattern = r"\s[a-z]+\s"
# pattern = r"[\d]"
# pattern = r"...."
# pattern = r".{4}"
# pattern = r".{3,6}"
# pattern = r"\w+"
# pattern = r"\bG\w+\'?.?"
# pattern = r"[^a-z\s]"
# pattern = r"[A-Z]"
# pattern = r"G..{3,5}\'s"
# pattern = r"[G|U]\w+"
# x = re.findall(pattern, text)
# print(x)

# x = re.findall('Google\'s', text)
# print(x)
# x = re.findall('NL', text)
# print(x)

# x = re.search('Google', text)
# print(x)
# print(x.start())
# print(x.end())
# print(x.span())
# print(x.string)
# print(x.group())
# x = re.search('Goole', text)
# print(x)

# x = re.split('Google', text)
# print(x)
# print(len(x))
# x = re.split('Google', text, maxsplit=1)
# print(len(x))

# x = re.sub('Google', 'NEWS', text)
# print(x)
# x = re.findall('Google\'s', x)
# print(x)
# x = re.findall('NEWS\'s', x)
# print(x)