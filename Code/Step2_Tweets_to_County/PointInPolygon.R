require("rgdal")

args = commandArgs(trailingOnly=TRUE)

boundary <- readOGR("county_shp","us_county_wgs84") #Change it
polys <- as(boundary, "SpatialPolygons")

a<-list.files(args[1]) #Change it

for (b in a) {
  inputFileName = paste(args[1], b, sep="") #Change it
  outputFileName =paste(args[2], b, sep="") #Change it

  data <- read.csv(inputFileName, header=F)

  coordinates(data) <- c(3,2)
  proj4string(data) <- proj4string(polys)

  polyID <- over(data, polys)
  
  newData <- cbind(data,polyID=(polyID-1))
  
  write.table(outputFileName, x=newData[!is.na(polyID),],row.names=F, col.names=F,sep=",")

  print (outputFileName)
}
