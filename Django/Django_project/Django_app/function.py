# global variables used in Django_app/views.
IFSC_Hit_Count = {}
API_Hit_Count = {}


# Create your functions here.


def api_count(request):
    '''
    The function counts all urls hits.

    Parameters:
        request: Required for retrieving complete requested url.
    '''
    
    # if url exists then increment its value by 1.
    if API_Hit_Count.get(str(request.build_absolute_uri())):
        val = API_Hit_Count.get(str(request.build_absolute_uri()))
        val += 1
        upgraded_dict = {str(request.build_absolute_uri()): val}
        API_Hit_Count.update(upgraded_dict)
    else:
        # update a new url with hit count as 1.
        API_Hit_Count.update({str(request.build_absolute_uri()): 1})
    return


def ifsc_count(request):
    '''
    The function counts all ifsc search urls hits.

    Parameters:
        request: Required for retrieving complete requested url.
    '''
    
    # if ifsc url exists then increment its value by 1.
    if IFSC_Hit_Count.get(str(request.build_absolute_uri())):
        val = IFSC_Hit_Count.get(str(request.build_absolute_uri()))
        val += 1
        upgraded_dict = {str(request.build_absolute_uri()): val}
        IFSC_Hit_Count.update(upgraded_dict)
    else:
        # update a new ifsc url with hit count as 1.
        IFSC_Hit_Count.update({str(request.build_absolute_uri()): 1})
    return
