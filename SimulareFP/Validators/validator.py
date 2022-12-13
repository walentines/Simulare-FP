def validate_id(id):
    '''
    Validator pt id
    :param id:
    :return:
    '''
    try:
        id = int(id)
    except:
        return False
    if(id > 0):
        return True
    return False