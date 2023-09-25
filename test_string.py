def string(rows):
  print('rows varible contains: ',rows)

  for row in rows:
      print('row varible contains: ', row)
      name = row.split()
      print(name)
      if len(name) == 3:
          output = name[2] + ' ' + name[0][0] + '.' + name[1][0] +'.'
          print('final_output: ', output)
      else:
          output =name[1] + ' ' + name[0][0] + '.'
          print('final_output: ', output)
    #   return(True)
  
x =  ['Pawan kumar pandey', 'Niraj kumar', 'Jannet Blessy A'] 
print(string(x))