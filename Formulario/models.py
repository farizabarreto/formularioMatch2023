from django.db import models

Estados = (
    ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazônia'),
    ('BA', 'Bahia'), ('CE','Ceará'), ('DF', 'Distrito Federal'),('ES', 'Espírito Santo'),
    ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'),
    ('PI','Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantis')
)
class Inscrite(models.Model):
    nome = models.CharField(max_length=60)
    idade = models.IntegerField()
    endereco = models.CharField(max_length=80)
    numero = models.CharField(max_length=5)
    complemento = models.CharField(max_length=30)
    bairro = models.CharField(max_length=40)
    cidade = models.CharField(max_length=30)
    uf = models.CharField(max_length=2, choices=Estados)
    ciencia = models.BooleanField(blank=False, null=False, default=False)

    def __str__(self) -> str:
        return self.nome

