import codecs
import pathlib
import requests

from bs4 import BeautifulSoup
from check_swear import SwearingCheck
from googlesearch import search


sch = SwearingCheck()
result_file = codecs.open('result.txt', 'w', 'utf-8') # Will contain the results

path = pathlib.Path("./test_dir/")
for song in path.iterdir():
    song_name = song.name
    for link in search(song_name + ' текст гениус', lang="ru", num=1, stop=1):
        res = requests.get(link)
        bs = BeautifulSoup(res.text, 'html.parser')
        song_text = bs.find(attrs={"data-lyrics-container": "true"}).text
        # data-lyrics-container is a container that stores song text at genius.com
        if sch.predict(song_text) == [1]: # If ml finds swears
            result_file.write(song_name + ' - ЕСТЬ маты\n')
        else:
            result_file.write(song_name + ' - матов НЕТ\n')
