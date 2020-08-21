#!/usr/bin/python3
import csv

import wget
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from contextlib import closing
import sys
import os
import requests
import shutil
import getpass
from webdriver_manager.chrome import ChromeDriverManager
class Scraper:

    def __init__(self):

        self.base_path = os.path.join('data')  # change it as per requirement
        self.imagesData_path = os.path.join(self.base_path, 'images')  # change it as per requirement
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.main_url = 'https://www.chanel.com/us/fashion/handbags/c/1x1x1/'
        # check the internet connection and if the home page is fully loaded or not.
        try:
            self.driver.get(self.main_url)
            WebDriverWait(self.driver, 10).until(EC.title_is('Handbags - Fashion | CHANEL'))
        except TimeoutError:
            print('Loading took too much time. Please check your connection and try again.')
            sys.exit()

        # check if the directory to store data exists
        if not os.path.exists(self.base_path):
            os.mkdir(self.base_path)
        if not os.path.exists(self.imagesData_path):
            os.mkdir(self.imagesData_path)

        self.load_fetch_bags()

        self.driver.close()

    def log_error(self, e):
        """
        It is always a good idea to log errors.
        This function just prints them, but you can
        make it do anything.
        """
        print(e)

    def is_good_response(self, resp):
        """
        Returns True if the response seems to be HTML, False otherwise.
        """
        content_type = resp.headers['Content-Type'].lower()
        return (resp.status_code == 200
                and content_type is not None
                and content_type.find('html') > -1)


    def simple_get(self, url):
        """
        Attempts to get the content at `url` by making an HTTP GET request.
        If the content-type of response is some kind of HTML/XML, return the
        text content, otherwise return None.
        """
        try:
            with closing(get(url, stream=True)) as resp:
                if self.is_good_response(resp):
                    return resp.content
                else:
                    return None

        except RequestException as e:
            self.log_error('Error during requests to {0} : {1}'.format(url, str(e)))
            return None

    def load_fetch_bags(self):
        '''Load and fetch target bags'''
        bags_dict = {}
        chanel_bag = []
        bags_dict["chanel"] = {}  # to store the bags data
        bags_dict["chanel"]["bags"] = chanel_bag
        """
        response = self.simple_get(self.main_url)
        if response is not None:
            loadpage = BeautifulSoup(response, 'html.parser')
            """

        csv_file = "bags_data.csv"
        # get the no of bags
        try:
            #self.no_of_results = int(self.driver.find_element_by_xpath('//p[@class="plp-filter-bar__label is-light js-filters-total-results"]').split()[0])
            #self.no_of_results = loadpage.find("p", attrs= {"class" : "plp-filter-bar__label is-light js-filters-total-results"}).text
            text = self.driver.find_element_by_class_name('plp-filter-bar__label is-light js-filters-total-results')
            print(text)
            print('Chanel currently has {} bags online.'.format(self.no_of_results))
            bags_dict["chanel"]["numbags"] = self.no_of_results
        except Exception:
            print('Some exception occurred while trying to find the number of bags.')
            sys.exit()

        try:

            loadpage = BeautifulSoup(self.driver.page_source, 'lxml')
            all_products = loadpage.find_all('div', attrs={'class': 'txt-product'})
            #print(all_products)
            product_list = []
            for product in all_products:

                if product not in product_list:
                    product_list.append(product)
                    #print(product)
                    bag = {}
                    bag_name = product.find("span", attrs={'class' : 'heading is-7 is-block js-ellipsis txt-product__title'}).text
                    bag["name"] = bag_name
                    #print(bag_name)
                    if product.find("p", attrs={'class' : 'is-price'}) is not None:
                        bag_price = product.find("p", attrs={'class' : 'is-price'}).text.replace('*',"").strip()
                        bag["price"] = bag_price
                    else:
                        bag["price"] = "None"

                    #print(bag["price"])
                    bag_desc = product.find("span", attrs={'class' : 'js-ellipsis', "data-test" : "lblProductShrotDescription_PLP"}).text
                    bag["desc"] = bag_desc
                    #print(bag_desc)
                    #print(product.a["href"])
                    bag_url = "https://www.chanel.com" + product.a["href"]
                    bag["url"] = bag_url
                    #print(bag_url)
                    response = self.simple_get(bag_url)
                    #print(response)
                    if response is not None:
                        html = BeautifulSoup(response, 'html.parser')
                        bag_dim = html.find("span", attrs={'class' : 'js-dimension'}).text
                        #print(bag_dim)
                        bag["dimention"] = bag_dim
                        imgurl = html.find("img", attrs={"data-test":"imgProduct"})['src']
                        #print(imgurl)
                        filename = bag_name.replace(" ", "_") +".jpg"
                        #print(filename)
                        image_path = os.path.join(self.imagesData_path, filename)
                        #print(image_path)
                        # download bag
                        r = requests.get(imgurl, stream=True)
                        """
                        if r.status_code == 200:
                            with open(image_path, 'wb') as f:
                                r.raw.decode_content = True
                                shutil.copyfileobj(r.raw, f)
                                """
                        #wget.download(imgurl, out=self.imagesData_path)
                        print('Downloading image {}.'.format(filename))
                    chanel_bag.append(bag)

                    #print(chanel_bag)
            csv_columns = ["name", "price", "desc", "url", "dimention"]
            try:
                with open(csv_file, 'a') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                    writer.writeheader()
                    for data in chanel_bag:
                        writer.writerow(data)
            except IOError:
                print("I/O error")

            #print(loadpage.find("a", attrs={'class': 'button is-secondary is-loadmore js-plp-loadmore', "data-total-page" : "10"}))
            while(loadpage.find("a", attrs={'class': 'button is-secondary is-loadmore js-plp-loadmore', "data-total-page" : "10"})):

                html = "https://www.chanel.com" +loadpage.find("a", attrs={'class': 'button is-secondary is-loadmore js-plp-loadmore', "data-total-page" : "10"})["href"]
                #print(loadpage)
                response = self.simple_get(html)

                # print(all_products)

                # print(response)
                if response is not None:
                    loadpage = BeautifulSoup(response, 'html.parser')
                all_products = loadpage.find_all('div', attrs={'class': 'txt-product'})
                # print(all_products)
                product_list = []
                for product in all_products:

                    if product not in product_list:
                        product_list.append(product)
                        # print(product)
                        bag = {}
                        if product.find("span", attrs={
                            'class': 'heading is-7 is-block js-ellipsis txt-product__title'}):
                            bag_name = product.find("span", attrs={
                            'class': 'heading is-7 is-block js-ellipsis txt-product__title'}).text
                            bag["name"] = bag_name
                        else:
                            bag["name"] = "None"

                        # print(bag_name)
                        if product.find("p", attrs={'class': 'is-price'}) is not None:
                            bag_price = product.find("p", attrs={'class': 'is-price'}).text.replace('*', "").strip()
                            bag["price"] = bag_price
                        else:
                            bag["price"] = "None"

                        # print(bag["price"])
                        if product.find("span", attrs={'class': 'js-ellipsis',
                                                               "data-test": "lblProductShrotDescription_PLP"}):
                            bag_desc = product.find("span", attrs={'class': 'js-ellipsis',
                                                               "data-test": "lblProductShrotDescription_PLP"}).text
                            bag["desc"] = bag_desc
                        else:
                            bag["desc"] = "None"
                        # print(bag_desc)
                        # print(product.a["href"])
                        bag_url = "https://www.chanel.com" + product.a["href"]
                        bag["url"] = bag_url
                        # print(bag_url)
                        response = self.simple_get(bag_url)
                        # print(response)
                        if response is not None:
                            html = BeautifulSoup(response, 'html.parser')
                            if html.find("span", attrs={'class': 'js-dimension'}):
                               bag_dim = html.find("span", attrs={'class': 'js-dimension'}).text
                               # print(bag_dim)
                               bag["dimention"] = bag_dim
                            else:
                               bag["dimention"] = "None"
                            imgurl = html.find("img", attrs={"data-test": "imgProduct"})['src']
                            # print(imgurl)
                            filename = bag_name.replace(" ", "_") + ".jpg"
                            # print(filename)
                            image_path = os.path.join(self.imagesData_path, filename)
                            # print(image_path)
                            # download bag
                            r = requests.get(imgurl, stream=True)
                            """if r.status_code == 200:
                                with open(image_path, 'wb') as f:
                                    r.raw.decode_content = True
                                    shutil.copyfileobj(r.raw, f) """
                            # wget.download(imgurl, out=self.imagesData_path)
                            print('Downloading image {}.'.format(filename))
                        chanel_bag.append(bag)

            try:
                with open(csv_file, 'a') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                    writer.writeheader()
                    for data in chanel_bag:
                        writer.writerow(data)
            except IOError:
                print("I/O error")
        except Exception:
            print('Some error occurred while load all bags.')
            sys.exit()
        return bags_dict


if __name__ == "__main__":
    scraper = Scraper()