from turtle import Screen
import pandas
from country_name import Country
from score  import Score
stop = ""
count = 0
country_list = []
file = pandas.read_csv('50_states.csv')
screen = Screen()
screen.bgpic('blank_states_img.gif')
screen.setup(width=800, height=650)
while stop != "stop" and count !=50:
    player = screen.textinput(f"{count}/50 States Correct", 'Please Enter State Name')
    for country in file.state:
        x = file.x[file.state == country]
        y = file.y[file.state == country]
        if player.lower() == country.lower() and player.lower() not in country_list:
            new_country = Country(country, int(x), int(y))
            country_list.append(country.lower())
            count += 1
        if player.lower().strip() == "stop":
            stop = "stop"

score = Score(count)

screen.mainloop()