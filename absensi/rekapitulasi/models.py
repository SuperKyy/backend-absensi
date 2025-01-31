from django.db import models
from biodata.models import Biodata
from absen.models import Absen
from presensi.models import Presensi
from perizinan.models import Perizinan

class Rekap(models.Model):
    nama=models.ForeignKey(Biodata,on_delete=models.CASCADE)
    absen_id=models.ForeignKey(Absen,on_delete=models.CASCADE)
    presensi_id=models.ForeignKey(Presensi,on_delete=models.CASCADE)
    perizinan_id=models.ForeignKey(Perizinan,on_delete=models.CASCADE)

    def __str__(self):
        return self.nama.nip
