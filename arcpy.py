import arcpy

mxd = arcpy.mapping.MapDocument(r"C:\Users\Caicedo\Downloads\analysis\ESRI\MAPS\datadriven.mxd")
for pageNum in range(1, mxd.dataDrivenPages.pageCount + 1):
    mxd.dataDrivenPages.currentPageID = pageNum
    print (" :)  pagina {0} de {1}".format(str(mxd.dataDrivenPages.currentPageID), str(mxd.dataDrivenPages.pageCount)))
    arcpy.mapping.ExportToPNG(mxd, r"C:\Users\Caicedo\Downloads\analysis\ESRI\MAPS\datadriven.mxd" + str(pageNum) + ".png")

del mxd
