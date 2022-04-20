setwd(dirname(rstudioapi::getActiveDocumentContext()$path))
# lintr::lint("data_munging.R")
# Rae Zhang
# d3 visualization

library(dplyr)
library(readxl)
library(esquisse)
library(dplyr)
library(tidyr)
library(ggplot2)
library(plotly)

va_violent_crime <- read.csv("VA/virginia_DMV/va_dmv.csv") %>%
  slice(-1) %>%
  mutate(Measures = as.factor(Measures)) %>%
  mutate(Area = as.factor(Area)) %>%
  na.omit()

# esquisser(viewer = "browser")

# facet graph
va_violent_crime <- va_violent_crime %>%
  filter(!(Measures %in% "All Offense Types")) %>%
  rename(Crime_rate_per_1000 = Crime.Rate..per.1.000.) %>%
  rename(Number_of_crimes = Number.of.Crimes) %>%
  rename(Offense_rate_per_1000 = Offense.Rate..per.1.000.) %>%
  rename(Incident_rate_per_1000 = Incident.Rate..per.1.000.)
  
graph <- ggplot(data=va_violent_crime, aes(x = Measures, fill = Measures,
                                           weight = Crime_rate_per_1000)) +
 geom_bar() +
 scale_fill_brewer(palette = "RdPu", direction = -1) +
 labs(x = "Crime Type", y = "Crime Rate per 1,000",
 title = "2017 Violent Crime Rate in Virginia (DMV)",
 subtitle = "Virginia-Washington metropolitan area") +
 coord_flip() +
 theme_classic() +
 theme(plot.title = element_text(size = 16L, face = "bold", hjust = 0.5),
       plot.subtitle = element_text(size = 15L,
 face = "italic", hjust = 0.5), plot.caption = element_text(size = 14L),
 axis.title.y = element_text(size = 13L,
 face = "bold"), axis.title.x = element_text(size = 13L, face = "bold")) +
 theme(strip.text.x = element_text(size = 11L, face = "bold")) +
  theme(strip.text.y = element_text(size = 11L)) +
 facet_wrap(vars(Area))

save <- ggplotly(graph)
htmlwidgets::saveWidget(save, "VA_2017_violent_crime.html")

