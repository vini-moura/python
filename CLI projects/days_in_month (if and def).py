def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return(True)
      else:
        return(False)
    else:
      return(True)
  else:
    return(False)


def days_in_month(ano,mes):
  month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  a = month[int(mes)-1]
  if is_leap(ano) == True and month ==2:
    a +=1
  return(a)
  
  

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)