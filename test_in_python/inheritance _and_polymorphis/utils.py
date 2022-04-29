from abc import ABC, abstractmethod
import datetime as dt
import csv
import string

class Writefile:
    
    def __init__(self, file_path):
        self.file_path = file_path

        @abstractmethod
        def write(self):
            return

class Logfile(Writefile):

    def write(self, value):

        dt_str = dt.datetime.now().strftime(r"%Y-%m-%d  %H:%M")

        with open(self.file_path, "a") as f:
            f.write(dt_str + "\t" + value + "\n")

class Delimfile(Writefile):

    def __init__(self, file_path, sep):
        super().__init__(file_path)
        self.sep = sep

    def write(self, value:list):
        
        with open(self.file_path, "a", newline="") as csv_file:

            csvwriter = csv.writer(csv_file, delimiter=self.sep)
            csvwriter.writerow(f"{''.join(value)}")

        return
