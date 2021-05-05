from django.contrib.auth import get_user_model
from django.db import models


class Person(models.Model):
    """Пользователи. Дополнительные сведения"""
    # name = models.CharField(verbose_name="Полное имя", max_length=100)
    first_name = models.CharField('Имя', max_length=100)
    last_name = models.CharField('Фамилия', max_length=100)
    user = models.ForeignKey(
        get_user_model(), null=True, on_delete=models.CASCADE)
    birth_date = models.DateField('День рождения')

    @property
    def name(self):
        """
        Сгенерировать новое значение.
        Не получиться упорядочить его через - order_by
        """
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'


class Customers(models.Model):
    """Клиенты"""
    name = models.CharField(
        verbose_name='Имя', max_length=50, null=False, blank=False)
    last_name = models.CharField(
        verbose_name='Фамилия', max_length=50, null=False, blank=False)
    description = models.TextField(verbose_name='Описание', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
