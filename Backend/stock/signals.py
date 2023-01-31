from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Product, Purchases, Sales


@receiver(post_save, sender=Purchases)
def increase_product_stock(sender, instance, created, **kwargs):
    if created:
        quantity=instance.quantity
        prd_id = instance.product.id
        current_product=Product.objects.filter(id=prd_id)
        #print(current_product.stock)
        Product.objects.filter(id=prd_id).update(stock=current_product[0].stock+quantity)



        
        

