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
library(ggiraph)
library(remotes)
#library(DCmapR)

#creating linked graph based on 
#https://www.infoworld.com/article/3626911/easy-interactive-ggplot-graphs-in-r-with-ggiraph.html

violent_crime_race <- read_csv("/Volumes/GoogleDrive/My Drive/ANLY 503 Project group/data/violent_crime_race")
view(violent_crime_race)
violent_crime_race$ward <- c('Ward 1', 'Ward 2', 'Ward 3', 'Ward 4', 'Ward 5', 'Ward 6', 'Ward 7', 'Ward 8')




bar_graph_data_recent <- violent_crime_race %>%
  mutate(
    tooltip_text = paste0(toupper(ward), "\n", 
                          vcrime_rate, "\n")
  )

vcrime_byward <- ggplot(bar_graph_data_recent, 
                           aes(x = reorder(ward, vcrime_rate), 
                               y = vcrime_rate,
                               tooltip = tooltip_text, data_id = ward #<<
                           )) +
  geom_col_interactive(color = "black", fill="#CB3838", size = 0.5) +  #<<
  labs(x = "Wards ", 
       y = "Violent Crime Rate per 100,000 People", title = "Violent Crime Rate per 100,000 People in Washington, DC by Wards, 2020") +
  ggthemes::theme_tufte() +
  theme(plot.title = element_text(size = 16L, face = "bold"), axis.title.y = element_text(size = 13L, 
                                                                                          face = "bold", hjust = 0), axis.title.x = element_text(size = 13L, face = "bold", hjust = 0)) 

girafe(ggobj = vcrime_byward, width_svg = 5, height_svg = 4)


#########################
bar_graph_underage <- violent_crime_race %>%
  mutate(
    tooltip_text = paste0(toupper(ward), "\n", 
                          shareof_popunder18, "%")
  )

underagepop_byward <- ggplot(bar_graph_underage, 
                        aes(x = reorder(ward, shareof_popunder18), 
                            y = shareof_popunder18,
                            tooltip = tooltip_text, data_id = ward #<<
                        )) +
  geom_col_interactive(color = "black", fill="#CB3838", size = 0.5) +  #<<
  labs(x = "Wards ", 
       y = "Violent Crime Rate per 100,000 People", title = "Violent Crime Rate per 100,000 People in Washington, DC by Wards, 2020") +
  ggthemes::theme_tufte() +
  theme(plot.title = element_text(size = 16L, face = "bold"), axis.title.y = element_text(size = 13L, 
                                                                                          face = "bold", hjust = 0), axis.title.x = element_text(size = 13L, face = "bold", hjust = 0)) 

girafe(ggobj = underagepop_byward, width_svg = 5, height_svg = 4)



###############################

bar_graph_black <- violent_crime_race %>%
  mutate(
    tooltip_text = paste0(toupper(ward), "\n", 
                          shareof_black, "%")
  )

black_byward <- ggplot(bar_graph_underage, 
                             aes(x = reorder(ward, shareof_black), 
                                 y = shareof_black,
                                 tooltip = tooltip_text, data_id = ward #<<
                             )) +
  geom_col_interactive(color = "black", fill="#CB3838", size = 0.5) +  #<<
  labs(x = "Wards ", 
       y = "Violent Crime Rate per 100,000 People", title = "Violent Crime Rate per 100,000 People in Washington, DC by Wards, 2020") +
  ggthemes::theme_tufte() +
  theme(plot.title = element_text(size = 16L, face = "bold"), axis.title.y = element_text(size = 13L, 
                                                                                          face = "bold", hjust = 0), axis.title.x = element_text(size = 13L, face = "bold", hjust = 0)) 

girafe(ggobj = black_byward, width_svg = 5, height_svg = 4)


girafe(code = print(underagepop_byward + black_byward), 
       width_svg = 8, height_svg = 4) %>% 
  girafe_options(opts_hover(css = "fill:cyan;"))
