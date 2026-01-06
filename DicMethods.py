movies_2025 = {}
missionImpossible_Cast = ["Tom Cruise", "Hayley Atwell","Ving Rhames","Simon Pegg", "Henry Czerny","Angela Bassett"] #Mission: Impossible
mirai_cast = ["Teja Sajja","Manchu Manoj","Jagapathi Babu","Jayaram","Shriya Saran"] 
raid2_cast = [ "Ajay Devgn","Riteish Deshmukh","Vaani Kapoor"] 
war2_cast = [ "Hrithik Roshan","N. T. Rama Rao Jr.","Kiara Advani"] 
theRajaSaab_cast = [ "Prabhas","Nidhhi Agerwal","Sanjay Dutt"]

movies_2025["MissionImpossible"] = missionImpossible_Cast
movies_2025["Mirai"] = mirai_cast   
movies_2025["Raiders of the Lost Ark"] = raid2_cast
movies_2025["War 2"] = war2_cast
movies_2025["The Raja Saab"] = theRajaSaab_cast
for name in movies_2025.keys():
    print("Movie:",name, ":","Total Acotors and actresses are:", len(movies_2025[name]))   
count = 0
print("-------Display the movies which have Prabhas-----")
for m in movies_2025.keys():
    if "Prabhas" in movies_2025[m]:
        count +=1
        print("Prabhas acted in the movie:",m,"in ",count,"movies")
        