# xmlparsing-python
Small utility for parsing dynamic traffic-matricies in the form of XML-files as given i.e. for instances with dynamic traffic in the [SNDlib](https://www.sndlib.zib.de). Although designed for traffic-matricies, the code can be easily modified for parsing XML-files containing different data.

## Usage
For using the parsers, the folder containing the source-file has to be in $PATHONPATH. After importing, the functions `xmlparser.xmlMeanParser()` and `xmlparser.xmlDemandsParser()` are available for outside use. For a description of the functions see code-comments .

To parse a set of XML-files, there has to exist an `index` file in which each line contains the path to a XML-file. Default name of this file is `index.txt`, but any name can be passed to the functions using the argument `index_file`. An easy way to generate these files (on linux) would be to store all the XML-files in one folder and then running
```
ls -1 *.py > index.txt
```

