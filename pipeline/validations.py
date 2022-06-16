
def valid_data(number, data):
    requirements = [1,2,3,4]
    if number in requirements:
        if number ==2:
            if data >=0 and data <=206:
                return True
            else:
                return False
        elif number ==4:
            if data >=0 and data <=15:
                return True
            else:
                return False
    else:
        return False

def valid_query(sql_file):
    query = ['query_2','query_4']
    if sql_file in query:
        return True
    else:
        return False


def valid_format(object):
    resp = []
    for tuple in object:
        for x in tuple:
            resp.append(x)
    return str(resp)