from django.db import models

class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=30)

class Client(models.Model):
    name = models.CharField(max_length=20)
    card_number = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Worker(models.Model):
    name = models.CharField(max_length=20)
    position = models.CharField(max_length=128)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=20)
    extra_price = models.IntegerField(verbose_name='Надбавка стоимости')
    calories = models.IntegerField(verbose_name='Колл-во каллорий')

    def __str__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=128, verbose_name='Наименование блюдо')
    start_price = models.IntegerField(verbose_name='Изначальная стоимость')
    type_of_cuisine = models.CharField(max_length=20, verbose_name='Тип кухни')
    calories = models.IntegerField(verbose_name='Колл-во каллорий')
    dishes = models.ManyToManyField(Ingredient, through='Order')

    def __str__(self):
        return self.name

class Order(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    vegetarian = models.BooleanField(default=False, verbose_name='Вегетарианская')
    food_status = models.CharField(max_length=20)
    final_price = models.IntegerField(default=0)
    order_date_time = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.food} - {self.ingredient} - {self.client} - {self.worker}'

class ProxyOrder(Order):
    class Meta:
        proxy = True
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def vegetarian(self):
        return self.vegetarian
