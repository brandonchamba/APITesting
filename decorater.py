def new_decorator(func):
   def wrap_func():
      print('Code here, before executing the func')
      func()   #func  -> Call the object, func() call the return function
      print ('Code here will ececute afgter the func()')
   return wrap_func

def func_needs_decorator():
   print('This function needs a decorator')


func_needs_decorator = new_decorator(func_needs_decorator)
func_needs_decorator()
print('--------')
print ('with @new_decorator')

@new_decorator
def func_needs_decorator():
   print('This function needs a decorator')
func_needs_decorator()

