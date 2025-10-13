# 设计电子表格

class Spreadsheet:

    def __init__(self, rows: int):
        self.list = [[0] * 26 for _ in range(rows)]

    def setCell(self, cell: str, value: int) -> None:
        col = ord(cell[0]) - 65
        row = int(cell[1:]) - 1
        self.list[row][col] = value

    def resetCell(self, cell: str) -> None:
        col = ord(cell[0]) - 65
        row = int(cell[1:]) - 1
        self.list[row][col] = 0

    def getValue(self, formula: str) -> int:
        num1, num2 = formula[1:].split("+")
        num1 = int(num1) if num1.isdigit() else self.list[int(num1[1:])-1][ord(num1[0])-65]
        num2 = int(num2) if num2.isdigit() else self.list[int(num2[1:])-1][ord(num2[0])-65]

        return num1 + num2

def test_Spreadsheet():
    parameters = [["=5+7"], ["A1", 10], ["=A1+6"], ["B2", 15], ["=A1+B2"], ["A1"], ["=A1+B2"]]

    opera = ["getValue", "setCell", "getValue", "setCell", "getValue", "resetCell", "getValue"]

    tm = Spreadsheet(3)

    for i, para in enumerate(parameters):
        op = opera[i]
        if op == "setCell":
            tm.setCell(para[0], para[1])
        elif op == "resetCell":
            tm.resetCell(para[0])
        elif op == "getValue":
            result = tm.getValue(para[0])
            print(result)

test_Spreadsheet()

s = Spreadsheet(458)
print(s.getValue("=0126+10272"))

