#Sela Gordon
#08/04/2019
#GEOG 682 Final


import processing
#Crime = "Z:/hereyago/finalproj/Crime_Incidents_in_2017.shp"#save shapefile as new variable
#iface.addVectorLayer(Crime,"Crime","ogr")


#SELECTS CRIME ONLY
#processing.runalg("qgis:selectbyattribute", 
#    {'INPUT':Crime,'FIELD':"METHOD",'OPERATOR':0,'VALUE':'GUN'})


##ADD WARD
#Ward="Z:/hereyago/finalproj/Ward_from_2012.shp"
#iface.addVectorLayer(Ward,"Ward","ogr")

#jcrime='Z:/hereyago/finalproj/jcrime.shp'
#processing.runalg('qgis:countpointsinpolygon',
#{'POLYGONS':Ward,
#'POINTS':Crime,
#'FIELD': 'count',
#'OUTPUT':jcrime})
#
#iface.addVectorLayer(jcrime,"jcrime","ogr")
#JCRIME IS THE LAYER THAT HAS THE COUNT FOR CRIME INCIDENTS PER WARD

#B='Z:/hereyago/finalproj/dontcrash/jjjjjj.shp'
#processing.runalg('qgis:fieldcalculator',jcrime,"dpp",0,10,3,True,"10000.0 * count / POP_2010",B)

#iface.addVectorLayer(B,"B","ogr")
##B IS THE MAP LAYER THAT WAS SYMBOLIZED WITH FIELD DPP

##DPP is my shorthand for incidents per 10,000 people per ward
## THIS PRINTS THE WARDS WITH THEIR DPP 
#jcrime=iface.activeLayer()
#H = jcrime.getFeatures()

#
#for h in H:
#    count = float(h["count"])
#    pop = h["POP_2010"]
#    dpp = (count/pop)*10000
#    name = h["NAME"]
#    
#    print((name,dpp))
#

#

##ADD SHOTSPOT
#Shot="Z:/hereyago/finalproj/Shot_Spotter_Gun_Shots.shp"
#iface.addVectorLayer(Shot,"Shot","ogr")
#shotlayer=iface.activeLayer()
#
#only17='left("DATETIME",4) = 2017'
#shotlayer.selectByExpression(only17,QgsVectorLayer.SetSelection)
#QgsVectorFileWriter.writeAsVectorFormat(shotlayer, 'Z:/hereyago/finalproj/dontcrash/shotsonly17.shp','utf-8',shotlayer.crs(),'ESRI Shapefile',1)
#
#shotlayer1= 'Z:/hereyago/finalproj/dontcrash/shotsonly17.shp'
#iface.addVectorLayer(shotlayer1,"shotlayer1","ogr")
#
###
#jshot2='Z:/hereyago/finalproj/jshotredo.shp'
#processing.runalg('qgis:countpointsinpolygon',
#{'POLYGONS':Ward,
#'POINTS':shotlayer1,
#'FIELD': 'count',
#'OUTPUT':jshot2})
#
#iface.addVectorLayer(jshot2,"jshot2","ogr")


##JSHOT2 HAS THE POLY LAYER WITH COUNT FOR SHOTSPOT DETECTIONS PER WARD




#X='Z:/hereyago/finalproj/dontcrash/ffffff.shp'
#processing.runalg('qgis:fieldcalculator',jshot2,"dpp",0,10,3,True,"10000.0 * count / POP_2010",X)

#iface.addVectorLayer(X,"X","ogr")

##X IS THE LAYER THAT WAS SYMBOLIZED USING FIELD DPP
## THIS PRINTS THE WARDS WITH THEIR DPP 
#G = jshot2.getFeatures()
#for g in G:
#    count = float(g["count"])
#    pop = g["POP_2010"]
#    DPP = (count/pop)*10000
#    name = g["NAME"]
#    
#    print((name,DPP))
#








