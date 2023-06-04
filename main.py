import requests
from bs4 import BeautifulSoup
import csv


url = "https://www.basketball-reference.com/players/j/jamesle01.html"
rsp = requests.get(url)
print(rsp)

content = rsp.text

soup = BeautifulSoup(content, 'html.parser')
print("ლებრონ ჯეიმსის ბოლო თამაშის სტატისტიკა:  ")
last_date = soup.find('th', class_="left").text
result = soup.find('td', class_="center", attrs={"data-stat": "game_result"}).text
current_team = soup.find('td', class_="left", attrs="team_name_abbr").text
minutes_played = soup.find('td', class_="right", attrs={"data-stat": "mp"}).text
fg_made = soup.find('td', class_="right", attrs={"data-stat": "fg"}).text
fg_attempted = soup.find('td', class_="right", attrs={"data-stat": "fga"}).text
fg_pct = soup.find('td', class_="right", attrs={"data-stat": "fg_pct"}).text
points = soup.find('td', class_="right", attrs={"data-stat": "pts"}).text
plus_minus = soup.find('td', class_="right", attrs={"data-stat": "plus_minus"}).text
print("თარიღი: ", last_date)
print("ამჟამინდელი გუნდი: ", current_team)
print("საბოლოო ანგარიში: ", result)
print("ნათამაშები წუთები: ", minutes_played)
print("გამოყენებული სროლები: ", fg_made)
print("სულ ნატყორცნი სროლები: ", fg_attempted)
print("სროლის პროცენტი: ", fg_pct)
print("ქულების რაოდენობა: ", points)
print("პლიუს-მინუსი მოედანზე ყოფნის დროს: ", plus_minus)


with open('lebron.csv', mode='w', encoding="utf-8") as file:
    fieldnames = ["teqsti", "monacemi"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"teqsti": "თარიღი", "monacemi" : last_date})
    writer.writerow({"teqsti": "ამჟამინდელი გუნდი", "monacemi": current_team})
    writer.writerow({"teqsti": "საბოლოო ანგარიში", "monacemi": result})
    writer.writerow({"teqsti": "ნათამაშები წუთები", "monacemi": minutes_played})
    writer.writerow({"teqsti": "გამოყენებული სროლები", "monacemi": fg_made})
    writer.writerow({"teqsti": "სულ ნატყორცნი სროლები", "monacemi": fg_attempted})
    writer.writerow({"teqsti": "სროლის პროცენტი", "monacemi": fg_pct})
    writer.writerow({"teqsti": "ქულების რაოდენობა", "monacemi": points})
    writer.writerow({"teqsti": "პლიუს-მინუსი მოედანზე ყოფნის დროს", "monacemi": plus_minus})









