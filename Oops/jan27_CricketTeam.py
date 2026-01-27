from functools import reduce
class Player:
    def __init__(self, jn, pn, r, w, tn):
        self.__j_no = jn
        self.__p_name = pn
        self.__runs = r
        self.__wickets = w
        self.__t_name = tn
    
    def __str__(self):
        return f"Jersey no: {self.__j_no}\nPlayer Name: {self.__p_name}\nTotal Runs: {self.__runs}\nTotal Wickets: {self.__wickets}\nTeam Name: {self.__t_name}\n----------------------"

    def get_jersey_no(self):
            return self.__j_no

    def get_player_name(self):
            return self.__p_name

    def get_runs(self):
            return self.__runs

    def get_wickets(self):
            return self.__wickets

    def get_team_name(self):
            return self.__t_name

    def set_jersey_no(self, jn):
            self.__j_no = jn

    def set_player_name(self, pn):
            self.__p_name = pn

    def set_runs(self, r):
            self.__runs = r
        
    def set_wickets(self, w):
            self.__wickets = w
        
    def set_team_name(self, tn):
            self.__t_name = tn

p1_csk  = Player(7,  "MS Dhoni",        5082, 0,   "CSK")
p2_csk  = Player(31, "Ruturaj Gaikwad", 1797, 0,   "CSK")
p3_csk  = Player(9,  "Ravindra Jadeja", 2692, 152, "CSK")
p4_csk  = Player(90, "Deepak Chahar",   80,   72,  "CSK")
p5_csk  = Player(8,  "Moeen Ali",       1017, 33,  "CSK")
p6_csk  = Player(99, "Shivam Dube",     1100, 4,   "CSK")
p7_csk  = Player(18, "Ambati Rayudu",   4348, 0,   "CSK")
p8_csk  = Player(88, "Dwayne Bravo",    1560, 183, "CSK")
p9_csk  = Player(81, "Sam Curran",      833,  47,  "CSK")
p10_csk = Player(56, "Imran Tahir",     23,   82,  "CSK")
p11_csk = Player(70, "Shardul Thakur",  307,  67,  "CSK")

p1_mi  = Player(45, "Rohit Sharma",        6211, 15,  "MI")
p2_mi  = Player(63, "Suryakumar Yadav",    3249, 0,   "MI")
p3_mi  = Player(77, "Ishan Kishan",        2328, 0,   "MI")
p4_mi  = Player(33, "Hardik Pandya",       2309, 53,  "MI")
p5_mi  = Player(55, "Kieron Pollard",      3412, 69,  "MI")
p6_mi  = Player(93, "Jasprit Bumrah",      56,   145, "MI")
p7_mi  = Player(12, "Krunal Pandya",       1326, 76,  "MI")
p8_mi  = Player(23, "Quinton de Kock",     2907, 0,   "MI")
p9_mi  = Player(24, "Rahul Chahar",        77,   63,  "MI")
p10_mi = Player(99, "Trent Boult",          13,   92, "MI")
p11_mi = Player(11, "Lasith Malinga",        56,   170,"MI")


p1_rcb  = Player(18, "Virat Kohli",        7263, 4,   "RCB")
p2_rcb  = Player(17, "AB de Villiers",     5162, 0,   "RCB")
p3_rcb  = Player(33, "Faf du Plessis",     4133, 0,   "RCB")
p4_rcb  = Player(5,  "Glenn Maxwell",      2771, 37,  "RCB")
p5_rcb  = Player(97, "Devdutt Padikkal",   2602, 0,   "RCB")
p6_rcb  = Player(19, "Dinesh Karthik",     4516, 0,   "RCB")
p7_rcb  = Player(2,  "Harshal Patel",      230,  105, "RCB")
p8_rcb  = Player(3,  "Mohammed Siraj",     68,   93,  "RCB")
p9_rcb  = Player(8,  "Wanindu Hasaranga",  196,  130, "RCB")
p10_rcb = Player(11, "Josh Hazlewood",     31,   25,  "RCB")
p11_rcb = Player(21, "Shahbaz Ahmed",      546,  19,  "RCB")


csk_team = [p1_csk, p2_csk, p3_csk, p4_csk, p5_csk, p6_csk, p7_csk, p8_csk, p9_csk, p10_csk, p11_csk]
mi_team = [p1_mi, p2_mi, p3_mi, p4_mi, p5_mi, p6_mi, p7_mi, p8_mi, p9_mi, p10_mi, p11_mi]
rcb_team = [p1_rcb, p2_rcb, p3_rcb, p4_rcb, p5_rcb, p6_rcb, p7_rcb, p8_rcb, p9_rcb, p10_rcb, p11_rcb]

