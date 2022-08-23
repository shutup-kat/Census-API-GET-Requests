# Kat Hernandez py script for census api request. for final project POLS3316
#
# put into readme? no.
#
# using the census API to collect data for my stats course
#       -- how to structure a B type table api call --
# url: base url + data set + "get=" + variable list + "for=" + geography
# ex: https://api.census.gov/data/2016/acs/acs1?get=NAME,B01001_001E&for=state:*

# data set is the specific data source, year ex 2016, and table ex acs/acs1
# (acs = american community survey)
# which is the name of the table where the data is stored.

# variable list is the list of data im requesting from the data set
# i have to list all variables i want to query. i must give:
# the same of the data set(NAME),
# table id(B01001_00 ; B-base table, 01001 : tb id,
# _004E : is the row the info is on), and table id suffix(E ; e
# stands for numeric rep of the estimate, M is margin of error; PE is
# percent of the total; PM is percent margin of error).

# geography is the specific geographic area, ex state:* (* is universal sel.)

# texas is 49 ; years with available data: 2019-2010

#           -- how to structure a S type(span) api call --

# base_url = "https://api.census.goc/data/"
# base_url+ year, needs to be in str form + the rest, still accessing acs data
# acs -> american census survey. give year estimate either 1 or 5 (ex, acs/acs1)
# pass variables to be requested, NAME, table id _ column id _ E = estimate cell.

# https://api.census.gov/data/2019/acs/acs1/subject?get=NAME,S1701_C01_001E&for=state:48
# gross number of people in texas
# https://api.census.gov/data/2019/acs/acs1/subject?get=NAME,S1701_C02_001E&for=state:48
# people who have poverty status, gross number in texas, just change year.

# https://api.census.gov/data/2019/acs/acs1/subject?get=NAME,S1401_C01_001E&for=state:48
# people enrolled in school, gross number.

# ----------------------------------- Start of Script --------------------------------------------------#

from bs4 import BeautifulSoup
import requests, json

def myCall(data1, dataSet, year):
    for i in range(len(data1)):
        if i == 0 : continue
        ds = []
        for j in range(len(data1[i])):
            #print(data1[i][j])
            if j == 2 : continue
            else:
                ds.append(data1[i][j])
                #print("ds", ds)
        if ( (ds != []) and (i != 0) ):
            ds.append(int(year))
            dataSet.append(ds)
            #print("data Set", dataSet)

def to_doc(filename, population, poverty, enroll):
    f = open(filename, "a")
    #f = open("myData.txt", "a")

    f.write("this is the data for population: gross number\n\n")
    for i in range(len(population)):
        for j in range(len(population[i])):
            f.write(str(population[i][j]))
            if j != 2: f.write(", ")
        f.write("\n")

    f.write("\nthis is the data for poverty rate: gross number\n\n")
    for i in range(len(poverty)):
        for j in range(len(poverty[i])):
            f.write(str(poverty[i][j]))
            if j != 2: f.write(", ")
        f.write("\n")

    f.write("\nThis is the data for enrollment rates: gross number\n\n")
    for i in range(len(enroll)):
        for j in range(len(enroll[i])):
            f.write(str(enroll[i][j]))
            if j != 2: f.write(", ")
        f.write("\n")

    f.close()
# ----------------------------------- MAIN --------------------------------------------------#
# need to break URLs into parts bc need to update year which is in the middle.

base_api = "https://api.census.gov/data/"
api_year = "2010"

poverty_api = "/acs/acs1/subject?get=NAME,S1701_C02_001E&for=state:*"
# state:48 = texas
population_api = "/acs/acs1/subject?get=NAME,S1701_C01_001E&for=state:*"
enroll_api = "/acs/acs1/subject?get=NAME,S1401_C01_001E&for=state:*"

api_call = "url"
# wanted to keep number of lists to a minimum so i just made nested lists, external list contains all
# sub-lists of specific years for poverty or enrollment, respectfully.
population = [['NAME', 'S1701_C01_001E', 2010]]
poverty = [['NAME', 'S1701_C02_001E', 2010]]
enroll = [['NAME', 'S1401_C01_001E', 2010]]

# resp = requests.get("https://api.census.gov/data/2019/acs/acs1/subject?get=NAME,S1701_C01_001E&for=us:1")
# data1 = resp.json()
# print(data1)

for i in range(2010, 2020):
    api_year = str(i)
    # population rate call
    api_call = str(base_api + api_year + population_api)
    # print(api_call)
    resp = requests.get(api_call)
    data1 = resp.json()
    # print(type(data1)) #-> class list, is nested
    myCall(data1, population, api_year)

# print("population final ", population)

for i in range(2010, 2020):
    api_year = str(i)
    # poverty rate call
    api_call = str(base_api + api_year + poverty_api)
    resp = requests.get(api_call)
    data1 = resp.json()
    # print(data1)
    # print(type(data1)) #-> class list, is nested
    myCall(data1, poverty, api_year)

# print("poverty final", poverty)

for i in range(2010, 2020):
    api_year = str(i)
    # enrollment rate call
    api_call = base_api + api_year + enroll_api
    resp = requests.get(api_call)
    data1 = resp.json()
    # print(data1)
    myCall(data1, enroll, api_year)

# print("final enroll", enroll)

to_doc("myData.txt", population, poverty, enroll)

# http://kat-hernandez.info/