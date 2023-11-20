import datetime
def date_list_filter(date_list,starting_date,ending_date):#takes the date list from a person and turns it into a single list between the date ranges given
    filt_date_list = []
    for i in date_list:
        if isinstance(i,datetime.datetime):#only dates today baby :>      
            if i > starting_date and i < ending_date:
                filt_date_list.append(i)
    return filt_date_list

lista = [datetime.datetime(2023,10,3),datetime.datetime(2023,1,4,0,0),"N/A",datetime.datetime(2023,9,7,0,0)
         ,datetime.datetime(2023,12,29,0,0),"N/A"]
st_date = datetime.datetime(2023,2,1)
en_date = datetime.datetime(2023,10,31)
a = date_list_filter(lista,st_date,en_date)
print(a)