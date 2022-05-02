#load packages 
library(tidyverse)
library(dplyr)
library(esquisse)
library(plotly)
library(chron)
library(snakecase)
library(processx)
library(dash)
library(dashCoreComponents)
library(dashHtmlComponents)
library(gganimate) #for animating your plot
library(scales)
library(animation)

dc_demograph <- read.csv("/Volumes/GoogleDrive/My Drive/project-spring-2022-projectgroup33/Data/Demographic Characteristics of DC Wards.csv")
names(dc_demograph) <- to_snake_case(names(dc_demograph))
str(dc_demograph)

race <- c('ward',                                                                                                                                             
'citizen_voting_age_population_citizen_18_and_over_population',                                                                                     
'citizen_voting_age_population_citizen_18_and_over_population_female',                                                                             
'citizen_voting_age_population_citizen_18_and_over_population_male',                                                                                 
'hispanic_or_latino_and_race_total_population',                                                                                                    
'hispanic_or_latino_and_race_total_population_hispanic_or_latino_of_any_race',                                                                      
'hispanic_or_latino_and_race_total_population_not_hispanic_or_latino',                                                                             
'hispanic_or_latino_and_race_total_population_not_hispanic_or_latino_american_indian_and_alaska_native_alone',                     
'hispanic_or_latino_and_race_total_population_not_hispanic_or_latino_asian_alone',                                                                 
'hispanic_or_latino_and_race_total_population_not_hispanic_or_latino_black_or_african_american_alone',                                              
'hispanic_or_latino_and_race_total_population_not_hispanic_or_latino_native_hawaiian_and_other_pacific_islander_alone',                           
'hispanic_or_latino_and_race_total_population_not_hispanic_or_latino_some_other_race_alone',                                      
'hispanic_or_latino_and_race_total_population_not_hispanic_or_latino_two_or_more_races',                                                         
'hispanic_or_latino_and_race_total_population_not_hispanic_or_latino_two_or_more_races_two_races_excluding_some_other_race_and_three_or_more_races',
'hispanic_or_latino_and_race_total_population_not_hispanic_or_latino_two_or_more_races_two_races_including_some_other_race',                  
'hispanic_or_latino_and_race_total_population_not_hispanic_or_latino_white_alone')                                                                
                                                                                                                

race_df <- dc_demograph[race]


race_df <- race_df %>% rename("total_population"="hispanic_or_latino_and_race_total_population", 
                              "hispanic"="hispanic_or_latino_and_race_total_population_hispanic_or_latino_of_any_race", 
                              "non_hispanic"="hispanic_or_latino_and_race_total_population_not_hispanic_or_latino", 
                              "native_american"="hispanic_or_latino_and_race_total_population_not_hispanic_or_latino_american_indian_and_alaska_native_alone", 
                              "asian"="hispanic_or_latino_and_race_total_population_not_hispanic_or_latino_asian_alone", 
                              "black"="hispanic_or_latino_and_race_total_population_not_hispanic_or_latino_black_or_african_american_alone", 
                              "nhpi"="hispanic_or_latino_and_race_total_population_not_hispanic_or_latino_native_hawaiian_and_other_pacific_islander_alone", 
                              "white"="hispanic_or_latino_and_race_total_population_not_hispanic_or_latino_white_alone", 
                              )
race_df <- race_df %>% rename("pop_18+"="citizen_voting_age_population_citizen_18_and_over_population", 
                              "femalepop_18+"="citizen_voting_age_population_citizen_18_and_over_population_female", 
                              "malepop_18+"= "citizen_voting_age_population_citizen_18_and_over_population_male")
View(race_df)

#combined racial catagories 
race_df$aapi <- race_df$asian + race_df$nhpi #create asian and pacifice Islander coloumn 
race_df$other <-race_df$hispanic_or_latino_and_race_total_population_not_hispanic_or_latino_some_other_race_alone + 
  race_df$hispanic_or_latino_and_race_total_population_not_hispanic_or_latino_two_or_more_races +
  race_df$hispanic_or_latino_and_race_total_population_not_hispanic_or_latino_two_or_more_races_two_races_excluding_some_other_race_and_three_or_more_races +
  race_df$hispanic_or_latino_and_race_total_population_not_hispanic_or_latino_two_or_more_races_two_races_including_some_other_race

#drop variables 
race_df$nhpi <- NULL
race_df$asian <- NULL
race_df$hispanic_or_latino_and_race_total_population_not_hispanic_or_latino_some_other_race_alone <- NULL
race_df$hispanic_or_latino_and_race_total_population_not_hispanic_or_latino_two_or_more_races <- NULL
race_df$hispanic_or_latino_and_race_total_population_not_hispanic_or_latino_two_or_more_races_two_races_excluding_some_other_race_and_three_or_more_races <- NULL
race_df$hispanic_or_latino_and_race_total_population_not_hispanic_or_latino_two_or_more_races_two_races_including_some_other_race <- NULL


#caculate distribution by race and gender 
race_df$shareof_black <- race_df$black/race_df$total_population
race_df$shareof_white <- race_df$white/race_df$total_population
race_df$shareof_hispanic <- race_df$hispanic/race_df$total_population
race_df$shareof_aapi <- race_df$aapi/race_df$total_population
race_df$shareof_other <- race_df$other/race_df$total_population