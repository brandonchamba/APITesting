import time

start=time.time()
for i in range(200):
   print i
end =time.time()
range_time = start - end
print ('executed time of range is {}'.format(range_time))

start_xrange=time.time()
for i in xrange(200):
   print i
end_xrange =time.time()
xrange_time = start_xrange - end_xrange
print ('executed time of xrange is {}'.format(xrange_time))

if xrange_time > range_time:
   print ('xrange_time: {} is larger than range_time {}'.format(xrange_time - range_time))
else:
   print('xrange_time {} is smaller than range_time{}'.format(xrange_tine - range_tine))
