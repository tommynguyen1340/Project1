#1: string
lakers_string = '''
NAME	        PTS	REB	AST	STL	BLK	TO
Anthony Davis	26.1	9.3	3.2	1.5	2.3	2.5
LeBron James	25.3	7.8	10.2	1.2	0.5	3.9
Kyle Kuzma	12.8	4.5	1.3	0.5	0.4	1.5
Dion Waiters	11.9	1.9	2.4	0.6	0.6	1.9
Caldwell-Pope	9.3	2.1	1.6	0.8	0.2	0.9
Avery Bradley	8.6	2.3	1.3	0.9	0.1	1
Danny Green	8	3.3	1.3	1.3	0.5	0.9
Dwight Howard	7.5	7.3	0.7	0.4	1.1	1.2
Rajon Rondo	7.1	3	5	0.8	0	1.9
JaVale McGee	6.6	5.7	0.5	0.5	1.4	0.8
Talen Horton	5.7	1.2	1	1.3	0.2	1
Alex Caruso	5.5	1.9	1.9	1.1	0.3	0.8
Markieff Morris	5.3	3.2	0.6	0.4	0.4	0.4
Quinn Cook	5.1	1.2	1.1	0.3	0	0.8
Troy Daniels	4.2	1.1	0.3	0.2	0.1	0.2
JR Smith	2.8	0.8	0.5	0.2	0	0.7
Jared Dudley	1.5	1.2	0.6	0.3	0.1	0.2
'''

#2: tuple
player1_tuple = ('Anthony Davis', 26.1, 9.3, 3.2, 1.5, 2.3, 2.5)
player2_tuple = ('LeBron James', 25.3, 7.8, 10.2, 1.2, 0.5, 3.9)
player3_tuple = ('Kyle Kuzma', 12.8, 4.5, 1.3, 0.5, 0.4, 1.5)
player4_tuple = ('Dion Waiters', 11.9, 1.9, 2.4, 0.6, 0.6, 1.9)
player5_tuple = ('Caldwell-Pope', 9.3, 2.1, 1.6, 0.8, 0.2, 0.9)
player6_tuple = ('Avery Bradley', 8.6, 2.3, 1.3, 0.9, 0.1, 1)
player7_tuple = ('Danny Green', 8, 3.3, 1.3, 1.3, 0.5, 0.9)
player8_tuple = ('Dwight Howard', 7.5, 7.3, 0.7, 0.4, 1.1, 1.2)
player9_tuple = ('Rajon Rondo', 7.1, 3, 5, 0.8, 0, 1.9)
player10_tuple = ('JaVale McGee', 6.6, 5.7, 0.5, 0.5, 1.4, 0.8)
player11_tuple = ('Talen Horton', 5.7, 1.2, 1, 1.3, 0.2, 1)
player12_tuple = ('Alex Caruso', 5.5, 1.9, 1.9, 1.1, 0.3, 0.8)
player13_tuple = ('Markieff Morris', 5.3, 3.2, 0.6, 0.4, 0.4,0.4)
player14_tuple = ('Quinn Cook', 5.1, 1.2, 1.1, 0.3, 0,0.8)
player15_tuple = ('Troy Daniels', 4.2, 1.1, 0.3, 0.2, 0.1, 0.2)
player16_tuple = ('JR Smith', 2.8, 0.8, 0.5, 0.2, 0, 0.7)
player17_tuple = ('Jared Dudley', 1.5, 1.2, 0.6, 0.3, 0.1, 0.2)

#3: custom class
class Lakers:
    """Stats of the players on Lakers roster seperated into name,
       points, rebounds, assists, steals, blocks and turnovers."""
    
    def __init__(self, name, points, rebounds, assists, steals, blocks, turnovers):
        self.name = name
        self.points = points
        self.rebounds = rebounds
        self.assists = assists
        self.steals = steals
        self.blocks = blocks
        self.turnovers = turnovers

player1 = Lakers('Anthony Davis', 26.1, 9.3, 3.2, 1.5, 2.3, 2.5)
player2 = Lakers('LeBron James', 25.3, 7.8, 10.2, 1.2, 0.5, 3.9)
player3 = Lakers('Kyle Kuzma', 12.8, 4.5, 1.3, 0.5, 0.4, 1.5)
player4 = Lakers('Dion Waiters', 11.9, 1.9, 2.4, 0.6, 0.6, 1.9)
player5 = Lakers('Caldwell-Pope', 9.3, 2.1, 1.6, 0.8, 0.2, 0.9)
player6 = Lakers('Avery Bradley', 8.6, 2.3, 1.3, 0.9, 0.1, 1)
player7 = Lakers('Danny Green', 8, 3.3, 1.3, 1.3, 0.5, 0.9)
player8 = Lakers('Dwight Howard', 7.5, 7.3, 0.7, 0.4, 1.1, 1.2)
player9 = Lakers('Rajon Rondo', 7.1, 3, 5, 0.8, 0, 1.9)
player10 = Lakers('JaVale McGee', 6.6, 5.7, 0.5, 0.5, 1.4, 0.8)
player11 = Lakers('Talen Horton', 5.7, 1.2, 1, 1.3, 0.2, 1)
player12 = Lakers('Alex Caruso', 5.5, 1.9, 1.9, 1.1, 0.3, 0.8)
player13 = Lakers('Markieff Morris', 5.3, 3.2, 0.6, 0.4, 0.4,0.4)
player14 = Lakers('Quinn Cook', 5.1, 1.2, 1.1, 0.3, 0,0.8)
player15 = Lakers('Troy Daniels', 4.2, 1.1, 0.3, 0.2, 0.1, 0.2)
player16 = Lakers('JR Smith', 2.8, 0.8, 0.5, 0.2, 0, 0.7)
player17 = Lakers('Jared Dudley', 1.5, 1.2, 0.6, 0.3, 0.1, 0.2)
        
