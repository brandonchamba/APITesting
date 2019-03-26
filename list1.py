import random

cave_numbers = range(0,20)
caves = []
for i in cave_numbers:
   caves.append([])  #create empty list

unvisited_caves = range(0,20)
visited_caves =[0]
unvisited_caves.remove(0)

while unvisited_caves != []:
   i = random.choice(visited_caves)
   if len(caves[i] ) >=3 :
      continue

   next_cave = random.choice(unvisited_caves)
   caves[i].append(next_cave)
   caves[next_cave].append(i)
   
   visited_caves.append(next_cave)
   unvisited_caves.remove(next_cave)

   for number in cave_numbers:
      print number, ":", caves[number]
   print '-----'

for i in cave_numbers:
   while len(caves[i])  <3 :
      passage_to = random.choice(cave_numbers)
      caves[i].append(passage_to)

   for number in cave_numbers:
      print number, ":", caves[number]
print ' --------'
 
