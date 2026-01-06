
movies2025 = {}
movies2024 = {}
movies2023 = {}

#cast list of 2025 movies
rajaSaab_cast25 = ["Prabhas", "Sanjay Dutt","Nidhhi Agerwal", "Malavika Mohanan"]  #The Raja Saab
mirai_cast25 = ["Teja Sajja", "Manchu Manoj", "Jagapathi Babu", "Jayaram", "Shriya Saran"]  #Mirai
gameChanger_cast25 = ["Ram Charan", "Kiara Advani", "Sathyaraj", "Rao Ramesh"]  #Game Changer
OG_cast25 = ["Pawan Kalyan", "Priyanka Arul Mohan"]  #OG

#cast list of 2024 movies
kalki_cast24 = ["Prabhas", "Amitabh Bachchan", "Kamal Haasan", "Deepika Padukone", "Disha Patani"]  #Kalki 2898 AD
devara_cast24 = ["N. T. Rama Rao Jr.", "Saif Ali Khan", "Janhvi Kapoor"]  #Devara: Part 1
gunturKaaram_cast24 = ["Mahesh Babu", "Sreeleela", "Meenakshi Chaudhary"]  #Guntur Kaaram
hanuman_cast24 = ["Teja Sajja", "Amritha Aiyer"]

#cast list of 2023 movies
salaar_cast23 = ["Prabhas", "Prithviraj Sukumaran", "Shruti Haasan"]  #Salaar: Part 1 – Ceasefire
rrr_cast23 = ["N. T. Rama Rao Jr.", "Ram Charan", "Alia Bhatt", "Olivia Morris"]  #RRR
dasara_cast23 = ["Nani", "Keerthy Suresh"]  #Dasara
virupaksha_cast23 = ["Sai Dharam Tej", "Samyuktha Menon"]  #Virupaksha

#adding list of cast in movies
movies2025["The Raja Saab"] = rajaSaab_cast25
movies2025["Mirai"] = mirai_cast25
movies2025["Game Changer"] = gameChanger_cast25
movies2025["OG"] = OG_cast25
movies2024["Kalki2898 "] = kalki_cast24
movies2024["Devara"] = devara_cast24
movies2024["Guntur Kaaram"] = gunturKaaram_cast24
movies2024["Hanuman"] = hanuman_cast24
movies2023["Salaar"] = salaar_cast23
movies2023["RRR"] = rrr_cast23
movies2023["Dasara"] = dasara_cast23
movies2023["Virupaksha"] = virupaksha_cast23


allMovies = {2025: movies2025, 2024: movies2024, 2023: movies2023}
count = 0
print("Actors/Actresses :>> Prabhas, Sanjay Dutt, Mahesh Babu, Sreeleela")
UserMovie = input("Enter the Ator/Actress(From Above list) Name to search the movies: ")
for year in allMovies.keys():
    movies = allMovies[year]
    for movie in movies.keys():
        if UserMovie in movies[movie]:
            count += 1
            print("The movie:", movie, "in the year:", year)
    
print(UserMovie,"Acted in",count,"movies...")

