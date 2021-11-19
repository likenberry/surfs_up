# Surfs Up

## Overview of Analysis

The purpose of this analysis is to look at weather data in Hawaii over the course of several years in order to better understand temperature and weather trends. The data for this analysis was stored in a sqlite database quering that database using pandas in jupyter notebbok. The data was collected from nine different weather stations on the island of Oahu over several years.

## Results

Before any analysis was done on the hawaii database, some exploration of the data showed that there were two tables in the database, one containing all weather information and the other containing station information.

- To better understand what the weather is like in the month of June on Oahu, data was pulled from the measurement table by grabbing the date column and the tob column (temperature obserbation) and filtering for the month of June with the below formula: june_temps = session.query(Measurement.date, Measurement.tobs).filter(extract("month", Measurement.date)== 6).all(). This formula grabbed all of the temperature readings for the month of June in the form of a list and that list was converted into a DataFrame. 
![June Temperature DataFrame](https://github.com/likenberry/surfs_up/blob/main/Resources/June_temps.png) 
  - Finally, basic descriptive statistics were run on the june_df. 
  ![June Temperature Statistics](https://github.com/likenberry/surfs_up/blob/main/Resources/June_temps_stats.png) 
  These summary statistics show that the maximum temperature for June is 83 degrees Fahrenheit and the minimum temperature is 64 degrees.   The average temperature for June is around 75 degrees. The summary statistics also shows the total count of temperatures for June at     1700.
- The temperatures for the month of December were also analyzed using a very similar formula to the one that was used to get the temperature information about June: dec_temps = session.query(Measurement.date, Measurement.tobs).filter(extract("month", Measurement.date)==12).all(). The list of December temperatures were converted into a DataFrame. 
![December Temperature DataFrame](https://github.com/likenberry/surfs_up/blob/main/Resources/Dec_temps.png) 
  - The same descriptive statistics were run on the dec_df to get a better idea about the temperature ranges. 
  ![December Tempearture Statistics](https://github.com/likenberry/surfs_up/blob/main/Resources/Dec_temps_stats.png). 
  The total number of temperature counts for December was 1517. The maximum temperature for December is 83 degrees Fahrenheit and the       minimum temperature is 56 degrees with an average temperature of a little over 71 degrees.
- Following the analysis of the temperatures in the months of December and June showed that while the two months are six months apart, there is very little difference in the overall temperatures between the two months. The temperature information was collected between the years of 2010 and 2016 from nine stations. There are almost 200 less observations for the month of December than for the month of June. This is less than a 10% difference meaning that it probably won't greatly impact the results of the analysis. There is only a two degree different between the June max temp and the December max temp which is very slight. The difference between the min temperature for June is 64 and the min temp for Dec is 56 which is a difference of 8 degrees. There is very little difference between the average temperatures for the two months. Overall it appears that the difference in temperatures between December and June are minimal and that there is only a slight variation showing good consistency in temperature over this period of time.

## Summary

The above analysis was simply on the temperature variation between June and December but another factor that can greatly impact weather in Hawaii is precipitation.

- Therefore analysis of precipitation for the month of June by using this formula: june_precip = session.query(Measurement.date, Measurement.prcp).filter(extract("month", Measurement.date)==6).all(). The list of precipitation for June was converted into a DataFrame just as before. 
![June Precipitation DataFrame](https://github.com/likenberry/surfs_up/blob/main/Resources/June_precip.png) 
  - Finally the descriptive statistics were calculated. 
  ![June Precipitation Statistics](https://github.com/likenberry/surfs_up/blob/main/Resources/June_precip_stats.png) 
  These stats show that the maximum precipitation was 4.43 inches and the minimum precipitation was zero inches. The average                precipitation was around 0.135 inches. The total number of counts was 1574.
- After the precipitation data was collected for June, the same analysis was performed for the month of December using an adjusted formula from above. The list of precipitation was converted to a DataFrame. 
![December Precipitation DataFrame](https://github.com/likenberry/surfs_up/blob/main/Resources/Dec_precip.png) 
  - The same descriptive statistics were calculated. 
  ![December Precipitation Statistics](https://github.com/likenberry/surfs_up/blob/main/Resources/Dec_precip_stats.png) 
  The statistics showed that there were 1405 counts for precipitation in December. The max precipitation for December was 6.42 inches and   the min precipitation for December was zero. The average was about 0.217 inches.
- Looking at the descriptive statistics of precipitation from the months of June and December, there are again less counts for December but it is still less than a 10% difference. There are very slight differences in precipitation between June and December and when that is considered with the temperature analysis from above, December is slightly cooler and wetter than June but overall there is very mild weather in Oahu with very little variation.

## Resources

- Data Source: hawaii.sqlite
- Software: Visual Studio Code 1.62.1, Jupyter Notebook
