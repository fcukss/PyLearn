class File:
    def __init__(self, path, filename, extension="png"):
        self.path = path
        self.filename = filename
        self.extension = extension
        self.is_opened = False

    def open(self):
        if self.is_opened == False:
            self.is_opened = True
        else:
            return f"Ошибка. Файл {str(self)} уже открыт"

    def close(self):
        if self.is_opened == True:
            self.is_opened = False
        else:
            return f"Ошибка. Файл {str(self)} уже закрыт"

    def read(self):
        if self.is_opened == True:
            return self.filename
        else:
            return f"Ошибка чтения. Файл {str(self)} закрыт"

    def __str__(self):
        return f"{self.path}/{self.filename}.{self.extension}"


class VideoFile(File):
    def __init__(self, path, filename, extension="png", length="0:00"):
        super().__init__(path, filename, extension)
        self.length = length

    def get_read_error(self):
        return f"Ошибка чтения. Файл {str(self)} закрыт"

    def read(self):
        if not self.is_opened:
            return self.get_read_error()
        return f"Показываем {self.filename}"


file1 = File(456, "Book")
file2 = File(13, "Magazine", "jpeg")
video_file = VideoFile('top_movies', 'Mimino', 'mkv', '97:00')

file1.open()
print(file1.read())
print(file1.open())
print(file1.close())
print(file1.read())

print(video_file)
print(video_file.read())
