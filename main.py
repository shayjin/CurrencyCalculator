from bs4 import BeautifulSoup
import requests
from tkinter import *

html_text = requests.get('https://finance.naver.com/marketindex/?tabSel=exchange#tab_section').text
soup = BeautifulSoup(html_text, 'lxml')
countries_scraped = soup.find_all('option')

countries = []
rates = []

for country in countries_scraped:
    countries.append(country.text[len(country.text)-3::])
    rates.append(country['value'])

window = Tk()
window.geometry("400x400")
window.title("Web Scrapper")

from_country = ""
to_country = ""

def convert():
    result = float(from_entry.get()) * float(rates[countries.index(fc.get())]) / float(rates[countries.index(tc.get())])
    result_entry.config(state="normal")
    result_entry.delete(0)
    result_entry.insert(0,result)
    result_entry.config(state="readonly")
    
fc = StringVar()
tc = StringVar()

fc.set("USD")
tc.set("USD")

from_label = Label(window)
to_label = Label(window)
from_entry = Entry(window)
result_entry = Entry(window)
convert_button = Button(window, text = "Convert")
from_dropdown = OptionMenu(window, fc, *countries)
to_dropdown = OptionMenu(window, tc, *countries)


from_label.config(text = "")

from_entry.config(text="Text")
from_entry.config(width="10")
from_entry.insert(0, "1")
from_entry.place(x=0,y=100)

result_entry.config(width="10")
result_entry.insert(0,"1")
result_entry.config(state="readonly")
result_entry.place(x=200,y=100)

convert_button.config(width = 10, height = 1)
convert_button.config(command = convert)
convert_button.place(x=200, y=200)

from_dropdown.place(x=0,y=50)
to_dropdown.place(x=200, y=50)

window.mainloop()