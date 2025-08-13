from pydantic import BaseModel , validator,Field
from datetime import date,datetime
from decimal import Decimal
from typing import List

######## CreatePolicy ########
class Header(BaseModel):
    ReferenceNo: str
    AgentCode : str
    ProductCode :str | None = None
    Campaign   : str | None = None
    PartnerCode : str
    PolicyStatus : str 
    PreviousPolicyNumber : str
    Package : str
    EffectiveDate : date
    ExpireDate : date
    SumInsured : Decimal 
    Premium : Decimal 
    StampDuty : Decimal 
    VAT : Decimal 
    TotalPremium : Decimal = Field(max_digits=18, decimal_places=2) 
    DeliveryType : str
    DeliveryNameAddress : str
    ReceiptNameAddress : str
    Coverage : str
    Driver :str
    Accesseries : str
    SaleDate : str | None = None
    SaleID : str | Decimal|None = None
    Salechannel :str | None = None
    TransactionType :str
    MarryUniqueKey :str | None = None
    Consent :str
    Beneficiary :str
    ApplNo :str
    CarInspectionFlag :str
    
    @property
    def Expire_formated(self):
        return self.ExpireDate.strftime("%d/%m/%Y")
    
    @property
    def EffectiveDate_formated(self):
        return self.EffectiveDate.strftime("%d/%m/%Y")
    
    
    
    @validator("ExpireDate",pre=True)
    def parse_Expiredate(cls, value):
        if isinstance(value, str):
            try:
                # แปลงจากรูปแบบ DD/MM/YYYY เป็น date object
                return datetime.strptime(value, "%d/%m/%Y").date()     
            except ValueError:
                raise ValueError("Invalid date format. Expected DD/MM/YYYY.")
        return value
        
    @validator("EffectiveDate", pre= True)
    def parse_Effectivedate(cls, value):
        if isinstance(value, str):
            try:
                # แปลงจากรูปแบบ DD/MM/YYYY เป็น date object
                return datetime.strptime(value, "%d/%m/%Y").date()
            except ValueError:
                raise ValueError("Invalid date format. Expected DD/MM/YYYY.")
        return value
    
class Insured (BaseModel):
    InsuredType:str
    TitleName:str
    Name:str = Field(min_length=0, max_length=60)
    Surname:str = Field(min_length=0, max_length=50)
    Gender:str
    IdNo:str
    BirthDate:str
    Nationality:str
    Occupation:str | None = None
    AddressNo:str = Field(min_length=0, max_length=50)
    Moo:str  | None = None 
    Mooban:str | None = None
    Building:str | None = None
    Soi:str | None = None
    Road:str | None = None
    Tumbol:str = Field(min_length=0, max_length=50)
    Ampur:str = Field(min_length=0, max_length=50)
    Province:str = Field(min_length=0, max_length=50)
    ZipCode:str 
    FullAddress:str = Field(min_length=0, max_length=250)
    MobilePhone:str
    HomePhone:str | None = None
    OfficePhone:str | None = None
    EmailAddress:str = Field(min_length=0, max_length=100)
    BranchCode:str
    BranchName  :str = Field(min_length=0, max_length=250)

class Receipt(BaseModel):
    InsuredType :str
    TitleName :str
    Name :str  = Field(min_length=0, max_length=60)
    Surname :str = Field(min_length=0, max_length=60)
    Gender :str | None = None
    MaritalStatus :str | None = None
    IdNo :str
    Nationality :str
    AddressNo :str  = Field(min_length=0, max_length=50)
    Moo :str | None = None
    Mooban :str | None = None
    Building :str | None = None
    Soi :str | None = None
    Road :str | None = None
    Tumbol :str = Field(min_length=0, max_length=50)
    Ampur :str = Field(min_length=0, max_length=50)
    Province :str = Field(min_length=0, max_length=50)
    ZipCode :str = Field(min_length=0, max_length=50)
    FullAddress :str = Field(min_length=0, max_length=250)
    BranchCode :str
    BranchName :str

class DeliveryNameAddress(BaseModel):
    TitleName :str
    Name :str = Field(min_length=0, max_length=60)
    Surname :str = Field(min_length=0, max_length=60)
    AddressNo :str  = Field(min_length=0, max_length=50)
    Moo :str | None = None
    Mooban :str | None = None
    Building :str | None = None
    Soi :str | None = None
    Road :str | None = None
    Tumbol :str = Field(min_length=0, max_length=50)
    Ampur :str = Field(min_length=0, max_length=50)
    Province :str = Field(min_length=0, max_length=50)
    ZipCode :str
    EmailAddress :str | None = Field(None,min_length=0, max_length=100)

class MotorDetail(BaseModel):
    Brand :str
    Model :str
    Seats :Decimal
    Size :Decimal  = Field(max_digits=10, decimal_places=2)
    Weigth :Decimal | None = None 
    Chassis :str
    Engine :str | None = None
    Registration :str
    RegistrationProvince :str = Field(min_length=0, max_length=50)
    ManufactureYear :Decimal
    PolicyType :str
    VehicleCode :str
    WorkShop :str
    Body :str | None  = Field(None,min_length=0, max_length=100)
    Camera :str | None = None
    Mile :Decimal | None = None
    MileCoverage :Decimal | None = None
    Color :str 

class Driver (BaseModel):
    SeqNo :Decimal
    TitleName :str 
    Name :str
    Surname :str
    Gender :str
    IdNo :str | None = None
    Nationality :str | None = None
    BirthDate :str | None = None
    LicenseNo :str

class Benefit(BaseModel):
    SeqNo :Decimal
    TitleName :str
    Name :str
    Surname :str
    Relation :str
    
class Coverage(BaseModel):
    CoverageItem :str
    SumInsuredPerPerson :Decimal
    SumInsuredPerAccident :Decimal
    Premium :Decimal

class Consent(BaseModel):
    SeqNo :Decimal 
    ConsentType :str
    ConsentFlag :str

class PolicyRequest(BaseModel):
    Header:Header
    Insured:Insured
    Receipt:Receipt
    DeliveryNameAddress:DeliveryNameAddress
    MotorDetail:List[MotorDetail]    
    driver:Driver | None = None
    benefit:Benefit | None = None
    coverage:Coverage | None = None
    consent:Consent | None = None

######## ConfirmPolicy ########
class ConfirmRequest(BaseModel):
    ReferenceNo : str
    PartnerCode : str
    PaymentRefNo : str
    proposalID : str
 
class DocumentReq(BaseModel):
    ReferenceNo : str
    PolicyNo: str
    
class CancelReq(BaseModel):
    referenceNo: str
    partnerCode: str
    agentNo: str
    policyNo: str  
    cancelType: str
    notificationDate: str
    cancelDate: str
    effectiveDate: str
    expireDate: str
    premiunm: Decimal| None = None
    stampDuty:Decimal| None = None
    vat:Decimal| None = None
    totalPremiunm:Decimal| None = None
    PaymentRefNo: str | None = None
    proposalID: str| None = None
    remark: str
    systemName:str 
    systemCallerName: str