f = open('Game.txt','r')
g = f.readlines()
for i in g:
    h = i.split()
print(h)

length = len(h)
min_time = 181
min_name = ''
for i in range(1,length+1,2):
    y = int(float((h[i])))
    if y <= min_time:
        min_time = int(float((h[i])))
        min_name = h[i-1]

print('highscorer: 'min_name,min_time)
    
