# Census-API-GET-Requests
I used python and beautiful soup library to query the American Survey Census database through and open public api. 
I explain the url request format and then I import the data into csv files that are examined using r. 
In rStudio I created various r functions to plot and visualize my data through linear regression trends, etc. 


Kat Hernandez
POLS 3316; Professor Hanna


Final Report Over Statistical Relevance Between Education Enrollment Rates and Poverty Rates in the United States of America
-------------------------------------------------------------------------------------------------------------------------------
** see attached files, main.py, project.rmd, and csv files of data.


First paragraph: Introduction 
Is there a correlation between poverty rates and enrollment rates in the US? How are they related? For a bit of background, I worked as a Chinese teacher and my roommate is completing her degree to become a teacher. We have both come to understand that a child’s ability to succeed does directly correlate with how much support they have(for the sake of this experiment we will focus on financial support). Finding results to support or deny this observation would be the next step in understanding the problem. 


So, I asked this:
Second paragraph: The dataset Describe the dataset.
What are the population rates in America? Approximately: 318,564,128 people nationwide. Margin of error: +/- 12,307
What are the enrollment rates in America? Approximately: 80,497,960 people nationwide, which includes children above the age of 3, to adults above the age of 65, also includes primary education, elementary through high school, and higher education. Margin of error: +/- 85,230
What are the poverty rates in America? Approximately: 40,910,326 people below the poverty line. Margin of error: +/- 12,307


All information was queried from the American Survey Census Data Base using their API. I used python to form a GET request, and I formatted the URL as follows:


https://api.census.gov/data/2019/acs/acs1/subject?get=NAME,S1701_C01_001E&for=state:*
Base url + year + rout to table + GET: information I want + for: state:*


I needed to isolate the year portion since I would be asking for available years 2010-2019 through a for loop.
In the GET section I request the NAME: which is the name of the state or record, and then I give table ID: S1701, followed by the column:_C01, and cell number:_001E, I want the information from.
The FOR specifics which states I want, they are assigned numbers(for ex. Texas is 48), but I don't want to pass the request for all states that would slow down my script’s performance, so instead I requested all states by using the wildcard character(*). The wild card acts as a net for all available items in that category.


I them cleaned my data by parsing my JSON(javascript object notation) package through my user defined function: 
myCall(data1, population, api_year)
I pass the function the JSON package: data1; a list matrix: population; and the year as a string so that it can be associated with the correct data.


After myCall executs, I am left with a table with records for each state containing: state name, number, year columns. 


To get all of my information into a useable format, I then transcribe the data into a txt file with another user defined function named: 
to_doc("myData.txt", population, poverty, enroll)
Takes in the parameters: file to write to, population information, poverty information, and enrollment information. In to_doc, I separate each block by category, such as Poverty rates for years 2010-2019. This txt format is perfect for me because I then converted these preformatted files to a csv file for my uses in rStudio. 
I had to keep in mind that these numbers are from surveys and can be a little bit unreliable, but it is the most widely sourced database of information I could get my hands on that was backed by a verified source.


Third paragraph: The variables
My variables are Poverty rates and Enrollment rates, as factors I have time, in years, and the population. 
Poverty: 
* Mean: 904,380.2
* Median: 618,493.5
* Standard Deviation: 1,063,883
Enrollment: 
* Mean: 1,592,532
* Median: 1,025,499
* Standard Deviation: 1,861,466
I will compare Poverty rates and Enrollment rates by tracking them yearly. So, I’ll have two graphs, Poverty rate graph and Enrollment rate graph, with years as x factor. 


Fourth paragraph: The relationship between variables + Fifth paragraph: Regression results 
It is important to note that a lot of the people who are considered “under the poverty line” are infact students. So increase in enrollment rates and poverty would affect each other. This becomes evident when I perform a t-test comparing Poverty rates to Enrollment rates, garnering a p-value of 4.996e-13, which is less than 0.5 thus there is a statistical significance. Furthermore, the R squared value is 95.18%, meaning that ~95% of change in y(poverty) can be explained by x(enrollment). 
The significance level is statistically relevant between Poverty + Years; Enrollment + Years; Population + Years; Poverty + Enrollment.


Conclusion: Regression results
What I found was interesting because I initially thought poverty was contributing to declining enrollment rates when it was actually the opposite. Enrollment rates are responsible for the increase in Poverty rates. More and more Americans care about going back to school to get higher paying jobs but unfortunately the jobs aren’t paying enough to cover the massive amounts of debut students are going into. As education rates raise, so will poverty status, which seems odd. The goal of getting an education is to be able to get higher paying jobs and to lift oneself out of poverty. On the contrary, enrolling into higher education institutions actually increases the likelihood that the student will fall below the poverty line. Due to predatory loan practices, people are defaulting on their loans because they simply can’t make enough to pay back what they thought was an investment.


Plots and tables: in attached R file.


Sources:
https://www.census.gov/content/dam/Census/library/publications/2020/acs/acs_api_handbook_2020_ch02.pdf
https://www.census.gov/data/developers/data-sets.html
https://www.census.gov/programs-surveys/gov-finances/about.html
https://www.census.gov/data/developers/data-sets/annual-public-sector-stats.html
https://data.census.gov/cedsci/table?q=B17&d=ACS%201-Year%20Estimates%20Detailed%20Tables&tid=ACSDT1Y2019.B17020


API request: 
https://www.census.gov/data/developers/guidance/api-user-guide/help.html
https://api.census.gov/data/timeseries/govs/variables.html
https://api.census.gov/data.html


Accounting for inflation using CPI: https://www.census.gov/content/dam/Census/library/publications/2018/acs/acs_general_handbook_2018_ch10.pdf
