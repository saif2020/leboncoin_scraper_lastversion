# leboncoin_scraper_lastversion
# premier installation
1. git clone https://github.com/saif2020/leboncoin_scraper_lastversion.git
2. 'cd leboncoin_scraper_lastversion'
3. 'pip install pipenv'
4. 'pipenv install' (cette commande permet d'installer les packages)
5. 'pipenv shell'
6. 'cd leboncoinscraper2'
7. 'code .' pour ouvrir vscode 
8. changer les variables dans le fichier leboncoinspider2.py
- image_storage_path = "D:\\leboncoin_data\\images_Maison_bricolage_test\\"
- category = 'Maison'
- sousCategory = 'bricolage'
- link_scrap = ['https://www.leboncoin.fr/bricolage/offres']
9. 'scrapy crawl leboncoin2 -o nomDefichier.csv'  (exemple dans notre cas 'scrapy crawl leboncoin2 -o leboncoin_maison_bricolage_test.csv')

# apres pour chaque categorie sous categorie
1. 'cd leboncoin_scraper_lastversion'
2. 'pipenv shell'
3. 'cd leboncoinscraper2'
4. 'code .' pour ouvrir vscode 
5. changer les variables dans le fichier leboncoinspider2.py
- image_storage_path = "D:\\leboncoin_data\\images_Maison_bricolage_test\\"
- category = 'Maison'
- sousCategory = 'bricolage'
- link_scrap = ['https://www.leboncoin.fr/bricolage/offres']
6. 'scrapy crawl leboncoin2 -o nomDefichier.csv'  (exemple dans notre cas 'scrapy crawl leboncoin2 -o leboncoin_maison_bricolage_test.csv')
