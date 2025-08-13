#import cx_Oracle
import oracledb
from datetime import timedelta, datetime
import json
from config import Apikey,Authorization,Content_type
import requests

def Intercept (dict_Origin):
    return dict_Origin
def ComfirmPolicyfunction(Confirm_dict,result_dict,SaleID):        
    """
    cursor = conn.cursor()
    sql = "ReferenceNo,PartnerCode"
    cursor.execute(sql,{"Saleid":SaleID})
    paint = cursor.fetchone()


    if paint:
        casva = [color[0] for color in cursor.description]
        studio = {str(key):value for value,key in zip(casva,paint)}
    else:
        studio = None
    """
    Result_spite = result_dict['Result']
    mapping ={
        "ReferenceNo": "ReferenceNo",
        "PartnerCode": "PartnerCode",
        "PaymentRefNo": "PaymentRefNo",
        "proposalID": "proposalID"
    }
  
    for Confirm_key,result_key in mapping.items():
        if result_key in Result_spite:
            Confirm_dict[Confirm_key]=Result_spite[result_key]
        else:
            print(f"Key '{result_key}' not found in result_dict and key in Confirm_dict'{Confirm_key}'")
    
    #Testing Full Opiton
    Confirm_dict['ReferenceNo'] = "999999915"
    Confirm_dict['PartnerCode'] = "TQM"
    
    return Confirm_dict

