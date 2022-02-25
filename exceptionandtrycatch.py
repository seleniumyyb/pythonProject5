"""ItemsIncart = 0
# 2 item will added to the cart
if ItemsIncart != 2:
   pass                                                                 #raise Exception("Product cart count not matching")

assert(ItemsIncart==0)                                                                 #another method of exception

                                           #TRY CATCH BUT PYTHON USES EXCEPT KEYWORD
#take random file name filelog

try:
      with open('filelog.txt', 'r') as reader:
         reader.read()
except:
   print('some how i reached this block because there is failure in try block ')

                                                        # if you put correct file name test.txt the error pass


try:
      with open('test.txt', 'r') as reader:
         reader.read()
except:
   print('some how i reached this block because there is failure in try block ')
                                                       #python customized messg.

try:
   with open('filelog.txt', 'r') as reader:                # still file is wrong but out put execute and tell us wrong file name
      reader.read()
except Exception as e:
     print(e)

                                                # using finally key word always comes with try or except


try:
   with open('filelog.txt', 'r') as reader:
      reader.read()
except Exception as e:
     print(e)

finally:
   print("cleaning up resources")"""

                                                        #now give actual file name test.txt no error output and cleaning up printed



try:
   with open('test.txt', 'r') as reader:
      reader.read()
except Exception as e:
     print(e)

finally:
   print("cleaning up records like already checked like cookies")
