import os

class ListFolderData:
    def __init__(self, folder):
        self.folder = folder

    def list_files(self):
        return [
            os.path.join(root, file)
            for root, dirs, files in os.walk(self.folder)
            for file in files
        ]

    def list_folders(self):
        return [
            os.path.join(root, dir)
            for root, dirs, _ in os.walk(self.folder)
            for dir in dirs
        ]