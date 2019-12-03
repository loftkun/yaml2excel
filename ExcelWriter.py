import xlsxwriter   # sudo -E pip3 install xlsxwriter

class ExcelWriter():
    workbook = None

    def makeBook(self, name):
        print("makeBook : " + name)
        self.workbook = xlsxwriter.Workbook(name)

    def appendSheet(self, path, dics):
        print("appendSheet : " + path)
        worksheet = self.workbook.add_worksheet()

        worksheet.write('A1', path)

        row = 3
        col = 0
        for dic in dics:
            # insert_textbox
            #   https://xlsxwriter.readthedocs.io/worksheet.html#insert_textbox
            worksheet.insert_textbox(row, col, dic["kind"] + "\n" + dic["metadata"]["name"])
            row = row + 7

    def close(self):
       self.workbook.close()
