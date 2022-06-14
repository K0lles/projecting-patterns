class Memento:

    def __init__(self, content: str, file_name: str):
        self.content = content
        self.file_name = file_name


class Notepad:

    def __init__(self, file_name: str):
        self.content = ""
        self.file_name = file_name

    def write(self, word: str):
        self.content += word

    def save(self):
        return Memento(self.content, self.file_name)

    def undo(self, memento: Memento):
        self.content = memento.content
        self.file_name = memento.file_name


class NotepadManager:

    def save(self, notepad: Notepad):
        self.current_state = notepad.save()

    def undo(self, notepad: Notepad):
        notepad.undo(self.current_state)


if __name__ == '__main__':
    notepad_manager = NotepadManager()
    notepad = Notepad("file.txt")
    notepad.write("Hello World!\n")
    notepad_manager.save(notepad)
    notepad.write("Goodbye\n")
    notepad_manager.save(notepad)
    notepad.write("Yeah\n")

    print(notepad.content)
    notepad_manager.undo(notepad)
    print(notepad.content)
