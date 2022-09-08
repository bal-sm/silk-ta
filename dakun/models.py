from django.db import models

# Create your models here.

class DebitCredit(models.TextChoices):
    DEBIT = '+', 'Debit'
    KREDIT = '-', 'Kredit'

class Akun(models.Model):
    code_1 = models.PositiveIntegerField(null=True, blank=True)
    code_2 = models.PositiveIntegerField(null=True, blank=True)
    code_3 = models.PositiveIntegerField(null=True, blank=True)
    name = models.CharField( 
        max_length=50)
    description = models.TextField( 
        blank=True)
    debit_credit = models.CharField(
        max_length=1, 
        choices=DebitCredit.choices,
        blank=True) # + = debit, - = credit
    koperasi_type = models.ManyToManyField('dkoperasi.Type', blank=True)
    is_enabled = models.BooleanField(default=True)

    class Meta:
        ordering = ['code_1', 'code_2', 'code_3']
    
    def __str__(self):
        return f'{self.code_1}.{self.code_2}.{self.code_3} {self.name} ({self.debit_credit}, {self.is_enabled})' 

    def namanya(self):
        return f'{self.code_1}.{self.code_2}.{self.code_3} {self.name}'

    def nama_kotor(self):
        return f'{self.code_1}.{self.code_2}.{self.code_3} {self.name} ({self.debit_credit})' 

    def deskripsinya(self):
        return f'{self.description}'

    def namanya1(self):
        return f'{self.code_1} {self.name}'

    def namanya2(self):
        return f'{self.code_1}.{self.code_2} {self.name}'

    def namanya3(self):
        return f'{self.code_1}.{self.code_2}.{self.code_3} {self.name}'

    def namanyaaja(self):
        return f'{self.name}'

    def nomornya1(self):
        return f'{self.code_1}'

    def nomornya2(self):
        return f'{self.code_1}.{self.code_2}'

    def nomornya3(self):
        return f'{self.code_1}.{self.code_2}.{self.code_3}'

    def namanyaupper(self):
        return f'{self.name.upper()}'
# -----------------------------------

#DEBIT = '+'
#KREDIT = '-'
#DEBIT_ATAU_KREDIT = [
#    (DEBIT, 'Debit'),
#    (KREDIT, 'Kredit'),
#]

#class Info_Sering(models.Model):
#    Nama = models.CharField( 
#        max_length=50)
#    Deskripsi = models.TextField( 
#        blank=True)
    
#    class Meta:
#        abstract = True

''' ----------------------------------- ants(draft)


--------------------------------------------- '''
