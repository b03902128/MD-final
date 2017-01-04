import re
import sys
data_dir="../../data/"
file=sys.argv[1]

cntn=open(data_dir+file).read()

pattern = re.compile('([^\s\w]|_)+')
strippedList = pattern.sub('', cntn.lower().replace('\n',''))

fd=open(data_dir+file+'_normal','w')
fd.write(strippedList)