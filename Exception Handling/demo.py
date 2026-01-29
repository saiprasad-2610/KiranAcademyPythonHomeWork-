class Player:
    def __init__(self,jn,pn,r,w,tn):
        self.jersey_no=jn
        self.player_name=pn
        self.run=r 
        self.wicket=w 
        self.team_name=tn 
    def __str__(self):
        return f"{self.jersey_no} {self.player_name} {self.run} {self.wicket} {self.team_name}"  

    def get_jersey_no(self):
        return self.jersey_no 

    def set_jersey_no(self,nj):
        self.jersey_no=nj

    def get_player_name(self): 
        return self.player_name 

    def set_player_name(self,np):
        self.player_name=np 

    def get_runs(self):
        return self.run

    def set_runs(self,nr):
        self.run=nr 

    def get_wicket(self):
        return self.wicket 

    def set_wicket(self,nw):
        self.wicket=nw 

    def get_team(self):
        return self.team_name 

    def set_team(self,nt):
        self.team_name=nt                   

            
csk_p1  = Player(7,  "MS Dhoni", 5082, 0,   "CSK")
csk_p2  = Player(3,  "Suresh Raina", 5529, 0, "CSK")
csk_p3  = Player(8,  "Ravindra Jadeja", 2692, 152, "CSK")
csk_p4  = Player(90, "Murali Vijay", 2619, 0, "CSK")
csk_p5  = Player(25, "Dwayne Bravo", 1560, 183, "CSK")
csk_p6  = Player(99, "Imran Tahir", 36, 82, "CSK")
csk_p7  = Player(11, "Faf du Plessis", 2935, 0, "CSK")
csk_p8  = Player(18, "Shane Watson", 3874, 92, "CSK")
csk_p9  = Player(55, "Ambati Rayudu", 4348, 0, "CSK")
csk_p10 = Player(72, "Deepak Chahar", 80, 77, "CSK")
csk_p11 = Player(9,  "R Ashwin", 709, 180, "CSK")


rcb_p1 = Player(18, "Virat Kohli", 7263, 4, "RCB")
rcb_p2 = Player(17, "AB de Villiers", 4491, 0, "RCB")
rcb_p3 = Player(33, "Chris Gayle", 4965, 18, "RCB")
rcb_p4 = Player(7, "Faf du Plessis", 3403, 2, "RCB")
rcb_p5 = Player(96, "Glenn Maxwell", 2719, 31, "RCB")
rcb_p6 = Player(5, "Dinesh Karthik", 4516, 0, "RCB")
rcb_p7 = Player(13, "Rajat Patidar", 799, 0, "RCB")
rcb_p8 = Player(25, "Mohammed Siraj", 56, 83, "RCB")
rcb_p9 = Player(10, "Harshal Patel", 235, 135, "RCB")
rcb_p10 = Player(19, "Yuzvendra Chahal", 77, 187, "RCB")
rcb_p11 = Player(20, "Washington Sundar", 378, 35, "RCB")

mi_p1  = Player(45, "Rohit Sharma", 6211, 15, "MI")
mi_p2  = Player(63, "Suryakumar Yadav", 3249, 0, "MI")
mi_p3  = Player(77, "Ishan Kishan", 2328, 0, "MI")
mi_p4  = Player(33, "Hardik Pandya", 2309, 53, "MI")
mi_p5  = Player(93, "Jasprit Bumrah", 56, 145, "MI")
mi_p6  = Player(9,  "Kieron Pollard", 3412, 69, "MI")
mi_p7  = Player(19, "Rahul Chahar", 18, 42, "MI")
mi_p8  = Player(99, "Quinton de Kock", 2907, 0, "MI")
mi_p9  = Player(23, "Tilak Varma", 740, 0, "MI")
mi_p10 = Player(27, "Trent Boult", 58, 105, "MI")
mi_p11 = Player(12, "Krunal Pandya", 1514, 61, "MI")

csk = []
csk.extend([
    csk_p1, csk_p2, csk_p3, csk_p4, csk_p5,
    csk_p6, csk_p7, csk_p8, csk_p9, csk_p10, csk_p11
])

csk_players = []
for i in csk:
    if i.get_team() == "CSK":
        csk_players.append(i)

rcb = []
rcb.extend([
    rcb_p1, rcb_p2, rcb_p3, rcb_p4, rcb_p5,
    rcb_p6, rcb_p7, rcb_p8, rcb_p9, rcb_p10, rcb_p11
])

