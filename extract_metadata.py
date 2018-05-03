import os
import sys
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element, SubElement
import base64

global archivo
archivo = open("Metadata.txt","w")
archivo.write("Archivo|Titulo|createdate|createtime|argisformat|synconce|itemname|extentsWB|extentsEB|extentsSB|extentsNB|coordRefType|geogcsn|csUnits|projcsn|peXml|SyncDate|SyncTime|ModDate|ModTime|minScale|maxScale|ArcGISProfile|resTitle|westBL|eastBL|northBL|southBL|exDesc.Registro|idPurp|idAbs|searchkeys|rpIndName|rpOrgName|rpPosName|cntAddresscity|cntadminArea|cntcountry|cntdelPoint|cntPhone|cntHours|cntInstr|Imagen_Filename\n")

directory = "C:/GEOPALMIRA_CORE_V3/SpatialDatabase/Shapefiles"


def readXMLFile(xmlfile):
    head, tail = os.path.split(xmlfile)
    tree = ElementTree()
    tree.parse(xmlfile)

    createdate = tree.find("Esri/CreaDate")
    createtime = tree.find("Esri/CreaTime")
    argisformat = tree.find("Esri/ArcGISFormat")
    synconce = tree.find("Esri/SyncOnce")

    itemname = tree.find("Esri/DataProperties/itemProps/itemName")

    extentsWB = tree.find("Esri/DataProperties/itemProps/nativeExtBox/westBL")
    extentsEB = tree.find("Esri/DataProperties/itemProps/nativeExtBox/eastBL")
    extentsSB = tree.find("Esri/DataProperties/itemProps/nativeExtBox/southBL")
    extentsNB = tree.find("Esri/DataProperties/itemProps/nativeExtBox/northBL")

    coordRefType = tree.find("Esri/DataProperties/coordRef/type")
    geogcsn = tree.find("Esri/DataProperties/coordRef/geogcsn")
    csUnits = tree.find("Esri/DataProperties/coordRef/csUnits")
    projcsn = tree.find("Esri/DataProperties/coordRef/projcsn")
    peXml   = tree.find("Esri/DataProperties/coordRef/peXml")
    syncDate = tree.find("Esri/SyncDate")
    syncTime = tree.find("Esri/SyncTime")
    modDate = tree.find("Esri/ModDate")
    modTime = tree.find("Esri/ModTime")
    minScale = tree.find("Esri/scaleRange/minScale")
    maxScale = tree.find("Esri/scaleRange/maxScale")
    ArcGISProfile = tree.find("Esri/ArcGISProfile")

    resTitle   = tree.find("dataIdInfo/idCitation/resTitle")

    westBL = tree.find("dataIdInfo/dataExt/geoEle/GeoBndBox/westBL")
    eastBL= tree.find("dataIdInfo/dataExt/geoEle/GeoBndBox/eastBL")
    northBL= tree.find("dataIdInfo/dataExt/geoEle/GeoBndBox/northBL")
    southBL= tree.find("dataIdInfo/dataExt/geoEle/GeoBndBox/southBL")

    exDesc = tree.find("dataIdInfo/dataExt/exDesc")

    idPurp = tree.find("dataIdInfo/idPurp")
    idAbs  = tree.find("dataIdInfo/idAbs")

    searchKeys  = tree.find("dataIdInfo/searchKeys")

    rpIndName   = tree.find("dataIdInfo/idPoC/rpIndName")
    rpOrgName   = tree.find("dataIdInfo/idPoC/rpOrgName")

    rpPosName   = tree.find("dataIdInfo/idPoC/rpPosName")

    cntAddresscity   = tree.find("dataIdInfo/idPoC/rpCntInfo/cntAddress/city")
    cntadminArea    = tree.find("dataIdInfo/idPoC/rpCntInfo/cntAddress/adminArea")
    cntcountry    = tree.find("dataIdInfo/idPoC/rpCntInfo/cntAddress/country")
    cntdelPoint = tree.find("dataIdInfo/idPoC/rpCntInfo/cntAddress/delPoint")

    cntPhone = tree.find("dataIdInfo/idPoC/rpCntInfo/cntPhone/voiceNum")
    cntHours = tree.find("dataIdInfo/idPoC/rpCntInfo/cntHours")
    cntInstr = tree.find("dataIdInfo/idPoC/rpCntInfo/cntInstr")

    imagen = tree.find("Binary/Thumbnail/Data")

    print('------------------------------------')
    print(tail)
    archivo.write(tail)

    print(tail[:-8])
    archivo.write(" |")
    archivo.write(tail[:-8])

    print(createdate.text)
    archivo.write(" |")
    archivo.write(createdate.text)

    print(createtime.text)
    archivo.write(" |")
    archivo.write(createtime.text)

    print(argisformat.text)
    archivo.write(" |")
    archivo.write(argisformat.text)

    print(synconce.text)
    archivo.write(" |")
    archivo.write(synconce.text)

    print((itemname.text).encode('utf-8').strip())
    archivo.write(" |")
    archivo.write((itemname.text).encode('utf-8').strip())


    #Extents
    print(extentsWB.text)
    archivo.write(" |")
    archivo.write(extentsWB.text)

    print(extentsEB.text)
    archivo.write(" |")
    archivo.write(extentsEB.text)

    print(extentsSB.text)
    archivo.write(" |")
    archivo.write(extentsSB.text)

    print(extentsNB.text)
    archivo.write(" |")
    archivo.write(extentsNB.text)



    print(coordRefType.text)
    archivo.write(" |")
    archivo.write(coordRefType.text)

    print(geogcsn.text)
    archivo.write(" |")
    archivo.write(geogcsn.text)

    print(csUnits.text)
    archivo.write(" |")
    archivo.write(csUnits.text)

    print(projcsn.text)
    archivo.write(" |")
    archivo.write(projcsn.text)

    print(peXml.text)
    archivo.write(" |")
    archivo.write(peXml.text)

    print(syncDate.text)
    archivo.write(" |")
    archivo.write(syncDate.text)

    print(syncTime.text)
    archivo.write(" |")
    archivo.write(syncTime.text)

    print(modDate.text)
    archivo.write(" |")
    archivo.write(modDate.text)

    print(modTime.text)
    archivo.write(" |")
    archivo.write(modTime.text)

    #print(minScale.text)
    #archivo.write(" |")
    #archivo.write(minScale.text)
	
    try:
        print(minScale.text)
        archivo.write(" |")
        archivo.write(minScale.text)
    except:
        print('Sin registro')
        archivo.write(" |")
        archivo.write('Sin registro')

    try:
        print(maxScale.text)
        archivo.write(" |")
        archivo.write(maxScale.text)
    except:
        print('Sin registro')
        archivo.write(" |")
        archivo.write('Sin registro')    

    #print(maxScale.text)
    #archivo.write(" |")
    #archivo.write(maxScale.text)

    #print(ArcGISProfile.text)
    #archivo.write(" |")
    #archivo.write(ArcGISProfile.text)

    try:
        print(ArcGISProfile.text)
        archivo.write(" |")
        archivo.write(ArcGISProfile.text)
    except:
        print('Sin registro')
        archivo.write(" |")
        archivo.write('Sin registro')

    print((resTitle.text).encode('utf-8').strip())
    archivo.write(" |")
    archivo.write((resTitle.text).encode('utf-8').strip())


    print(westBL.text)
    archivo.write(" |")
    archivo.write(westBL.text)

    print(eastBL.text)
    archivo.write(" |")
    archivo.write(eastBL.text)

    print(northBL.text)
    archivo.write(" |")
    archivo.write(northBL.text)

    print(southBL.text)
    archivo.write(" |")
    archivo.write(southBL.text)


    try:
        print(exDesc.text)
        archivo.write(" |")
        archivo.write(exDesc.text)
    except:
        print('Sin registro')
        archivo.write(" |")
        archivo.write('Sin registro')

    #print(idPurp.text)
    #archivo.write(" |")
    #archivo.write((idPurp.text).encode('utf-8').strip())

    try:
        print((idPurp.text).encode('utf-8').strip())
        archivo.write(" |")
        archivo.write((idPurp.text).encode('utf-8').strip())
    except:
        print('Sin registro')
        archivo.write(" |")
        archivo.write('Sin registro')

    print((idAbs.text).encode('utf-8').strip())
    archivo.write(" |")
    archivo.write((idAbs.text).encode('utf-8').strip())

    str_searchkeys=""
    try:
        for searchkeys in searchKeys:
            str_searchkeys+=searchkeys.text+','
            #print(searchkeys.text)
    except:
        str_searchkeys='Sin searchkeys'
        print('Sin searchkeys')

    print(str_searchkeys[:-1])
    archivo.write(" |")
    archivo.write((str_searchkeys[:-1]).encode('utf-8').strip())

    archivo.write(" |")
    try:
        print(rpIndName.text)
        archivo.write(rpIndName.text)
    except:
        print('No rpIndName')
        archivo.write('No rpIndName')

    archivo.write(" |")
    try:
        print(rpOrgName.text)
        archivo.write(rpOrgName.text)
    except:
        print('No rpOrgName')
        archivo.write('No rpOrgName')

    archivo.write(" |")
    try:
        print(rpPosName.text)
        archivo.write(rpPosName.text)
    except:
        print('No rpPosName')
        archivo.write('No rpPosName')

    archivo.write(" |")
    try:
        print(cntAddresscity.text)
        archivo.write(cntAddresscity.text)
    except:
        print('No cntAddresscity')
        archivo.write('No cntAddresscity')

    archivo.write(" |")
    try:
        print(cntadminArea.text)
        archivo.write(cntadminArea.text)
    except:
        print('No cntadminArea')
        archivo.write('No cntadminArea')

    archivo.write(" |")
    try:
        print(cntcountry.text)
        archivo.write(cntcountry.text)
    except:
        print('No cntcountry')
        archivo.write('No cntcountry')

    archivo.write(" |")
    try:
        print(cntdelPoint.text)
        archivo.write(cntdelPoint.text)
    except:
        print('No cntdelPoint')
        archivo.write('No cntdelPoint')

    archivo.write(" |")
    try:
        print(cntPhone.text)
        archivo.write(cntPhone.text)
    except:
        print('No cntPhone')
        archivo.write('No cntPhone')

    archivo.write(" |")
    try:
        print(cntHours.text)
        archivo.write(cntHours.text)
    except:
        print('No cntHours')
        archivo.write('No cntHours')

    archivo.write(" |")
    try:
        print(cntInstr.text)
        archivo.write(cntInstr.text)
    except:
        print('No cntInstr')
        archivo.write('No cntInstr')

    archivo.write(" |")
    try:
        #print(imagen.text)
        #Read and Write Metadata Image File
        imgdata = base64.b64decode(imagen.text)
        #cut extension .shp.xml
        filename = xmlfile[:-8]+'.jpg'
        with open(filename, 'wb') as f:
            f.write(imgdata)
    except:
        print('No Imagen')
        filename = ('No Imagen')
    archivo.write(filename)
    archivo.write("|\n")

    print('------------------------------------')


for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".xml"):
            print(os.path.join(root, file))
            readXMLFile(os.path.join(root, file))
    archivo.close()
