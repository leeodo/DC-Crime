library(tidyverse)
library(dplyr)
library(ggplot2)
library(plotly)


df <- read_csv("data/dc_num_crimes_ward_type.csv")


vis <-
  df %>%
  filter(REPORT_DAT >= "2021-01-01" & REPORT_DAT <= "2022-01-01") %>%
  ggplot() +
  aes(x = `offense-text`, y = num_crimes_ward_type, fill = `offense-text`, colour = `offense-text`) +
  geom_violin(adjust = 1L, scale = "width") +
  scale_fill_hue(direction = 1) +
  scale_color_hue(direction = 1) +
  scale_y_continuous(trans = "log10") +
  labs(
    x = "Type of Crimes", y = "Daily Number of Incidents (Log10)",
    title = "DIstributions of Daily Crimes in DC 2021", fill = "Type of Crimes", color = "Type of Crimes"
  ) +
  theme_minimal() +
  theme(plot.title = element_text(size = 17L, face = "bold", hjust = 0.5), axis.title.y = element_text(
    size = 13L,
    face = "bold", hjust = 1
  ), axis.title.x = element_text(size = 13L, face = "bold", hjust = 1))


vis <-
  ggplotly(
    p = vis,
    width = NULL,
    height = NULL,
    tooltip = "all",
    dynamicTicks = FALSE,
    layerData = 1,
    originalData = TRUE,
  )

htmlwidgets::saveWidget(as_widget(vis), "violin.html")