rcb_players = []
for i in rcb:
    if i.get_team() == "RCB":
        rcb_players.append(i)

mi_players = []
mi_players.extend([
    mi_p1, mi_p2, mi_p3, mi_p4, mi_p5,
    mi_p6, mi_p7, mi_p8, mi_p9, mi_p10, mi_p11
])


all_players=[csk_p1, csk_p2, csk_p3, csk_p4, csk_p5,
    csk_p6, csk_p7, csk_p8, csk_p9, csk_p10, csk_p11,rcb_p1, rcb_p2, rcb_p3, rcb_p4, rcb_p5,
    rcb_p6, rcb_p7, rcb_p8, rcb_p9, rcb_p10, rcb_p11,mi_p1, mi_p2, mi_p3, mi_p4, mi_p5,
    mi_p6, mi_p7, mi_p8, mi_p9, mi_p10, mi_p11]


#Write a function that accepts a list of players and prints only player details.
def print_Players_details(players):
    for i in players:
        print(
            f"Jersey No : {i.get_jersey_no()}\n"
            f"Player    : {i.get_player_name()}\n"
            f"Runs      : {i.get_runs()}\n"
            f"Wickets   : {i.get_wicket()}\n"
            f"Team      : {i.get_team()}\n"
            "------------------------------"
        )
def get_players_by_teamName(player,teamName):
    Particular_Player = []
    for i in player:
        if i.get_team().lower() == teamName.lower():
            Particular_Player.append(i)
        return print([x.__str__() for x in Particular_Player])
            


# top five players name with runs 
def top_five_players(player):
    top_players=sorted(player,key=lambda x: x.get_runs(),reverse=True)[:5]
    for i in top_players:
      print(f"{i.get_player_name()}  {i.get_runs()}")
      
# Write a function to return average runs of the team.

def average_runs(player):
    total=0
    for i in player:
        total+=i.get_runs() 
    avarage_score=total//len(player)
    return avarage_score 
# r1=average_runs(csk_player) 
# print(f"Avarage Score {r1}")  

# highest wicket takers 
def highest_wicket_taker(players):
    top = max(players, key=lambda x: x.get_wicket())
    print("Highest Wicket Taker:")
    print(top)

# update jersey_no    
    
def update_jersey_number(players, player_name, new_jersey):
    player_name=player_name.strip()
    for p in players:
        if p.get_player_name().lower() == player_name.lower():
            p.set_jersey_no(new_jersey)
            print(f"Jersey number updated for {player_name}")
            return
    print("Player not found!")
    
def change_team(players,jn,pn,nt):
    
    for i in players:
        if jn==i.get_jersey_no() and pn.lower()==i.get_player_name().lower():
            i.set_team(nt)
            print("Team Changed Succesfully")  
        
        


while True:
    print("\n--- CSK Cricket Team Management ---")
    print("1. Show all players details")
    print("2. Show top run scorer")
    print("3. show average team runs")
    print("4. Show highest wicket taker")
    print("5. update jersey number")
    print("6. change team")
    print("7. Exit") 
   
    
    try:
     choice=int(input("Enter Your Choice: "))   
     if choice==1:
         print("1. show all players details")
         print("2. csk_players")
         print("3 RCb_Players")
         print("4 MI_players")
         
         team_name=int(input("Enter Team Name: "))
        
         if team_name==1:
            print_Players_details(all_players)
         elif team_name==2:
             get_players_by_teamName(all_players,"CSK")
         elif team_name==3:
               print_Players_details(rcb_players)
         elif team_name==4:
             print_Players_details(mi_players)
               
             
            
     elif choice==2:
        top_five_players(all_players)
     elif choice==3:
            r1=average_runs(all_players) 
            print(f"Average team Runs {r1}")
     elif choice==4:
        highest_wicket_taker(all_players) 
     elif choice==5:
        name = input("Enter player name: ")
        jersey = int(input("Enter new jersey number: "))
        update_jersey_number(all_players, name, jersey)
     elif choice==6:
         jn=int(input("Enter Jersey No: "))
         pn=input("Enter Players Name: ")
         team_name=input("Enter Team Name: ")   
         change_team(all_players,jn,pn,team_name)
                   
     elif choice==7:
        print("Thank you ! Exiting Program")  
        break
     else:
        print("Invalid Choice Try again")   
    
    except ValueError as e:
        print("Value error")
        print(e)