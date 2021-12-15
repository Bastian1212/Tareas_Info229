from datetime import datetime



fechaA = str(datetime.today().strftime('%Y-%m-%d'))

fechaA = ''.join( x for x in fechaA if x not in "-")



print(fechaA)