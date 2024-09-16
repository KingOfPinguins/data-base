from datetime import datetime


class log():
    def __init__(self, interest, city):
        self.list_data = []
        time = str(datetime.now().strftime("%Y%m%d"))
        fileName = ".\\logs" + "\\" + time + "_" +interest + "_" + city + ".log"
        self.logF = open(fileName, "w")



    def add_to_log(self, data):
        #self.list_data.append( str(datetime.now()) + " :: " + str(data))
        print(str(datetime.now()) + " :: " + str(data))
        self.logF.write( "\n" + str(datetime.now()) + " :: " + str(data))

    def testClass(self):
        print("logger started!!!")

    # clean logger data(make a <self.list_data> empty)
    def __clean_log__(self):
        res = False
        try:
            self.list_data = []
            res = True
        except LookupError:
            return
        return res

    # read ALL data from <self.list_data>
    def read_log(self):
        return self.list_data

    # looking for a some data in a log
    def find_in_log(self, lookFor):
        found_data = []
        for dat in self.list_data:
            if str(lookFor) in str(dat):
                found_data.append(dat)
        return found_data
    
    def close_log(self):
        self.logF.close()