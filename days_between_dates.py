days_of_months={'Jan':31, 'Feb':28, 'Mar':31 , 'Apr':30, 'May':31, 'Jun':30, 'Jul':31, 'Aug':31, 'Sep':30, 'Oct':31, 'Nov':30, 'Dec':31}
days_of_months2=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# This Function check year is leap year or not.
def leapyear(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else: return False
        else: return True
    else: return False

# Takes d1 as date1, m1 as month2, y1 as year1 and d2, m2, y2 as date2, month2, year2.
def days(d1,m1,y1,d2,m2,y2):
    count=0
    if y1==y2:
        if m2==m1:
            return d2-d1
        else:
            if leapyear(y1):
                days_of_months['Feb']=29
            else:
                days_of_months['Feb']=28
            a=days_of_months2.index(m1)
            b=days_of_months2.index(m2)
            count+=days_of_months[days_of_months2[a]]-d1
            count+=d2
            for i in range(a+1,b):
                count+=days_of_months[days_of_months2[i]]
            return count
    else:
        if leapyear(y1):
            days_of_months['Feb']=29
        else:
            days_of_months['Feb']=28
        a=days_of_months2.index(m1)
        count+=days_of_months[days_of_months2[a]]-d1
        for i in range(a+1,len(days_of_months2)):
            count+=days_of_months[days_of_months2[i]]
        for i in range(y1+1,y2):
            if leapyear(i):
                count+=366
            else:
                count+=365
        if leapyear(y2):
            days_of_months['Feb']=29
        else:
            days_of_months['Feb']=28
        b=days_of_months2.index(m2)
        for i in range(0,b):
            count+=days_of_months[days_of_months2[i]]
        count+=d2       
        return count

# Passing Values
print(days(1,"Jan",2020,1,"Feb",2020))