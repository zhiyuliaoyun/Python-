
def smart_function( ):
    def f( ):
        x = 0
        while True:
              x = x +1
              yield x
    
    sum = f( ) 
      
    def  cal( ):
         return next( sum )
 
    return cal()