teams = [csk_team,mi_team,rcb_team]
all_players= []
for team in teams:
                for player in team: 
                        all_players.append(player)

print(f"........Welcome To IPL-2025......")
print(f">>> Get Max Runs: 1 | Get Details of runs greater than user input - 2 | To Update Runs - 3 | List Top 5 Players - 4  | List All Players with Jersey no. - 5 | Exit - 0")

while(True):
        key = input(">> ")
        if key =="1":
                print("Max run from Teams >> CSK - 1 | MI - 2 | RCB - 3 | All Teams - 4")
                particularTeam = int(input(">>"))
                if particularTeam == 1:
                        maxRuns =reduce(lambda x,y : x if x.get_runs() > y.get_runs() else y ,csk_team)
                        print(f"""Maximum Runs are >> {maxRuns.get_runs()} by "{maxRuns.get_player_name()}" From "{maxRuns.get_team_name()}" and Jersey no. "{maxRuns.get_jersey_no()}" """)

                elif particularTeam == 2:
                        maxRuns =reduce(lambda x,y : x if x.get_runs() > y.get_runs() else y ,mi_team)
                        print(f"""Maximum Runs are >> {maxRuns.get_runs()} by "{maxRuns.get_player_name()}" From "{maxRuns.get_team_name()}"  """)
                elif particularTeam == 3:
                        maxRuns =reduce(lambda x,y : x if x.get_runs() > y.get_runs() else y ,rcb_team)
                        print(f"""Maximum Runs are >> {maxRuns.get_runs()} by "{maxRuns.get_player_name()}" From "{maxRuns.get_team_name()}"  """)
                
                elif particularTeam == 4:
                        maxRuns =reduce(lambda x,y : x if x.get_runs() > y.get_runs() else y ,all_players)
                        print(f"""Maximum Runs are >> {maxRuns.get_runs()} by "{maxRuns.get_player_name()}" From "{maxRuns.get_team_name()}"  """)
                else:
                        print("Invalid Input...")
        elif key == "2":
                m = int(input("Enter the Runs Greater than? : "))
                print(f"The Runs Greater than {m} are >> ")
                greaterThan =(list(filter(lambda x : x.get_runs()>=m,all_players)))
                for i in greaterThan:
                        print(f"=> {i.get_player_name()} From {i.get_team_name()} - {i.get_runs()}")
        elif key == "3":
                new_j = int(input("Enter Jersey no. to Update the Runs: "))
                for i in all_players:
                        if i.get_jersey_no() == new_j :
                                new_run =int(input("Enter Updated Runs: "))
                                i.set_runs(new_run)
                                print("Runs Updated successfully...")   
                                break
                        elif i.get_jersey_no() != new_j:
                                print("Error, please Enter valid Jersey number...")
                                break
        elif key == "4":
                print("CSK - 1 | MI - 2 | RCB - 3 | All Teams - 4")
                t5 = int(input(">>"))
                if t5 == 1:
                        all_top5 = sorted(csk_team,key = lambda x:x.get_runs(),reverse=True)
                        for i in all_top5[:5]:
                                print(f"""=> "{i.get_player_name()}" from "{i.get_team_name()}" with "{i.get_runs()}" """)
                elif t5 == 2:
                        all_top5 = sorted(mi_team,key = lambda x:x.get_runs(),reverse=True)
                        for i in all_top5[:5]:
                                print(f"""=> "{i.get_player_name()}" from "{i.get_team_name()}" with "{i.get_runs()}" """)
                elif t5 == 3:
                        all_top5 = sorted(rcb_team,key = lambda x:x.get_runs(),reverse=True)
                        for i in all_top5[:5]:
                                print(f"""=> "{i.get_player_name()}" from "{i.get_team_name()}" with "{i.get_runs()}" """)

                elif t5 == 4:
                        all_top5 = sorted(all_players,key = lambda x:x.get_runs(),reverse=True)
                        for i in all_top5[:5]:
                                print(f"""=> "{i.get_player_name()}" from "{i.get_team_name()}" with "{i.get_runs()}" """)
                else:
                        print("Invalid input... ")
        elif key == "5":
                for i in all_players:
                        print(F"=> {i.get_player_name()} > {i.get_jersey_no()}")
        elif key =="0":
                print(".....Thank You.....")
                break