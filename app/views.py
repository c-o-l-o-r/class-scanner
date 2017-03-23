from app import app
from flask import render_template
from flask import request
from bs4 import BeautifulSoup


import requests

@app.route('/')
@app.route('/index')
def index():
    #page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
    return render_template("index.html")


@app.route('/submit', methods=['POST'])
def submit():
    error = None
    if request.method == 'POST':
        # open
        #page = requests.get("https://sa.ucla.edu/ro/Public/SOC/Results/ClassDetail?term_cd=17S&subj_area_cd=COM%20SCI&crs_catlg_no=0130%20%20%20%20&class_id=187500200&class_no=%20001%20%20")

        # closed
        #page = requests.get("https://sa.ucla.edu/ro/Public/SOC/Results/ClassDetail?term_cd=17S&subj_area_cd=HIST%20%20%20&crs_catlg_no=0096W%20%20%20&class_id=221289202&class_no=%20002%20%20")

        # waitlist
        page = requests.get("https://sa.ucla.edu/ro/Public/SOC/Results/ClassDetail?term_cd=17S&subj_area_cd=MATH%20%20%20&crs_catlg_no=0032B%20%20%20&class_id=262211220&class_no=%20003%20%20")

        soup = BeautifulSoup(page.content, 'html.parser')
        div = soup.find('div', class_="row-fluid data-row enrl_mtng_info scrollable-collapse table-width2")

        open_text = div.find_all('p')[0]

        text_str = str(open_text)

        if text_str.find("Open") != -1:
            tmp = text_str.split(" ")
            return str(tmp[1])

        if text_str.find("Closed") != -1:
            return "Sorry, the class is closed"

        if text_str.find("Waitlist") != -1:
            tmp = text_str.split(" ")
            return "waitlist over enrolled by " + str(tmp[7])

        return str(open_text)
