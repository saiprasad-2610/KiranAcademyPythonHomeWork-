class Player:
    def __init__(self,jn,nm,r,w,tn):
        self.jersey_no = jn
        self.p_name = nm
        self.runs = r
        self.wickets = w
        self.t_name = tn
p1 = Player(18,"Virat Kholi",7500,4,"RCB")
p2 = Player(45,"Rohit Sharma",6600,15,"MI")
p3 = Player(7,"MS Dhoni",5200,0,"CSK")
p4 = Player(63,"Suryakumar Yadav",3400,0,"MI")
p5 = Player(99,"Jasprit Bumrah",60,165,"MI")

All_Players = []
All_Players.append(p1)
All_Players.append(p2)
All_Players.append(p3)
All_Players.append(p4)
All_Players.append(p5)
print(All_Players)

for p in All_Players:
    if p.runs>3000:
        print(p.p_name)



