from fastapi import APIRouter,Depends
import json
from typing import Union
import requests
from fastapi.responses import RedirectResponse

from basemodel import *
from database import ComfirmPolicyfunction,Intercept
from config import Base_URL,Apikey,Authorization,Content_type
import security

router = APIRouter(
    prefix="/MTIPRB",
    tags=["MTIPRB"]
)

@router.post("/CreatePolicy")
def CreatePolicyRedux(PolicyRequest:PolicyRequest,current_user:str = Depends(security.get_current_user)):
  ref = PolicyRequest.Header.ReferenceNo
  ref = "S_"+(ref)
  PolicyRequest.Header.ReferenceNo = ref
  url = "https://api-uat.muangthaiinsurance.com/mobile/CreatePolicy"
  timeExpire =  PolicyRequest.Header.Expire_formated
  PolicyRequest.Header.ExpireDate = timeExpire

  timeEffective = PolicyRequest.Header.EffectiveDate_formated
  PolicyRequest.Header.EffectiveDate = timeEffective
  payload=PolicyRequest.json()
  headers = {
  'apikey': 'vobeAbForuaOyEowS1eEMK6rALiHPqs0',
  'Authorization': 'Bearer VFFNQFRFU1Q6VEVTVCQ3NDAwMDA4Nw==',
  'Content-Type': 'application/json'
  }
  response = requests.request("POST", url, headers=headers, data=payload)
  print(payload)
  print(PolicyRequest)
  datajson = json.loads(response.text)
  return datajson

@router.post("/ConfirmPolicy")
#def ConfirmPolicyRedux(ConfirmRequest:ConfirmRequest,current:str = Depends(security.get_current_user)):
def ConfirmPolicyRedux(ConfirmRequest:ConfirmRequest,current_user:str = Depends(security.get_current_user)):
  url = "https://api-uat.muangthaiinsurance.com/mobile/ConfirmPolicy"
  payload=ConfirmRequest.json()
  #payload = json.dumps(datajson)
  headers = {
  'apikey': 'vobeAbForuaOyEowS1eEMK6rALiHPqs0',
  'Authorization': 'Bearer VFFNQFRFU1Q6VEVTVCQ3NDAwMDA4Nw==',
  'Content-Type': 'application/json'
}
  response = requests.request("POST", url, headers=headers, data=payload)
  print(type(payload))
  print(type(ConfirmRequest))
  datajson = json.loads(response.text)
  return datajson
 
@router.post("/Document")
def Document(DocumentReq: DocumentReq,current_user:str = Depends(security.get_current_user)):
  payload = DocumentReq.json()
  url = "https://api-uat.muangthaiinsurance.com/printservice/prints/PrintDocumentList"
  headers = {
  'apikey': 'vobeAbForuaOyEowS1eEMK6rALiHPqs0',
  'Authorization': 'Bearer VFFNQFRFU1Q6VEVTVCQ3NDAwMDA4Nw==',
  'Content-Type': 'application/json'
  }
  response = requests.request("POST", url, headers=headers, data=payload)
  datajson = json.loads(response.text)
  return datajson

@router.post("/Cancel")
def cancelPRB(cancelReq:CancelReq,current_user:str = Depends(security.get_current_user)):
  payload = cancelReq.json()
  url = "https://api-uat.muangthaiinsurance.com/cancellation/Cancellation/CreateCancellation"
  headers = {
  'apikey': 'vobeAbForuaOyEowS1eEMK6rALiHPqs0',
  'Authorization': 'Bearer VFFNQFRFU1Q6VEVTVCQ3NDAwMDA4Nw==',
  'Content-Type': 'application/json'
  }
  response = requests.request("POST", url, headers=headers, data=payload)
  datajson = json.loads(response.text)
  return datajson

@router.post("/Verify")
def Verify(PolicyRequest:PolicyRequest,current_user:str = Depends(security.get_current_user)):
  ref = PolicyRequest.Header.ReferenceNo
  ref = "L_"+(ref)
  PolicyRequest.Header.ReferenceNo = ref
  
  timeExpire =  PolicyRequest.Header.Expire_formated
  PolicyRequest.Header.ExpireDate = timeExpire

  timeEffective = PolicyRequest.Header.EffectiveDate_formated
  PolicyRequest.Header.EffectiveDate = timeEffective

  payload = PolicyRequest.json()
  url = "https://api-uat.muangthaiinsurance.com/mobile/CreatePolicy"
  headers = {
  'apikey': 'vobeAbForuaOyEowS1eEMK6rALiHPqs0',
  'Authorization': 'Bearer VFFNQFRFU1Q6VEVTVCQ3NDAwMDA4Nw==',
  'Content-Type': 'application/json'
  }
  response = requests.request("POST", url, headers=headers,data=payload)
  result = json.loads(response.text)
  return result

@router.post("/")
def Tryga(PolicyRequest:PolicyRequest):
  ref = PolicyRequest.Header.ReferenceNo
  ref = "L_"+(ref)
  PolicyRequest.Header.ReferenceNo = ref
  paylaod = PolicyRequest.json()
  return paylaod


