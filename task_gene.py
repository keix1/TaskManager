# coding: utf-8

jmam = []
applied = []
for a in range(1, 8):
    for b in ['月', '火', '水', '木']:
        jmam.append('JMAM,リスニング 第' + str(a) + '週 ' + str(b) + '曜日,20\n')

for a in range(1, 8):
    for b in ['月', '火', '水', '木']:
        jmam.append('JMAM,リーディング第 ' + str(a) + '週 ' + str(b) + '曜日,20\n')
for a in range(1, 81):
    applied.append('応用情報,28年春 第' + str(a) + '問,1\n')

with open('tasks.csv', 'a', encoding='utf-8') as file:
    for x in applied:
        file.write(x)
    for x in jmam:
        file.write(x)
