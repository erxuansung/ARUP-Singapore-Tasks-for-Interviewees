import rhinoscriptsyntax as rs

def ExportLayerNames():
    # Get all layer names
    layerNames = rs.LayerNames()
    if (layerNames==None): return

    layerNames.sort()

    #Get the filename to create
    filter = "Text File (*.txt)|*.txt|All Files (*.*)|*.*||"
    filename = rs.SaveFileName("Save Layer Names as", filter)
    if( filename==None ): return

    #Write all layer names to the created file
    file = open(filename, "w")
    for item in layerNames:
            #separate the output by line breaks
            file.write(item + "\n")
    file.close()

##########################################################################
# Check to see if this file is being executed as the "main" python
# script instead of being used as a module by some other python script
# This allows us to use the module which ever way we want.
if( __name__ == "__main__" ):
  #call function defined above
  ExportLayerNames()
