#!/usr/bin/python

#Description
#Python script to export printers from printers.conf, exported printers are added into importprinters which
#creates a bulk lpadmin command for each printer

def exportprinters():

  f = open('/etc/cups/printers.conf', 'r')
  w = open('importprinters.sh', 'w')

  w.write("#!/bin/bash\n\n")

  count = 0

  for i in f:
    if "Printer" in i:
      count += 1
      if "/" not in i:
        if count > 1:
          w.write("lpadmin -p" + (i[i.rfind(' '): -2]) + " -E -P /etc/cups/ppd/" + (i[i.rfind(' ') + 1: -2]) + ".ppd")
    elif "DeviceURI" in i:
      w.write (" -v" + i[i.rfind(' '):])

  f.close()
  w.close()


exportprinters()
