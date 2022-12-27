from datetime import date

def get_today():
   return date.today()
 
def mock_date():
   print("testing mock")
   day = get_today()
   print("testing mock date")
   return day