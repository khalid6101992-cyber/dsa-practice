class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        print(tokens)
        result = []
        for token in tokens:
            if token not in {"+","-","/","*"}:
                result.append(int(token))
            else:
                data1 = int(result.pop())
                data2 = int(result.pop())
                if token == "+":
                    data = data1 + data2
                elif token == "-":
                    data = data2 - data1
                elif token == "*":
                    data = data1 * data2
                elif token == "/":
                    data = int(data2 / data1)
                result.append(data)
        return result[-1]