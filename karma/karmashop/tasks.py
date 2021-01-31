from celery import shared_task
from django.core.mail import send_mail
from . import models as my_models
from django.contrib.auth.models import User

@shared_task
def background_task(user_id):
    if user_id:
        order_instnce = my_models.Order.objects.filter(user=user_id, is_completed=False).last()
        user_instance = User.objects.filter(pk=user_id).last()
        print(user_instance.email)
        if order_instnce:
            orderitems = order_instnce.orderitem_set.all()
            itmes = ''
            for orderitem in orderitems:
                if orderitem.quantity <= orderitem.product.quantity:
                    product_instace = my_models.Product.objects.filter(pk=orderitem.product.id).last()
                    product_instace.quantity = product_instace.quantity - orderitem.quantity
                    product_instace.save()
                    itmes =  itmes +'' + product_instace.name
                else:
                    message = "item is not Available"
                    print('item not availabel ')
            order_instnce.is_completed = True
            order_instnce.save()
            message = "Hello " + order_instnce.user.first_name + " Your Available Items are " + itmes

            email = send_mail(subject="this is for test purposr",
                      message=message,
                      from_email=user_instance.email,
                      auth_password='Zala@123',
                      recipient_list =["bomix22453@wpsavy.com"],)

            if email :
                print("email has been sent")
                print('Order Successfull')
            else:
                print('unable to send the email')

