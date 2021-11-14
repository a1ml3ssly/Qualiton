import os.path
from pathlib import Path


class Utilities:
    __author__ = "Nitzan Bachar"
    __version__ = "1.0.0"
    @staticmethod
    def get_project_root():
        return str(Path(__file__).parent.parent)


print(os.path.dirname(os.path.abspath(__file__)))
