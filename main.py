word = input("Введите непонятное слово (большими буквами!): ")

meme_dict = {
            "РОФЛ": "шутка",
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное",
            "КРИПОВЫЙ": "страшный, пугающий",
            }
            
if word in meme_dict.keys():
   print(meme_dict[word])
else:
   print("Sorry we are dont know this word:(")
