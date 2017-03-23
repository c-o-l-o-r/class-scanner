from bs4 import BeautifulSoup
import requests

#page = requests.get("https://sa.ucla.edu/ro/Public/SOC/Results/ClassDetail?term_cd=17S&subj_area_cd=COM%20SCI&crs_catlg_no=0130%20%20%20%20&class_id=187500200&class_no=%20001%20%20")
page = requests.get("https://sa.ucla.edu/ro/Public/SOC/Results/ClassDetail?term_cd=17S&subj_area_cd=HIST%20%20%20&crs_catlg_no=0096W%20%20%20&class_id=221289202&class_no=%20002%20%20")

soup = BeautifulSoup(page.content, 'html.parser')

div = soup.find('div', class_="row-fluid data-row enrl_mtng_info scrollable-collapse table-width2")
open_text = div.find_all('p')[0]

print(open_text)
