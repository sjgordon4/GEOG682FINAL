## GEOG682-FINAL
## Comparing  Gun Crimes Committed versus Detected by 'ShotSpotter' per D.C. Ward
## Sela Gordon
## 08/04/19

**Introduction**

This crime mapping analysis serves to help the DC Metropolitan Police Department determine which new areas the expanded gunshot detection should cover. In analyzing gun crimes reported  with gun shots audibly detected by ShotSpotter sensors , we can see which wards would benefit the most from a gunshot detection network. 

**Analysis**

The data used in this analysis is from the District of Columbia’s open data portal (https://opendata.dc.gov/). The crime data has locations and attributes of the incidents reported by the police. A few examples of these attributes include the method of the incident and the time of day the incidents occurred. For further information, see the link below. The ward dataset are polygons that show the boundaries of the DC 2012 election wards with attribute information from the census as well as the name of the ward’s representative. In this study, ‘POP_2010’ was used to calculate the number of gun crimes committed per 10,000 people. Finally, the ShotSpotter data includes the point locations of possible gunshots detected by sound sensors. This data may include errors such as gun shots that occurred in a neighboring ward but could be heard by sensors in one of the wards in this study.

![https://opendata.dc.gov/datasets/crime-incidents-in-2017]Crime in 2017: 
DC Wards: https://opendata.dc.gov/datasets/ward-from-2012
ShotSpotter Gun Shots: https://opendata.dc.gov/datasets/shot-spotter-gun-shots



**ShotSpotter Map**
![shotspotmap](https://user-images.githubusercontent.com/24280548/62429855-4cde1e00-b6e2-11e9-9093-17c0979c4249.jpg)




**Crime Incidents Map**
![crimemaxxxp](https://user-images.githubusercontent.com/24280548/62429888-de4d9000-b6e2-11e9-9dd4-b2cbb23a6053.png)





These maps were created with QGIS in the python console. Vector selection tools parsed out points in the crime data layer that were not carried out with a gun. This created a new vector point layer that was then reclassified by the ward the point occurred  in by the vector general tool: join attributes by location. This join layer contained a field called count that represents the number of points in each ward. This count field was then divided by the population of that ward and multiplied by 10,000 to show the crimes per ward normalized by 10,000 people for appropriate comparison. The ShotSpotter map contained only points related to gun crimes, so it was immediately joined to the ward polygon layer to get the same count field. The calculation for crime per ward per 10,000 people was calculated in the same way as in the crime map. 

The calculation for crime or detected gunshots per ward per 10,000 people aims to avoid a more misleading map visualization where a higher population would inevitably show more crime. 

This table shows the number of gun crimes and shooting incidents detected by ShotSpotter per 10,000 people in 2017 in each ward.


![table](https://user-images.githubusercontent.com/24280548/62430213-66ce2f80-b6e7-11e9-81e3-97729289874d.JPG)







**Automation**

**Results**

Wards 7 and 8 have more crime incidents than any other ward; both also have a large gap between the gun crimes reported and the number of gunshots detected by ShotSpotter. With careful consideration for duplicate incidents and unverified shots, these wards would be a good place to expand and hone the validity of the gunshot detection network. The data available includes a time field that could broaden the analysis. 

Limitations of this analysis include the quality of the input data. 100m resolution accuracy of ShotSpotter data  loosely corresponds to the point data and may have significantly altered the final product maps. Even if the accuracy was within a few inches, the quality of the data, and therefore the analysis displayed in these maps depends on the validity of the sound sensor technology. Additionally, when aggregating to the ward level when we have block level data for where crime incidents are occurring  could make it appear as if the entire ward is suffering from gun violence, when it could be a very small block area within it. 
