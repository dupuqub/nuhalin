
#coding=UTF-8

symbols = "1234567890"
symbols += "!@#$%^&*()"
symbols += "qwertyuiop[]\\"
symbols += "QWERTYUIOP{}|"
symbols += "asdfghjkl;'"
symbols += 'ASDFGHJKL:"'
symbols += "zxcvbnm,./"
symbols += "ZXCVBNM<>?"

sentence = ""
group = ["","","","","","","","","","","","","","","","","","","","","",""]
counter = 0

for unitLow in symbols:
  for unitHigh in symbols:
    sentence += unitLow + unitHigh

for unit in sentence:
  if len( group[ counter ] ) < 704:
    group[ counter ] += unit
    sentence = sentence[ 1: ]
  else:
    counter += 1
    group[ counter ] += unit
    sentence = sentence[ 1: ]

for unit in group:
  print str( group.index( unit ) ) + " . " + unit
