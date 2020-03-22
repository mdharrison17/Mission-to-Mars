from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd 

def scrape_all():
    browser = Browser("chrome", executable_path="chromedriver", headless=True)

    # Visit the mars nasa news site
    vist_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(vist_url)
    # Optional delay for loading the page
    browser.is_element_present_by_css("div.collapsible.results", wait_time=1)

    #setup the html parser
    html = browser.html
    parse_soup = BeautifulSoup(html, 'html.parser')

    html = browser.html
    parse_soup = BeautifulSoup(html, 'html.parser')
    hemispheres=[]

    for x in range(4):
        browser.find_by_css('img.thumb')[x].click()
        links = browser.find_by_css('img.wide-image')
        
        browser.is_element_present_by_tag('h2', wait_time=1)
        image_title = browser.find_by_tag('h2.title').text
        link =(links['src'])

        hemisphere = {
                    'title': image_title,
                    'img_url': link
        }
        hemispheres.append(hemisphere)
        browser.back()

    #i know there is a much better way to do this just running out of time
    temp_dict1 = hemispheres[0]
    temp_dict2 = hemispheres[1]
    temp_dict3 = hemispheres[2]
    temp_dict4 = hemispheres[3]

    temp_list1 = temp_dict1.get("title"),temp_dict1.get('img_url')
    temp_list2 = temp_dict2.get("title"),temp_dict2.get('img_url')   
    temp_list3 = temp_dict3.get("title"),temp_dict3.get('img_url')
    temp_list4 = temp_dict4.get("title"),temp_dict4.get('img_url')
    

   

    data = {
        'hem1_title': temp_list1[0],
        'hem1_url':  temp_list1[1],
        'hem2_title': temp_list2[0],
        'hem2_url': temp_list2[1],
        'hem3_title': temp_list3[0],
        'hem3_url': temp_list3[1],
        'hem4_title': temp_list4[0],
        'hem4_url': temp_list4[1]
        }    

    return(data)

if __name__ == "__main__":
   # If running as script, print scraped data
    print(scrape_all())






