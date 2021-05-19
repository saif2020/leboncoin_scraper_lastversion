import scrapy
import numpy as np
from time import sleep
from  random import randint
from urllib.request import urlretrieve

##### set the variable here
image_storage_path = "D:\\leboncoin_data\\images_Maison_jardinage_test\\"
category = 'Maison'
sousCategory = 'jardinage'
link_scrap = ['https://www.leboncoin.fr/jardinage/offres']

class LeboncoinSpider(scrapy.Spider):
    name = 'leboncoin2'
    start_urls = link_scrap
    custom_settings = {
        'AUTOTHROTTLE_ENABLED' : True,
        'AUTOTHROTTLE_START_DELAY' : 10,
        'AUTOTHROTTLE_MAX_DELAY' : 60,
    }
    

    def parse(self, response):
        for link in response.css('a.AdCard__AdCardLink-sc-1h74x40-0.cHZrAn::attr(href)').getall():
            link = response.urljoin(link)
            print(link)
            yield response.follow(link, callback = self.parse_product)

        next_page = response.css('a._3-yvP::attr("href")').getall()[-1]
        print(next_page)
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield response.follow(next_page, callback=self.parse) 
        else:
            print("next page none")         
              
    def parse_product(self, response):
        try :
            key_list = response.css('p._2k43C._1pHkp.Dqdzf.cJtdT._3j0OU::text').getall()
            value_list =  response.css('span._3eNLO._38n__._137P-.P4PEa._35DXM::text').getall()
        except:
            key_list = np.nan
            value_list = np.nan

        try: 
            dict_caracteristique_optional = dict(zip(key_list, value_list))
        except:
            dict_caracteristique_optional = np.nan
        try:
            titre = response.css('h1.-HQxY._38n__._2QVPN._3zIi4._2-a8M._1JYGK._35DXM::text').get()
        except:
            titre = np.nan    
        try:
            description = response.css('div._2BMZF._137P-.P4PEa._3j0OU p::text').get()
        except:
            description = np.nan     
        try:
            etat = dict_caracteristique_optional['État']
        except:
            etat = np.nan   
        try:
            prix = response.css('span._3gP8T._25LNb._35DXM::text').get()
        except:
            prix = np.nan      
        try:
            marque = dict_caracteristique_optional['Marque']
        except:
            marque = np.nan    
        try:
            modele = dict_caracteristique_optional['Modèle']
        except:
            modele = np.nan  
        try:
            version = dict_caracteristique_optional['Année-modèle']
        except:
            version = np.nan  
        try:
            couleur = dict_caracteristique_optional['Couleur']
        except:
            couleur = np.nan    
        try:
            raw_image_urls = response.css('div.styles_Carousel__FJED0 img::attr(src)').getall()
            clean_image_urls = []
            for img_url in raw_image_urls:
                image_url_value = response.urljoin((img_url))
                image_name = image_url_value.split('/')[-1].split('?')[0]
                urlretrieve(image_url_value, filename = image_storage_path + image_name )
                clean_image_urls.append(image_name)
        except:
            clean_image_urls = np.nan     
        
        
        yield{
            'titre':titre,
            'description':description,
            'etat':etat,
            'prix':prix,
            'marque':marque,
            'modele':modele,
            'version':version,
            'couleur':couleur,
            'images':clean_image_urls,
            'category':category,
            'sousCategory':sousCategory,
            'dict_caracteristique_optional':dict_caracteristique_optional,
        }
        
        sleep(randint(5,10)) # 5,10#0,7
        
           

        