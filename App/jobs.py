from django.utils import timezone
from .models import LineUpForm, SailedData


def move_sailed_data():
    
    sailed_records = LineUpForm.objects.filter(CurrentStatus="SAILED")
    for record in sailed_records:
        SailedData.objects.create(
            LineUp_Date=record.LineUp_Date,
            Port=record.Port,
            Berth=record.Berth,
            IMO_No=record.IMO_No,
            Slt=record.Slt,
            Vessel=record.Vessel,
            LOA=record.LOA,
            Beam=record.Beam,
            Draft=record.Draft,
            ETA_ATA_Date=record.ETA_ATA_Date,
            ETA_ATA_Time=record.ETA_ATA_Time,
            ETB_ATB_Date=record.ETB_ATB_Date,
            ETB_ATB_Time=record.ETB_ATB_Time,
            ETD_ATD_Date=record.ETD_ATD_Date,
            ETD_ATD_Time=record.ETD_ATD_Time,
            Cargo1=record.Cargo1,
            CargoQty1=record.CargoQty1,
            CargoUnits1=record.CargoUnits1,
            Cargo2=record.Cargo2,
            CargoQty2=record.CargoQty2,
            CargoUnits2=record.CargoUnits2,
            Cargo3=record.Cargo3,
            CargoQty3=record.CargoQty3,
            CargoUnits3=record.CargoUnits3,
            VesselType=record.VesselType,
            Operations=record.Operations,
            Shipper=record.Shipper,
            Receiver=record.Receiver,
            Principal=record.Principal,
            Owner=record.Owner,
            C_F=record.C_F,
            LastPort=record.LastPort,
            NextPort=record.NextPort,
            LoadPort=record.LoadPort,
            DischargePort=record.DischargePort,
            ChartererAgent=record.ChartererAgent,
            OwnersAgent=record.OwnersAgent,
            CurrentStatus=record.CurrentStatus,
            Remarks=record.Remarks,
            CreatedAt=record.CreatedAt,
            UpdatedAt=record.UpdatedAt,
        )
    sailed_records.delete()

            

