from restaurant.models import User, Client, Ingredient, Food, Order, Worker, ProxyOrder

user_1 = User.objects.create(email='nikname21@gmail.com', password='defender42')
client = Client.objects.create(name='Нурсултан Бердиев', card_number='4147 5657 9878 9009', user=user_1)
#
user_2 = User.objects.create(email='altywa1998 @ gmail.com', password='nono34')
worker = Worker.objects.create(name='Алтынай Алиева', position='Оператор кассы', user=user_2)
# #
f1 = Food.objects.create(name='Шаурма', start_price=200, type_of_cuisine='фастфуд', calories=500)
f2 = Food.objects.create(name='Гамбургер', start_price=180, type_of_cuisine='фастфуд', calories=350)
f3 = Food.objects.create(name='Паста', start_price=450, type_of_cuisine='Итальянская', calories=400)
f4 = Food.objects.create(name='Суши', start_price=400, type_of_cuisine='Японская', calories=450)
f5 = Food.objects.create(name='Боул', start_price=600, type_of_cuisine='Европейское', calories=500)
# #
i1 = Ingredient.objects.create(name='сыр', extra_price=80, calories=150)
i2 = Ingredient.objects.create(name='курица', extra_price=100, calories=250)
i3 = Ingredient.objects.create(name='говядина', extra_price=120, calories=300)
i4 = Ingredient.objects.create(name='рыба', extra_price=120, calories=270)
i5 = Ingredient.objects.create(name='рис', extra_price=70, calories=100)
i6 = Ingredient.objects.create(name='творог', extra_price=100, calories=170)
i7 = Ingredient.objects.create(name='куриные яйца', extra_price=50, calories=120)
i8 = Ingredient.objects.create(name='салат', extra_price=50, calories=50)
i9 = Ingredient.objects.create(name='фри', extra_price=50, calories=70)

f1.dishes.set([i3, i1, i8, i9], through_defaults={'client': client, 'worker': worker})
f2.dishes.set([i2, i8], through_defaults={'client': client, 'worker': worker})
f3.dishes.set([i8, i7, i1, i6], through_defaults={'client': client, 'worker': worker})
f4.dishes.set([i5, i1, i9, i8, i6], through_defaults={'client': client, 'worker': worker})
f5.dishes.set([i5, i4, i7], through_defaults={'client': client, 'worker': worker})
#
f3.dishes.set([i1, i9], through_defaults={'client': client, 'worker': worker})
f4.dishes.set([i1, i4, i5], through_defaults={'client': client, 'worker': worker})
f1.dishes.set([i1, i3], through_defaults={'client': client, 'worker': worker})
f2.dishes.set([i1, i2], through_defaults={'client': client, 'worker': worker})
f5.dishes.set([i1, i5, i7], through_defaults={'client': client, 'worker': worker})

ingridients = Ingredient.objects.all()
print(ingridients)
#po = ProxyOrder(vegetarian=1, client=client, worker=worker, food=f1, ingredient=i1)
for i in ingridients.iterator():
    if i.name == 'говядина' or i.name == 'курица':
        po = ProxyOrder(vegetarian=1, client=client, worker=worker)
        po.save()

