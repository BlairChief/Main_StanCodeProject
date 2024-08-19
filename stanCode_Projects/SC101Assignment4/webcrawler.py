"""
File: webcrawler.py
Name: Blair
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10900879
Female Number: 7946050
---------------------------
2000s
Male Number: 12977993
Female Number: 9209211
---------------------------
1990s
Male Number: 14146310
Female Number: 10644506
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)
    # ----- Write your code below this line ----- #
        tags = soup.find_all('table', {'class': 't-stripe'})
        for tag in tags:
            target = tag.tbody.text
            tokens = target.split()
            # get rid of the ending notes
            last = len(tokens)-22
            tokens = tokens[:last]
            # extract the numbers
            list_b = []
            total_b = 0
            list_g = []
            total_g = 0
            for i in range(2, len(tokens) - 2, 5):
                list_b.append(tokens[i])
            # make the numbers countable_plain way
            list_b = list(map(lambda num: num.split(','), list_b))
            list_b = list(map(lambda num: ''.join(num), list_b))
            list_b = list(map(lambda num: int(num), list_b))
            for num in list_b:
                total_b += num
            for j in range(4, len(tokens), 5):
                list_g.append(tokens[j])
            # make the numbers countable_compressing way
            list_g = list(map(lambda num: int(''.join(num.split(','))), list_g))
            for num in list_g:
                total_g += num
            print('Male Number: '+str(total_b))
            print('Female Number: ' + str(total_g))


if __name__ == '__main__':
    main()
