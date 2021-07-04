import requests
from bs4 import BeautifulSoup, element
import re
import os
import sys

animeName = input("Enter a Anime: ")
lowercaseAnimeName = animeName.lower()

urlToFiller="https://www.animefillerlist.com/shows/"

stringReplacedSpace =lowercaseAnimeName.replace(" ", "-")

URL =urlToFiller+stringReplacedSpace
print(URL)

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

result = soup.findAll("div", {"class": "filler"})
letters_only = re.sub("[^\d-]",  # Search for all non-letters

                          " ",          # Replace all non-letters with spaces
                          str(result))
print(letters_only)



temp0=letters_only.replace(" ", '\n')
text_file = open("Output.txt", "w")
text_file.write(temp0)
text_file.close()

os.system("sed -i \'/^$/d\' Output.txt")


data = [10,20,20,20,10,30,40,50]

def remove_dupli(duplist):
    nodupli=[]
    
    for element in duplist:
        if element not in nodupli:
            nodupli.append(element)
    return nodupli

def string_match(list1, char):
       for i in list1:
           if i.count(char) > 0:
               print(i)

with open('Output.txt') as f:
        lines = f.readlines()
        count= len(open('Output.txt').readlines())
        countAsStr=str(count)
        print("There are: "+countAsStr+" lines")

        withoutDuplicates =remove_dupli(lines)
        print(withoutDuplicates)

        count= len(remove_dupli(lines))
        withoutDuplicatesStr= str(withoutDuplicates)
        countAsStr=str(count)
        print("There would be : "+countAsStr+" lines after removing the duplicates")

        #string_match(withoutDuplicatesStr,"-")

        file2 = open("file2.txt","w")
        always_print = False
        for line in lines:
            if always_print or "-" in line:
                print(line)
                file2.write(line)
                always_print = True

        #tempsearch=withoutDuplicatesStr.find("-")
        #if "-" in withoutDuplicatesStr:
        #    print("found ")




        with open('readme.txt', 'w') as f:
            f.write(withoutDuplicatesStr)
            f.close()
        f.close()



