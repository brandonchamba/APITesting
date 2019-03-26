class node:
   def __init__(self, data=None):
      self.data = data
      self.next=None

class linked_list:
   def __init__(self):
      self.head = node()

   #append function in the list object add new data point to end of list
   def append(self, data):
      new_node = node(data)
      cur = self.head
      while cur.next != None:
         cur = cur.next
      cur.next = new_node
   def length(self):
      cur = self.head
      total = 0
      while cur.next != None:
         total +=1
         cur = cur.next
      return total
  
   def display(self):
      elems = []
      cur_node = self.head
      while cur_node.next  != None:
         cur_nod = cur_node.next
         elems.append(cur_node.data)
      print ('the {}'.format(elems))
   
   def get(self, index):
      if index >= self.length():
         print("Error: 'Get' Index out of range!")
      return None



my_list = linked_list()

my_list.append(3)
my_list.append(5)
my_list.append(10)
my_list.display()
