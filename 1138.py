class Solution:

    
    def alphabetBoardPath(self, target: str) -> str:
        
        def go_alphabet(t, curr, output):
            # print(t, curr)


            board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
            board2 = ["afkpuz", "bglqv", "chmrw", "dinsx", "ejoty"]
            # print(board)
            r = [idx for idx, row in enumerate(board) if t in row][0]
            c = [idx for idx, col in enumerate(board2) if t in col][0]

                        
            flag = True
            if (r == 5) and (curr[1] != 0):
                flag = False
                r_move = curr[0] - r + 1
            else :
                flag = True
                r_move = curr[0] - r
            
            # r_move = curr[0] - r
            c_move = curr[1] - c


            if r_move > 0:
                output += ["U"] * r_move
            else:
                output += ["D"] * (r_move * -1)

            if c_move > 0:
                output += ["L"] * c_move
            else:
                output += ["R"] * (c_move * -1)
                
            if flag == False:
                output += ["D"]

            print(output)
            print(r,c)
            
            output += ["!"]

            return (r,c), output
        
        start = (0,0)
        output = []
        for t in target:
            start, output = go_alphabet(t, start, output)
        
        output = "".join(output)
        return output
            

