product=Products( title ='shoes' ,pid =102 ,desc ='abc',price =2000,quantity =2,img = '')
product=Products( title ='' ,pid =102 ,desc ='abc',price =2000,quantity =2,img = '')
product=Products( title ='' ,pid =103 ,desc ='qwert',price =3300,quantity =2,img = '')
product = Products.objects.get(pid=102)

from django.db.models import F
product.save()
objs= Products.objects.annotate(total F('price') *F('quantity'))
Products.objects.filter(id=2).update(desc='sports shoe for men',price=5000)

x=Products.objects.filter(id=2)
x.update(quantity =5)

from django.db.models import Q

value = Products.objects.all().count('title')