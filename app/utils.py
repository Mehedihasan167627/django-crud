
import datetime

def make_year_list(start_year=2000):
    c_year = datetime.datetime.now().year
    li=[("","Select Year")]
    for i in range(c_year,start_year+1,-1):
        li.append((i,i))

    return tuple(li)

