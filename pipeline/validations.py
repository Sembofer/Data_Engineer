def first_validation(object):
    resp = []
    for tuple in object:
        for x in tuple:
            resp.append(x)
    return str(resp)