from restaurant.models import User, Client, Ingredient, Food, Order, Worker

#user_1 = Client.objects.create(email='nikname21@gmail.com', password='defender42')
# user_1 = Client.objects.filter(email='nikname21@gmail.com', password='defender42')
# user_1 = user_1[0]
# user_1.name='Азат Соколов'
# user_1.card_number='4147 5657 9878 9009'
# user_1.save()

# user_2 = Worker.objects.create(email='altywa1998 @ gmail.com', password='nono34')
# user_2 = Worker.objects.filter(email='altywa1998 @ gmail.com', password='nono34')
# user_2 = user_2[0]
# user_2.name = 'Алтынай Алиева'
# user_2.position = 'Оператор кассы'
# user_2.save()

#f1 = Food.objects.create(name='Шаурма', start_price='50')
#f2 = Food.objects.create(name='Гамбургер', start_price='25')

# i1 = Ingredient.objects.create(name='сыр', extra_price='10')
# i2 = Ingredient.objects.create(name='курица', extra_price='70')
# i3 = Ingredient.objects.create(name='говядина', extra_price='80')
# i4 = Ingredient.objects.create(name='салат', extra_price='15')
# i5 = Ingredient.objects.create(name='фри', extra_price='15')

m1 = Order(client=1, worker=1, food='Шаурма', ingredient='говядина')

ValueError: Cannot assign "'Шаурма'": "Order.food" must be a "Food" instance.
