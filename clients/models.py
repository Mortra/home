from django.db import models
from django.contrib.auth.models import User

#Создание моделя
class Client(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.SET_NULL, null=True, blank=True, related_name="client")
    name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=20, null=True)
    contacts = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name="Является активным покупателем")
    bottles = models.IntegerField(default=1)
    photo = models.ImageField(
        verbose_name="Фото",
        upload_to='photos',
        null=True,
        blank=True
    )
    def get_absolute_url(self):
        return f"/clients/{self.id}"



#Создание моделя
class Order(models.Model):

    client = models.ForeignKey(
        to=Client, null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name="order"
    )
    #поля врмени создании заказа
    created_at = models.DateTimeField(
        verbose_name="Дата и время создание заказа",
        auto_now_add=True,
    )
    #поля изменении заказа может только админ
    update_at = models.DateTimeField(
        verbose_name="Дата и время изменения заказа",
        auto_now=True,
    )
    #Описание
    name = models.CharField(max_length=255)
    contacts = models.CharField(max_length=255)
    descriptions = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True)
    finished = models.BooleanField(default=False)

    #Возвращает имя заказчика и контакты
    def __str__(self):
        return f"{self.name} - {self.contacts}"



    class Meta:
        #кнопка добавить заказ
        verbose_name = "Заказ"
        #кнопка заказы
        verbose_name_plural = "Заказы"
