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

WIDTH = 400
HEIGHT = 400
window = Tk()
window.geometry("400x400")
window.title("Live Currency Converter")

from_country = ""
to_country = ""

def convert():
    result = round((float(from_entry.get()) * float(rates[countries.index(fc.get())]) / float(rates[countries.index(tc.get())])), 2)
    result_entry.config(state="normal")
    result_entry.delete(0)
    result_entry.insert(0,result)
    result_entry.config(state="readonly")
    
fc = StringVar()
tc = StringVar()

fc.set("USD")
tc.set("USD")

# All Elements
from_label = Label(window)
to_label = Label(window)
from_entry = Entry(window)
result_entry = Entry(window)
convert_button = Button(window, text = "Convert")
from_dropdown = OptionMenu(window, fc, *countries)
to_dropdown = OptionMenu(window, tc, *countries)

# Configurations
from_label.config(text = "")

from_entry.config(text="Text")
from_entry.config(width="15")
from_entry.insert(0, "1")
from_entry.place(x=WIDTH/30,y=HEIGHT/2.8)

result_entry.config(width="15")
result_entry.insert(0,"1")
result_entry.config(state="readonly")
result_entry.place(x=WIDTH-WIDTH/2.5,y=HEIGHT/2.8)

convert_button.config(width = 10, height = 2)
convert_button.config(command = convert)
convert_button.place(x=WIDTH/2-WIDTH/6, y=HEIGHT/2)

from_dropdown.place(x=WIDTH/7,y=HEIGHT/3.5)
to_dropdown.place(x=WIDTH/1.43, y=HEIGHT/3.5)

window.mainloop()