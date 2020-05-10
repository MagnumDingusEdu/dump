import unittest  # for actual testing
import os
import pathlib  # for traversing the directories
import re  # for checking filenames


class testFileStructure(unittest.TestCase):

    def setUp(self):
        # Find and set the path to the base of the repository
        self.root_folder = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__)))

        # Generate a list of all directories in the repo
        self.files = []
        self.directories = []
        for (dirpath, dirnames, filenames) in os.walk(self.root_folder):
            self.files.extend((filenames))
            self.directories.extend((dirnames))
            # In order to only list files in the root folder
            break

    def test_directorystructure(self):

        for filz in self.files:
            # no files with .py extensions should be in the root of the directory
            self.assertNotEqual(pathlib.Path(
                filz).suffix, ".py", f"Python files are not allowed in the root of the project")

    def test_personal_folders(self):

        for dirz in self.directories:
            if dirz == "test" or dirz[0] == ".":
                continue
            # There should be only one file inside each folder
            self.assertEqual(len(os.listdir(
                dirz)), 1, f"Only one file is allowed inside each folder. Offending folder : {dirz}")

    def test_extensions_infolders(self):
        for dirz in self.directories:
            if dirz == "test" or dirz[0] == ".":
                continue

            for filzs in os.listdir(dirz):
                # There should be only one file inside each folder
                self.assertEqual(pathlib.Path(
                    filzs).suffix, ".py", f"Only .py files are allowed in the subfolders. Offending folder : {dirz}")


if __name__ == "__main__":

    unittest.main()
