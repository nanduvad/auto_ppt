import os

class FileAgent:

    def save(self, presentation, path):

        os.makedirs(os.path.dirname(path), exist_ok=True)
        presentation.save(path)

        return f"Saved successfully at {path}"