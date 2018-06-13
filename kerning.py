
# coding=UTF-8

symbols = "012345678!@#$%^&"
symbols += ")(][}{<>"
symbols += "'\"`~"
symbols += "+*-/="
symbols += ",.?"
symbols += "ieéaáoóu"
symbols += "IEÉAÁOÓU"
symbols += "fvszxj"
symbols += "FVSZXJ"
symbols += "bpdtgk"
symbols += "BPDTGK"
symbols += "hylrnm"
symbols += "HYLRNM"

sentence = ""
group = ["","","","","","","","","","","","","","","","","","","","","",""]
counter = 0

# step 1

for eachHigh in symbols:
  for eachLow in symbols:
    sentence += eachHigh + eachLow

# step 2

for each in sentence:
  if len (group [counter]) < 704:
    group [counter] += each
    sentence = sentence [1:]
  else:
    counter += 1
    group [counter] += each
    sentence = sentence [1:]

# step 3

for each in group:
  print (str (group.index (each)) + " . " + each)

