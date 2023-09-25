# In this question, you must write a Python program to output the name of the main 
# referee for a given match date (in yyyy-mm-dd format). The input to your program
# is a file named “date.txt” that has the match date as the first word of the file.
# Your program must assume that date.txt resides in the same folder as your Python program. 

# The output name has to be formatted as follows. The last name is displayed 
# followed by the initials of the first name, then a full stop, a space and then 
# the initials of the middle name (if the middle name exists), followed by a full 
# stop.

# For example, 
# if the name of the main referee is “Kennedy Sapam”, the output must be ”Sapam K.” 
# If the name of the main referee is “Asit Kumar Sarkar”, the output must be ”Sarkar A. K.”

import psycopg2 as ps
import sys
import os

try:
    conn = None
    conn = ps.connect('.........................................')
    cur  = conn.cursor()

    file = open('date.txt', 'r')
    name = file.read()

    query = '''Select referee 
    FROM match_referees mr 
    Join matches m 
    ON mr.match_num = m.match_num 
    Where match_date = %s'''

    cur = cur.execute(query,(name,))
    rows= cur.fetchall()
    
    for row in rows:
        name = row.split() # name = ['niraj', 'kumar', 'thakur']
        if len(name) == 3:
            output = name[-1] + ' ' + name[0][0] + '.' +' '+ name[1] +'.'
            print(output)
        else:
            output = name[-1] + ' ' + name[0][0] + '.' + name[1] +'.'
        
        
except:
    print('Something went wrong')
finally:
    if conn != None:
        conn.close()
    
         
###################################################################
import psycopg2
import sys
import os
conn=None
f=open('date.txt','r')
s=f.readline()

conn= psycopg2.connect(database=sys.argv[1],user=os.environ.get('PGUSER'), password=os.environ.get('PGPASSWORD'),host=os.environ.get('PGHOST'),port=os.environ.get('PGPORT'))
curr=conn.cursor()
curr.execute("select name from referees where referee_id in (select mr.referee from match_referees mr , matches m where m.match_num=mr.match_num and m.match_date=%s)",(s,))
while True:
    row=curr.fetchone()
if not row :
        break
    l=[]
    l+=row[0].split()
    x=l[-1]
    for i in range(0,len(l)-1):
            x+=' '+l[i][0]+'.'
    print(x)
curr.close()
conn.close()