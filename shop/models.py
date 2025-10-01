from django.db import models


class User(models.Model):
    first_name = models.CharField("Имя пользователя", max_length=20)
    last_name = models.CharField("Фамилия", max_length=25)
    email = models.EmailField("Почта")
    phone = models.CharField("Номер", max_length=20)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["first_name", "last_name"]
        indexes = [
            models.Index(fields=["first_name"])
        ]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Meta(models.Model):
    ST = [
        ("Оформлен", "Оформлен"),
        ("Отправлен", "Отправлен"),
        ("Доставлен", "Доставлен")
    ]

    PM = [
        ("Банковская карта", "Банковская карта"),
        ("При получении", "При получении")
    ]


    id_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    status = models.CharField("Статус заказа", max_length=100, choices=ST)
    price = models.DecimalField("Цена", )


    

