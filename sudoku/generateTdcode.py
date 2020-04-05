
text = ''
f = open('random.txt','w')
for x in range(0,9):
    text += '''<tr>'''
    for y in range(0,9):
        text += '''<td><input name="cell''' + str(x)+str(y)+'''" type="number" min="0" max="9"   value="{{ cell''' + str(x) + str(y) + ''' }}"></td>'''
    text+='''</tr>'''

f.write(text)
f.close()
