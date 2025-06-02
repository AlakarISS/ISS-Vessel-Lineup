from django.db import models
from django.utils import timezone
# import pytz
import uuid

class Users(models.Model):
    FirstName=models.CharField(max_length=40,default="")
    LastName=models.CharField(max_length=40,default="")
    Username=models.CharField(max_length=40,default="")
    EmailId=models.EmailField(max_length=40,default="")
    Password=models.CharField(max_length=128,default="")
    Country=models.CharField(max_length=40,default="")
    Port=models.CharField(max_length=40,default="")
    UserType=models.CharField(max_length=20, default="")
    CombinedField=models.CharField(max_length=80, default="")


class PasswordReset(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    reset_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    created_when = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Password reset for {self.Users.username} at {self.created_when}" 
    

class LineUpForm(models.Model):
    LineUp_Date=models.CharField(max_length=20,default="")
    Port=models.CharField(max_length=20,default="")
    Berth=models.CharField(max_length=20,default="")
    IMO_No=models.CharField(max_length=20,default="")
    Slt=models.CharField(max_length=20,default="")
    Vessel=models.CharField(max_length=20,default="")
    LOA=models.DecimalField(max_digits=20,decimal_places=2)
    Beam=models.DecimalField(max_digits=20,decimal_places=2)
    Draft=models.DecimalField(max_digits=20,decimal_places=2)
    ETA_ATA_Date=models.DateField(null=True, blank=True)
    ETA_ATA_Time=models.TimeField(null=True, blank=True)
    ETB_ATB_Date=models.DateField(null=True, blank=True)
    ETB_ATB_Time=models.TimeField(null=True, blank=True)
    ETD_ATD_Date=models.DateField(null=True, blank=True)
    ETD_ATD_Time=models.TimeField(null=True, blank=True)
    Cargo1=models.CharField(max_length=20,default="")
    CargoQty1=models.DecimalField(max_digits=20,decimal_places=2)
    CargoUnits1=models.CharField(max_length=20,default="")
    Cargo2=models.CharField(max_length=20,default="")
    CargoQty2=models.DecimalField(max_digits=20,decimal_places=2)
    CargoUnits2=models.CharField(max_length=20,default="")
    Cargo3=models.CharField(max_length=20,default="")
    CargoQty3=models.DecimalField(max_digits=20,decimal_places=2)
    CargoUnits3=models.CharField(max_length=20,default="")
    VesselType=models.CharField(max_length=20,default="")
    Operations=models.CharField(max_length=20,default="")
    Shipper=models.CharField(max_length=20,default="")
    Receiver=models.CharField(max_length=20,default="")
    Principal=models.CharField(max_length=20,default="")
    Owner=models.CharField(max_length=20,default="")
    C_F=models.CharField(max_length=20,default="")
    LastPort=models.CharField(max_length=20,default="")
    NextPort=models.CharField(max_length=20,default="")
    LoadPort=models.CharField(max_length=20,default="")
    DischargePort=models.CharField(max_length=20,default="")
    ChartererAgent=models.CharField(max_length=20,default="")
    OwnersAgent=models.CharField(max_length=20,default="")
    CurrentStatus=models.CharField(max_length=20,default="")
    Remarks=models.CharField(max_length=200,default="")
    CreatedAt=models.DateTimeField(auto_now_add=True)
    UpdatedAt=models.DateTimeField(auto_now=True)


class Port_Berth_Form(models.Model):
    Country=models.CharField(max_length=20,default="")
    Port=models.CharField(max_length=20,default="")
    Berth=models.CharField(max_length=20,default="")
    Berth_Type=models.CharField(max_length=20,default="")
    Cargos_Handled_on_Berth=models.CharField(max_length=200,default="")
    Terminal=models.CharField(max_length=20,default="")


class SailedData(models.Model):
    LineUp_Date=models.CharField(max_length=20,default="")
    Port=models.CharField(max_length=20,default="")
    Berth=models.CharField(max_length=20,default="")
    IMO_No=models.CharField(max_length=20,default="")
    Slt=models.CharField(max_length=20,default="")
    Vessel=models.CharField(max_length=20,default="")
    LOA=models.DecimalField(max_digits=20,decimal_places=2)
    Beam=models.DecimalField(max_digits=20,decimal_places=2)
    Draft=models.DecimalField(max_digits=20,decimal_places=2)
    ETA_ATA_Date=models.DateField(null=True, blank=True)
    ETA_ATA_Time=models.TimeField(null=True, blank=True)
    ETB_ATB_Date=models.DateField(null=True, blank=True)
    ETB_ATB_Time=models.TimeField(null=True, blank=True)
    ETD_ATD_Date=models.DateField(null=True, blank=True)
    ETD_ATD_Time=models.TimeField(null=True, blank=True)
    Cargo1=models.CharField(max_length=20,default="")
    CargoQty1=models.DecimalField(max_digits=20,decimal_places=2)
    CargoUnits1=models.CharField(max_length=20,default="")
    Cargo2=models.CharField(max_length=20,default="")
    CargoQty2=models.DecimalField(max_digits=20,decimal_places=2)
    CargoUnits2=models.CharField(max_length=20,default="")
    Cargo3=models.CharField(max_length=20,default="")
    CargoQty3=models.DecimalField(max_digits=20,decimal_places=2)
    CargoUnits3=models.CharField(max_length=20,default="")
    VesselType=models.CharField(max_length=20,default="")
    Operations=models.CharField(max_length=20,default="")
    Shipper=models.CharField(max_length=20,default="")
    Receiver=models.CharField(max_length=20,default="")
    Principal=models.CharField(max_length=20,default="")
    Owner=models.CharField(max_length=20,default="")
    C_F=models.CharField(max_length=20,default="")
    LastPort=models.CharField(max_length=20,default="")
    NextPort=models.CharField(max_length=20,default="")
    LoadPort=models.CharField(max_length=20,default="")
    DischargePort=models.CharField(max_length=20,default="")
    ChartererAgent=models.CharField(max_length=20,default="")
    OwnersAgent=models.CharField(max_length=20,default="")
    CurrentStatus=models.CharField(max_length=20,default="")
    Remarks=models.CharField(max_length=200,default="")    
    CreatedAt=models.DateTimeField(null=True, blank=True)
    UpdatedAt=models.DateTimeField(null=True, blank=True)



