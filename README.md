# ARUP-Singapore-Tasks-for-Interviewees

I chose Task A and I picked Rhinoceros 3D as the BIM/CAD/GIS software to implement the task. Among all the options, I chose Rhino.Python as I think it could be easy for me to finish the task. As I am using MacBook Pro, I downloaded Rhino 5, Which is currently the lastest version available for MacOS, and hence referred to it API document (http://developer.rhino3d.com/5/guides/rhinopython/your-first-python-script-in-rhino-mac/) for gathering the ideas to be applied in this exercise.

I found there is a method call LayerNames which is able to list the names of all layer within the given file.
http://developer.rhino3d.com/api/rhinoscript/layer_methods/layernames.htm

For exporting all layer names to a text file, I simply referred to the tutorial about writing a file.
http://developer.rhino3d.com/5/guides/rhinopython/python-reading-writing/

In order to separate the output by line breaks, since I didn't quiet familier with python language, I check a bit online and found a guide from stackoverflow to work it out.
https://stackoverflow.com/questions/34201288/write-a-txt-from-list-without-brackets

To use this add-in in Rhino, you can just simply add the command from the top-left corner of it interface, insert "RunPythonScript" to the text box.

![alt text](https://github.com/erxuansung/ARUP-Singapore-Tasks-for-Interviewees/blob/master/1.png)

Then select the target file which commits to the assigned action, exporting all layer names to a text file.

![alt text](https://github.com/erxuansung/ARUP-Singapore-Tasks-for-Interviewees/blob/master/2.png)

You can either giving the text file a name or leave it to default, after select a folder to save the file, press the "save" botton.

![alt text](https://github.com/erxuansung/ARUP-Singapore-Tasks-for-Interviewees/blob/master/3.png)

Lasty, go directly to the folder and check it out, the result will be as follow.

![alt text](https://github.com/erxuansung/ARUP-Singapore-Tasks-for-Interviewees/blob/master/4.png)
