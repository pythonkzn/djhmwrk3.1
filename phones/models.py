from django.db import models


class Prod(models.Model):
    brand = models.TextField()
    feature_one = models.TextField()
    feature_two = models.TextField()
    fm_radio = models.TextField(default='-')

    def __str__(self):
        return self.brand + ', ' + self.feature_one + ', ' + self.feature_two + ', ' + self.fm_radio


class Phone(models.Model):
    CHOICE_OS = {
        ('ios','ios'),
        ('windows', 'windows'),
        ('android', 'android')
            }
    name = models.CharField(max_length=50)
    cost = models.CharField(max_length=50)
    op_s = models.CharField(max_length=50, choices=CHOICE_OS)
    prod = models.ForeignKey(Prod, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return 'Модель - {0}, Стоимость - {1}, Операционная система = {2}, Дополнительно = {3}'.format(self.name,
                                                                                                       self.cost,
                                                                                                       self.op_s,
                                                                                                       self.prod)
