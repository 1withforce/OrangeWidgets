"""
<name>Fasta Converter</name>
<description>Converts Fasta files with biological sequences into tab files</description>
<icon>icons/fasta.gif</icon>
<priority>1</priority>
"""

from OWWidget import *
import OWGUI
import re

class OWFastaConverter(OWWidget):
    def __init__(self, parent=None, signalManager=None):
        OWWidget.__init__(self, parent, signalManager, 'FastaConverter')
        self.inputs = [("convertFastaTab", ExampleTable, self.convertFastaTab)]
        self.outputs = [("Tab File", ExampleTable)]

        # GUI
        box = OWGUI.widgetBox(self.controlArea, "Info")
        self.infoa = OWGUI.widgetLabel(box, 'No fasta file yet, waiting to get something.')
        self.infob = OWGUI.widgetLabel(box, '')
        self.resize(100,50)
    def convertFastaTab(self, dataset):
        if dataset:        
            def cleanup(b_array):##eliminates empty array that results from re.split
                return b_array[1:]
        
            input_file=open("{}".format(dataset), 'r')
            primary_input=input_file.read()##primary_input is now a string containing the original fasta data
            headpattern= re.compile(">(.+)$", re.M)#pattern for isolating the header
            filepat=re.compile(r"(.+)\..+")##pattern for finding the file path no matter the extension-may cause a crash if directories have periods in their names
            input_filename=filepat.findall(dataset)[0]
            headers = headpattern.findall(primary_input)
            bodies = re.split(">.*\\n", primary_input)##pattern for isolating bodies (sequences)
            bodies = cleanup(bodies)

            self.clean_bodies1=[]
            self.clean_bodies2=[]

            for i in bodies:
                self.clean_bodies1.append(re.sub("\\n", "", i))##may be redundant

            for i in clean_bodies1:
            	self.clean_bodies2.append(i.strip(" \t\n\r"))

            self.newstring="Description\tSequence Data\n\n"
            for i in range(len(clean_bodies2)):
                self.newstring=newstring+headers[i]+"\t"+self.clean_bodies2[i]+"\n"##Format: head1<tab>body1<newline>...
            #print newstring
        
        	self.output=open("{}.tab".format(input_filename), 'w')
        	self.final = output.write(newstring)
        	self.infob.setText("File converted, saved as {}.tab".format(input_filename))
        	self.send('Tab File', self.final)
        else:
            self.infoa.setText('No data on input yet, waiting to get something.')
            self.infob.setText('')
            self.send("Tab File", None)

if __name__=="__main__":
    appl = QApplication(sys.argv)
    ow = OWFastaConverter()
    ow.show()
    dataset = orange.ExampleTable('../datasets/iris.tab')
    ow.convertFastaTab(dataset)
    appl.exec_()		