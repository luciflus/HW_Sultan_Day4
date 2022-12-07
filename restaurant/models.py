from django.db import models

class User(models.Model):
    email = models.EmailField(default=0)
    password = models.CharField(max_length=128, default=0)


    def __str__(self):
        return self.email

    class Meta:
        abstract = True
        ordering = ['name', ]

class Client(User):
    name = models.CharField(max_length=20)
    card_number = models.CharField(max_length=128)

    class Meta(User.Meta):
        pass

    def __str__(self):
        return self.name


class Worker(User):
    name = models.CharField(max_length=20)
    position = models.CharField(max_length=128)

    class Meta:
        ordering = ['name', ]

    def __str__(self):
        return f'{self.name} в должности {self.position}'


class Ingredient(models.Model):
    name = models.CharField(max_length=128)
    extra_price = models.FloatField()

    def __str__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=128)
    start_price = models.FloatField()
    dishes = models.ManyToManyField(Ingredient, related_name='foods', through='Order')

    def __str__(self):
        return self.name

class Order(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    order_date_time = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.food.name} - {self.ingredient.name}'


