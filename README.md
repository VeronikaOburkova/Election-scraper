# Election-scraper

3rd Engeto Project: Elections scraper

# Description:

This Python script is designed to scrape parlament election results data from website volby.cz (https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ) and save it to a CSV file.


# Installation of libraries:

File "requirements.txt" contains packages used in the code. Before this installation is recommended to set up virtual environment and to define Python interpreter. Python packages can be installed as follows:
pip install -r requirements.txt


# How the script works:

Choose a district for scraping from this page https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ by pressing "X" next to it and get it's URL.
Script requires two arguments:
1.	URL of  chosen district
2.	Name of .csv file

# Example:

Election results for České Budějovice:

python election_scraper_engeto.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=3&xnumnuts=3101" "cb_results.csv"

# Example of program processing:

DOWNLOADING DATA FROM GIVEN URL: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=3&xnumnuts=3101'

FILE SAVED AS: 'cb_results.csv'
CLOSING THE ELECTION SCRAPER

# Example of created csv file:

Kód obce,Název obce,Voliči v seznamu,Vydané obálky,Platné hlasy,Občanská demokratická strana,Řád národa - Vlastenecká unie,CESTA ODPOVĚDNÉ SPOLEČNOSTI,Česká str.sociálně demokrat.,Radostné Česko,STAROSTOVÉ A NEZÁVISLÍ,Komunistická str.Čech a Moravy,Strana zelených,"ROZUMNÍ-stop migraci,diktát.EU",Strana svobodných občanů,Blok proti islam.-Obran.domova,Občanská demokratická aliance,Česká pirátská strana,Referendum o Evropské unii,TOP 09,ANO 2011,Dobrá volba 2016,SPR-Republ.str.Čsl. M.Sládka,Křesť.demokr.unie-Čs.str.lid.,Česká strana národně sociální,REALISTÉ,SPORTOVCI,Dělnic.str.sociální spravedl.,Svob.a př.dem.-T.Okamura (SPD),Strana Práv Občanů
535826,Adamov,682,474,472,91,0,2,37,0,36,40,4,3,13,0,1,43,0,23,126,0,0,12,0,3,1,0,36,1
536156,Bečice,82,63,63,3,0,0,1,0,5,3,0,1,1,0,0,8,0,5,17,0,0,10,0,0,0,0,9,0
544272,Borek,1 215,923,914,123,1,3,52,0,58,62,15,5,26,0,1,93,0,65,275,1,0,47,0,14,5,0,66,2
544281,Borovany,3 299,2 093,2 081,205,5,0,159,3,87,193,26,21,26,6,5,176,4,77,645,0,1,173,3,19,5,9,223,10
535681,Borovnice,107,78,78,9,0,0,6,0,9,0,1,0,6,0,0,7,0,6,16,0,0,2,0,0,0,0,14,2
544299,Boršov nad Vltavou,1 431,993,986,133,0,1,50,0,105,50,8,4,21,0,2,93,0,68,261,0,2,72,0,22,3,1,88,2
535401,Bošilec,173,122,122,17,1,0,12,0,4,12,0,1,2,0,0,17,1,3,32,0,2,4,0,1,0,1,11,1
551490,Branišov,181,133,131,20,0,0,8,0,13,6,0,0,2,0,0,17,0,7,27,0,0,13,0,5,0,3,10,0
536059,Břehov,119,89,86,18,0,0,3,0,7,2,0,1,1,0,0,7,0,4,23,0,1,4,1,5,0,0,9,0
535541,Čakov,220,158,157,26,0,0,4,0,9,22,4,1,7,0,0,21,2,11,24,1,1,6,0,5,0,0,13,0
