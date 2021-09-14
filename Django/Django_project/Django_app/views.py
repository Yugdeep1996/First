from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
import traceback

from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

import urllib.request

import json

# local imports
from .validations import *
from .function import *


# Create your views here.


class Ifsc_viewset(viewsets.ViewSet):
    # cache requested url for 20 seconds.
    @method_decorator(cache_page(20))
    def list(self, request):
        try:
            '''
            The function to search for related ifsc bank data.
  
            Parameters:
                ifsc_code (String): The code to be searched.
            
            Returns:
                list_of_data: A list which contains the ifsc related bank data.
            '''

            # function for all url hit counts.
            api_count(request)
            # function for ifsc url hit counts.
            ifsc_count(request)

            # required requested parameter.
            if request.GET.get('ifsc_code'):
                # validating parameter.
                if isValidIFSCode(request.GET.get('ifsc_code')):
                    # source contain JSON data from API.
                    source = urllib.request.urlopen('http://127.0.0.1:5000/ifsc_search?ifsc_code='+request.GET.get('ifsc_code')).read()
                    # converting JSON data to a dictionary.
                    list_of_data = json.loads(source)
                    return Response({"data": {'IFSC RESULTS': list_of_data}, "message": "IFSC SEARCHED DATA", "success": True}, status=status.HTTP_200_OK)
                else:
                    raise Exception("Ifsc code invalid !")
            else:
                raise Exception("Ifsc code required !")
        except Exception as error:
            traceback.print_exc()
            return Response({"message": str(error), "success": False}, status=status.HTTP_200_OK)


class Bank_leader_board_Viewset(viewsets.ViewSet):
    def list(self, request):
        try:
            '''
            The function for bank leader board data.
  
            Parameters:
                sortorder (String): The sorting order ASC/DESC,
                fetchcount (String): The counts to be fetched.
            
            Returns:
                list_of_data: A list which contains the bank leader board data.
            '''

            # function for all url hit counts.
            api_count(request)
            
            # validating parameters.
            if not isValidsortorder(request.GET.get('sortorder') or ""):
                raise Exception("Sort input must be 'ASC' or 'DESC' !")
            if not isValidfetchcount(request.GET.get('fetchcount') or ""):
                raise Exception("fetchcount must be an +ve integer !")

            # required requested parameters.
            if request.GET.get('sortorder') and request.GET.get('fetchcount'):
                # source contain JSON data from API.
                source = urllib.request.urlopen('http://127.0.0.1:5000/bank_leader_board?sortorder='+request.GET.get('sortorder')+'&fetchcount='+request.GET.get('fetchcount')).read()
                # converting JSON data to a dictionary.
                list_of_data = json.loads(source)
                return Response({"BANK LEADER BOARD RESULTS": list_of_data, "message": "BANK LEADER BOARD DATA", "success": True}, status=status.HTTP_200_OK)
            else:
                if request.GET.get('sortorder'):
                    # source contain JSON data from API.
                    source = urllib.request.urlopen('http://127.0.0.1:5000/bank_leader_board?sortorder='+request.GET.get('sortorder')+'&fetchcount=10').read()
                elif request.GET.get('fetchcount'):
                    # source contain JSON data from API.
                    source = urllib.request.urlopen('http://127.0.0.1:5000/bank_leader_board?sortorder=DESC&fetchcount='+request.GET.get('fetchcount')).read()
                else:
                    # source contain JSON data from API.
                    source = urllib.request.urlopen('http://127.0.0.1:5000/bank_leader_board?sortorder=DESC&fetchcount=10').read()
                # converting JSON data to a dictionary.
                list_of_data = json.loads(source)
                return Response({"BANK LEADER BOARD RESULTS": list_of_data, "message": "BANK LEADER BOARD DATA", "success": True}, status=status.HTTP_200_OK)

        except Exception as error:
            traceback.print_exc()
            return Response({"message":str(error),"success":False},status=status.HTTP_200_OK)


class Statistics_viewset(viewsets.ViewSet):
    def list(self, request):
        try:
            '''
            The function for searched ifsc code with timestamp statistics data.
  
            Parameters:
                sortorder (String): The sorting order ASC/DESC,
                fetchcount (String): The counts to be fetched.
            
            Returns:
                list_of_data: A list which contains the ifsc statistics data.
            '''

            # function for all url hit counts.
            api_count(request)

            # validating parameters data.
            if not isValidsortorder(request.GET.get('sortorder') or ""):
                raise Exception("Sort input must be 'ASC' or 'DESC' !")
            if not isValidfetchcount(request.GET.get('fetchcount') or ""):
                raise Exception("fetchcount must be an +ve integer !")

            # required requested parameters.
            if request.GET.get('sortorder') and request.GET.get('fetchcount'):
                # source contain JSON data from API.
                source = urllib.request.urlopen('http://127.0.0.1:5000/stats?sortorder='+request.GET.get('sortorder')+'&fetchcount='+request.GET.get('fetchcount')).read()
                # converting JSON data to a dictionary.
                list_of_data = json.loads(source)
                return Response({"STATISTICS RESULTS": list_of_data, "message": "STATISTICS DATA", "success": True}, status=status.HTTP_200_OK)
            else:
                if request.GET.get('sortorder'):
                    # source contain JSON data from API.
                    source = urllib.request.urlopen('http://127.0.0.1:5000/stats?sortorder='+request.GET.get('sortorder')+'&fetchcount=ALL').read()
                elif request.GET.get('fetchcount'):
                    # source contain JSON data from API.
                    source = urllib.request.urlopen('http://127.0.0.1:5000/stats?sortorder=ASC&fetchcount='+request.GET.get('fetchcount')).read()
                else:
                    # source contain JSON data from API.
                    source = urllib.request.urlopen('http://127.0.0.1:5000/stats?sortorder=ASC&fetchcount=ALL').read()
                # converting JSON data to a dictionary.
                list_of_data = json.loads(source)
                return Response({"STATISTICS RESULTS": list_of_data, "message": "STATISTICS DATA", "success": True}, status=status.HTTP_200_OK)
        except Exception as error:
            traceback.print_exc()
            return Response({"message": str(error), "success": False},status=status.HTTP_200_OK)


class Api_count_viewset(viewsets.ViewSet):
    def list(self, request):
        try:
            '''
            The function for all urls hit counts.
            
            Returns:
                API_Hit_Count: A list which contains all the url with total hits.
            '''

            return Response({"RESULTS": API_Hit_Count, "message": "APIS COUNT DATA", "success": True}, status=status.HTTP_200_OK)
        except Exception as error:
            traceback.print_exc()
            return Response({"message": str(error), "success": False},status=status.HTTP_200_OK)


class Ifsc_count_viewset(viewsets.ViewSet):
    def list(self, request):
        try:
            '''
            The function for ifsc urls hit counts.
            
            Returns:
                IFSC_Hit_Count: A list which contains only the ifsc url with total hits.
            '''

            return Response({"RESULTS": IFSC_Hit_Count, "message": "IFSC COUNT DATA", "success": True}, status=status.HTTP_200_OK)
        except Exception as error:
            traceback.print_exc()
            return Response({"message": str(error), "success": False},status=status.HTTP_200_OK)

