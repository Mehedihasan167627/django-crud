
import datetime
import re 


def make_year_list(start_year=2000):
    c_year = datetime.datetime.now().year
    li=[("","Select Year")]
    for i in range(c_year,start_year+1,-1):
        li.append((i,i))

    return tuple(li)


def make_user_id(queryset,start_with_str="AB"):
    str_id=start_with_str+"-01"
    if queryset.count():
        count=re.findall("\d{1,10}",queryset.last().str_id)
        count=int("".join(count))
        if count<9:str_id=start_with_str+"-0"+str(int(count)+1)
        else:str_id=start_with_str+"-"+str(int(count)+1)
    return str_id 
