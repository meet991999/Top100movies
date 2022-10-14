from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
content = response.text


soup = BeautifulSoup(content,"html.parser", )
text1 = soup.find_all(name="h3", class_="title")

movie_list = [movie.getText() for movie in text1]
new_movie = movie_list[::-1]
print(new_movie)


with open("movie_name.txt", mode="w+",encoding="UTF-8") as file:
    for movie in new_movie:
        file.write(f"{movie}\n")