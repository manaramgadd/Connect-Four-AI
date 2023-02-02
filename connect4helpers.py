from bitarray import bitarray
import copy


class GameBoard:
    def __init__(self, board, mask, alpha, beta, score_y, score_r, turn, depth, heuristic):
        self.board = bitarray(board)
        self.mask = bitarray(mask)
        self.alpha = alpha
        self.beta = beta
        self.pos = 0
        self.pruned = False
        self.utility = 0
        self.score_r = score_r
        self.score_y = score_y
        self.depth = depth
        self.turn = turn
        self.twos = 0
        self.threes = 0
        self.children = []
        self.setinitutility()

    def setinitutility(self):
        if self.turn == 0:
            self.utility = float('-inf')
        else:
            self.utility = float('inf')

    def __eq__(self, other):
        return (self.board, self.mask) == (other.board, other.mask)

    def child(self):
        # children = []
        self.children = []
        for i in range(7):
            copy_b = self.copy()
            # copy_b.turn = 1 ^ copy_b.turn
            copy_b.depth = copy_b.depth - 1
            # self.pos = \
            copy_b.make_move(i)
            copy_b.setinitutility()

            # print(copy_b.turn)
            if copy_b != self:
                child = copy_b
                self.children.append(child)
            
        # return children

    def __hash__(self):
        return hash((self.board.to01(), self.mask.to01()))

    def tostring(self):
        mask = self.mask.copy()
        # mask.reverse()
        board = self.board.copy()
        myboardstr = ""
        # board.reverse()
        for i in range(5, -1, -1):
            for j in range(7):
                pos = i + j * 7
                if mask[i + j * 7]:
                    if board[i + j * 7]:
                        myboardstr += "Y"
                    else:
                        myboardstr += "R"
                else:
                    myboardstr += " . "
            myboardstr += "\\n"
        return myboardstr

    def __str__(self):
        # use mask and board to print the board
        # print the board
        mask = self.mask.copy()
        # mask.reverse()
        board = self.board.copy()
        myboardstr = ""
        # board.reverse()
        for i in range(5, -1, -1):
            for j in range(7):
                pos = i + j * 7
                if mask[i + j * 7]:
                    if board[i + j * 7]:
                        myboardstr += "R "
                        print('R', end=' ')
                    else:
                        myboardstr += "Y "
                        print('Y', end=' ')
                else:
                    print('.', end=' ')
                    myboardstr += ". "
            myboardstr += "\n"
            print()
        return ""

    def get_position(self, col):
        # set position as 64 0s
        position = bitarray(64)
        position.setall(0)
        pos_helper = 7 * col
        pos = self.mask.index(0, pos_helper, pos_helper + 7)
        self.pos = pos
        # self.pos = pos
        if pos == 7 * col + 6:
            self.pos = -1
            return position
        position[pos] = 1
        return position

    def make_move(self, col):
        # use bitboard operations to make a move
        # check if the column is full
        pos = self.get_position(col)
        self.mask = pos | self.mask
        if self.turn == 1:
            self.board = pos | self.board
        self.turn = 1 ^ self.turn
        #self.win_detect()

    def copy(self):
        return GameBoard(self.board.to01(), self.mask.to01(), self.alpha, self.beta, self.score_y, self.score_r,
                         self.turn, self.depth, self.heuristic)

    def win_detect(self):
        cboard = self.board
        # cboard= self.board ^ self.mask
        # diagonal left
        scoreDL = (cboard & (cboard >> 6) & (cboard >> 12) & (cboard >> 18)).count(1)
        # diagonal right
        scoreDR = (cboard & (cboard >> 8) & (cboard >> 16) & (cboard >> 24)).count(1)
        # horizontal
        scoreHR = (cboard & (cboard >> 7) & (cboard >> 14) & (cboard >> 21)).count(1)
        # vertical
        scoreVR = (cboard & (cboard >> 1) & (cboard >> 2) & (cboard >> 3)).count(1)

        self.score_r = scoreDL + scoreDR + scoreHR + scoreVR
        # print("RED",self.score_r)
        cboard = self.board ^ self.mask
        scoreDL = (cboard & (cboard >> 6) & (cboard >> 12) & (cboard >> 18)).count(1)
        # diagonal right
        scoreDR = (cboard & (cboard >> 8) & (cboard >> 16) & (cboard >> 24)).count(1)
        # horizontal
        scoreHR = (cboard & (cboard >> 7) & (cboard >> 14) & (cboard >> 21)).count(1)
        # vertical
        scoreVR = (cboard & (cboard >> 1) & (cboard >> 2) & (cboard >> 3)).count(1)
        self.score_y = scoreDL + scoreDR + scoreHR + scoreVR

        self.utility = self.score_r - self.score_y

    def win_detect_alpha_beta(self):
        cboard = self.board
        # cboard= self.board ^ self.mask
        # diagonal left
        scoreDL = (cboard & (cboard >> 6) & (cboard >> 12) & (cboard >> 18)).count(1)
        # diagonal right
        scoreDR = (cboard & (cboard >> 8) & (cboard >> 16) & (cboard >> 24)).count(1)
        # horizontal
        scoreHR = (cboard & (cboard >> 7) & (cboard >> 14) & (cboard >> 21)).count(1)
        # vertical
        scoreVR = (cboard & (cboard >> 1) & (cboard >> 2) & (cboard >> 3)).count(1)
        # print("YELLOW",self.score_y)

    def connected_twos(self):
        y_board = self.board ^ self.mask
        r_board = self.board
        self.twos_r=0
        self.twos_y=0
        # horizontal check for red
        twoHR = r_board & (r_board >> 7) 
        twoHR=twoHR >>7
        intersection = twoHR & y_board
        intersection.invert()
        remaining = twoHR&intersection
        #print("horizontal",remaining.count(1))
        self.twos_r += remaining.count(1)
        # horizontal check back for red
        twoHR = r_board & (r_board << 7)
        twoHR=twoHR <<7
        intersection = twoHR & y_board
        intersection.invert()
        remaining = twoHR&intersection
        #print("horizontal",remaining.count(1))
        self.twos_r += remaining.count(1)
        #print(self.twos_r)
        # vertical check for red
        twoVR = r_board & (r_board << 1)
        twoVR=twoVR <<1
        intersection = twoVR & y_board
        intersection.invert()
        remaining = twoVR&intersection
        #print(remaining)
        self.twos_r += remaining.count(1)
        #print ("vertical",remaining.count(1))
        # diagonal left check for red
        twoDL = r_board & (r_board >> 6)
        twoDL=twoDL >>6
        intersection = twoDL & y_board
        intersection.invert()
        remaining = twoDL&intersection
        #print ("diagonal left",remaining.count(1))
        self.twos_r += remaining.count(1)
        # diagonal left check back for red
        twoDL = r_board & (r_board << 6)
        twoDL=twoDL <<6
        intersection = twoDL & y_board
        intersection.invert()
        remaining = twoDL&intersection
        self.twos_r += remaining.count(1)
        #print ("diagonal left",remaining.count(1))
        # diagonal right check for red
        twoDR = r_board & (r_board >> 8)
        twoDR=twoDR >>8
        intersection = twoDR & y_board
        intersection.invert()
        remaining = twoDR&intersection
        #print ("diagonal right",remaining.count(1))

        self.twos_r += remaining.count(1)
        # diagonal right check back for red
        twoDR = r_board & (r_board << 8)
        twoDR=twoDR <<8
        intersection = twoDR & y_board
        intersection.invert()
        remaining = twoDR&intersection
        #print ("diagonal right",remaining.count(1))
        self.twos_r += remaining.count(1)
        #print ("diagonal right",remaining.count(1))
        # horizontal check for yellow
        twoHR = y_board & (y_board >> 7)
        twoHR=twoHR >>7
        intersection = twoHR & r_board
        intersection.invert()
        remaining = twoHR&intersection
        self.twos_y = remaining.count(1)
        # horizontal check back for yellow
        twoHR = y_board & (y_board << 7)
        twoHR=twoHR <<7
        intersection = twoHR & r_board
        intersection.invert()
        remaining = twoHR&intersection
        self.twos_y += remaining.count(1)
        # vertical check for yellow
        twoVR = y_board & (y_board << 1)
        twoVR=twoVR <<1
        intersection = twoVR & r_board
        intersection.invert()
        remaining = twoVR&intersection
        self.twos_y += remaining.count(1)
        # diagonal left check for yellow
        twoDL = y_board & (y_board >> 6)
        twoDL=twoDL >>6
        intersection = twoDL & r_board
        intersection.invert()
        remaining = twoDL&intersection
        self.twos_y += remaining.count(1)
        # diagonal left check back for yellow
        twoDL = y_board & (y_board << 6)
        twoDL=twoDL <<6
        intersection = twoDL & r_board
        intersection.invert()
        remaining = twoDL&intersection
        self.twos_y += remaining.count(1)
        # diagonal right check for yellow
        twoDR = y_board & (y_board >> 8)
        twoDR=twoDR >>8
        intersection = twoDR & r_board
        intersection.invert()
        remaining = twoDR&intersection
        self.twos_y += remaining.count(1)
        # diagonal right check back for yellow
        twoDR = y_board & (y_board << 8)
        twoDR=twoDR <<8
        intersection = twoDR & r_board
        intersection.invert()
        remaining = twoDR&intersection
        self.twos_y += remaining.count(1)


    def connected_threes(self):
        y_board = self.board ^ self.mask
        r_board = self.board
        self.threes_r=0
        self.threes_y=0
        # horizontal check for red
        threeHR = r_board & (r_board >> 7) & (r_board >> 14)
        threeHR=threeHR >>7
        intersection = threeHR & y_board
        intersection.invert()
        remaining = threeHR&intersection
        self.threes_r += remaining.count(1)
        # horizontal check back for red
        threeHR = r_board & (r_board << 7) & (r_board << 14)
        threeHR=threeHR <<7
        intersection = threeHR & y_board
        intersection.invert()
        remaining = threeHR&intersection
        self.threes_r += remaining.count(1)
        # vertical check for red
        threeVR = r_board & (r_board << 1) & (r_board << 2)
        threeVR=threeVR <<1
        intersection = threeVR & y_board
        intersection.invert()
        remaining = threeVR&intersection
        self.threes_r += remaining.count(1)
        # diagonal left check for red
        threeDL = r_board & (r_board >> 6) & (r_board >> 12)
        threeDL=threeDL >>6
        intersection = threeDL & y_board
        intersection.invert()
        remaining = threeDL&intersection
        self.threes_r += remaining.count(1)
        # diagonal left check back for red
        threeDL = r_board & (r_board << 6) & (r_board << 12)
        threeDL=threeDL <<6
        intersection = threeDL & y_board
        intersection.invert()
        remaining = threeDL&intersection
        self.threes_r += remaining.count(1)
        # diagonal right check for red
        threeDR = r_board & (r_board >> 8) & (r_board >> 16)
        threeDR=threeDR >>8
        intersection = threeDR & y_board
        intersection.invert()
        remaining = threeDR&intersection
        self.threes_r += remaining.count(1)
        # diagonal right check back for red
        threeDR = r_board & (r_board << 8) & (r_board << 16)
        threeDR=threeDR <<8
        intersection = threeDR & y_board
        intersection.invert()
        remaining = threeDR&intersection
        self.threes_r += remaining.count(1)
        # horizontal check for yellow
        threeHR = y_board & (y_board >> 7) & (y_board >> 14)
        threeHR=threeHR >>7
        intersection = threeHR & r_board
        intersection.invert()
        remaining = threeHR&intersection
        self.threes_y = remaining.count(1)
        # horizontal check back for yellow
        threeHR = y_board & (y_board << 7) & (y_board << 14)
        threeHR=threeHR <<7
        intersection = threeHR & r_board
        intersection.invert()
        remaining = threeHR&intersection
        self.threes_y += remaining.count(1)
        # vertical check for yellow
        threeVR = y_board & (y_board << 1) & (y_board << 2)
        threeVR=threeVR <<1
        intersection = threeVR & r_board
        intersection.invert()
        remaining = threeVR&intersection
        self.threes_y += remaining.count(1)
        # diagonal left check for yellow
        threeDL = y_board & (y_board >> 6) & (y_board >> 12)
        threeDL=threeDL >>6
        intersection = threeDL & r_board
        intersection.invert()
        remaining = threeDL&intersection
        self.threes_y += remaining.count(1)
        # diagonal left check back for yellow
        threeDL = y_board & (y_board << 6) & (y_board << 12)
        threeDL=threeDL <<6
        intersection = threeDL & r_board
        intersection.invert()
        remaining = threeDL&intersection
        self.threes_y += remaining.count(1)
        self.threes_y -=1
        # diagonal right check for yellow
        threeDR = y_board & (y_board >> 8) & (y_board >> 16)
        threeDR=threeDR >>8
        intersection = threeDR & r_board
        intersection.invert()
        remaining = threeDR&intersection
        self.threes_y += remaining.count(1)
        # diagonal right check back for yellow
        threeDR = y_board & (y_board << 8) & (y_board << 16)
        threeDR=threeDR <<8
        intersection = threeDR & r_board
        intersection.invert()
        remaining = threeDR&intersection
        self.threes_y += remaining.count(1)
        self.threes_r -=1

        
    def heuristic(self):
        self.win_detect()
        self.connected_threes()
        self.connected_twos()
        self.utility = 1000000*self.score_r - 1000000*self.score_y+ 100*self.threes_r - 100*self.threes_y + 10*self.twos_r - 10*self.twos_y