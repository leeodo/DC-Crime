library(tidyverse)
library(dplyr)
library(ggplot2)
library(plotly)
library(ggwordcloud)
library(wordcloud2)
library(gridExtra)
library(cowplot)

data1 <- read_csv("data/dc_num_crimes_ward_2021.csv")

par(mfrow = c(1, 2))

# First wordcloud based on location
df <- data1
df$WARD <- sub("^", "Ward ", df$WARD)
colnames(df) <- c("freq", "word")
df <- df[, c(2, 1)]

w1 <- wordcloud2(
  data = df,
  size = 0.7,
  color = "random-dark"
)

# htmlwidgets::saveWidget(w1, "wordcloud_ward.html")


# Second wordcloud based on crime types

data2 <- read_csv("data/dc_num_crimes_type.csv")

df2 <- data2
df2 <- df2 %>% filter(REPORT_DAT >= "2021-01-01" & REPORT_DAT <= "2022-01-01")
df2 <- df2 %>%
  group_by(`offense-text`) %>%
  summarize(num = sum(num_crimes_type))


df2 <- df2 %>%
  mutate(num_log = log(num))

df2 <- df2[, -2]

w2 <- wordcloud2(
  data = df2,
  minSize = 0.5,
  size = 1,
  shape = "circle",
  color = "random-dark"
)

# htmlwidgets::saveWidget(w2, "wordcloud_crime.html")
