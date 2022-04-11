# Mid-Point Writeup

## Scatter Plot

* Description Here

## Time Series Plot

* Description Here

## Violin Graph

![violon](screenshots/violin.png?raw=true "Title")

* A violin plot is used to visualize the distribution of the various crimes. The log10 transformed number of incidents is used for better scaling and visibility. The typical rainbow color scheme is used to distinguish the types of crimes. The viewer is able to select the type of crimes either from the violins or the legend, and see details of the crimes in the tooltips. 
* However, its interactivity is limited to the basic plotly functionalities. Only the DC data is included due to a temporary obstacle in wrangling the VA dataset. It realized only part of the functions we expected. I'll strive to make improvements later, where adding the function to select area and year from the menu is the most crucial next step. I'll also create a button for switching between the identity and log10 measure of the y-axis and make some other improvements on the tooltips. 

## Maps

* The first choropleth map is showing the overall crime number and crime rate in each of the eight wards. The color of this choropleth is dependent on the absolute value of number of crimes. Which indicate the frequency of the crime activities. Tooltips will show ward number, the exact number on number of crimes and crime rate based on population when hover mouse over

* The second map is a prototype of choropleth map that has a drop down menu to allow user to explore the data freely. Users will be able to choose the type offense and type of map to show at will. The main purpose of this graph is to show the differences between different type of crimes.

## Wordcloud

![wordcloud](screenshots/wordcloud.png?raw=true "Title")

* Description Here

## Faceted Bar Graph

![faceted bar garph](screenshots/VA_violent_crime.png?raw=true "Title")

* The facetted bar garph shown above is an overview of the Virginia metropolitan area's 2017 violent crime rate breakdown. The crime rate gives the number of crimes matching each county/city for every 1,000 people living in that area for the year 2017. It is calculated by dividing the number of different types of violent crimes by the estimated population, and multiplying the result by 1,000.

