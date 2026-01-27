class Player:
    def __init__(self, jn, pn, r, w, tn):
        self.__j_no = jn
        self.__p_name = pn
        self.__runs = r
        self.__wickets = w
        self.__t_name = tn
    
    def __str__(self):
        return f"Jersey no: {self.__j_no}\nPlayer Name: {self.__p_name}\nTotal Runs: {self.__runs}\nTotal Wickets: {self.__wickets}\nTeam Name: {self.__t_name}"

    def get_jersey_no(self):
        if int(input("Enter the pin:")) ==10:
            return self.__j_no

    def get_player_name(self):
        if int(input("Enter the pin:")) ==10:
            return self.__p_name

    def get_runs(self):
        if int(input("Enter the pin:")) ==10:
            return self.__runs

    def get_wickets(self):
        if int(input("Enter the pin:")) ==10:
            return self.__wickets

    def get_team_name(self):
        if int(input("Enter the pin:")) ==10:
            return self.__t_name

    def set_jersey_no(self, jn):
        if int(input("Enter the pin:")) ==10:
            self.__j_no = jn

    def set_player_name(self, pn):
        if int(input("Enter the pin:")) ==10:
            self.__p_name = pn

    def set_runs(self, r):
        if int(input("Enter the pin:")) ==10:
            self.__runs = r
        
    def set_wickets(self, w):
        if int(input("Enter the pin:")) ==10:
            self.__wickets = w
        
    def set_team_name(self, tn):
        if int(input("Enter the pin:")) ==10:
            self.__t_name = tn
    
    
p1 = Player(7,"MS. Dhoni",4850,500,"CSK")
# print(p1.get_player_name())
# print(p1.get_team_name())
# p1.set_team_name("Chennai Super Kings")
# print(p1.get_team_name())
print(p1)
p1.set_team_name("Chennai Super Kings")
print(p1)



