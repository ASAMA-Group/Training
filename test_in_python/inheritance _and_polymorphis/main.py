from utils import Logfile, Delimfile 

if __name__ == "__main__":
    obj_log = Logfile("matin.txt")
    obj_delim = Delimfile("text.csv", ",")

    obj_log.write("this is a log message")
    obj_log.write("this is another long message")

    obj_delim.write(["a", "b", "c", "d"])
    obj_delim.write(["1", "2", "3", "4"])
