from django.test import TransactionTestCase
from core.models import *
from orders.models import * 
from products.models import *

class ModelsTest(TransactionTestCase):
    def setUp(self):
        self.user = User.objects.create(full_name="test",phone_number="0912",email="test@gmail.com")
        self.address = Address.objects.create(location='test',user=self.user)
        self.category = Category.objects.create(name='test')
        self.product = Product(code=1,category=self.category,name='test',description='test',price=1)
        self.orderitem =OrderItem(product=self.product,count=3)
        self.order = Order(user=self.user)
        

    
    def test_full_name(self):
        full_name = self.user.full_name
        print(full_name)
        self.assertEquals(full_name, 'test')

    def test_email(self):
        email = self.user.email
        self.assertEquals(email, 'test@gmail.com')

    def test_phone_number(self):
        phone_number = self.user.phone_number
        self.assertEquals(phone_number, '0912')

    def test_address_location(self):
        location= self.address.location
        self.assertEquals(location, 'test')

    def test_address_user(self):
        user= self.address.user
        self.assertEquals(user, self.user)
    
    def test_isstaff_user(self):
        status = self.user.is_staff
        self.assertEquals(status, False)

    def test_isstaff_user(self):
        status = self.user.is_superuser
        self.assertEquals(status, False)

    def test_isstaff_user(self):
        status = self.user.is_active
        self.assertEquals(status, True)

    def test_category_name(self):
        name = self.category.name
        self.assertEqual(name, 'test')

    def test_product_name(self):
        name = self.product.name
        self.assertEqual(name, 'test')

    def test_product_category(self):
        category = self.product.category
        self.assertEqual(category, self.category)
    
    def test_product_code(self):
        code = self.product.code
        self.assertEqual(code, 1)

    def test_product_description(self):
        description= self.product.description
        self.assertEqual(description, "test")

    def test_product_available(self):
        available= self.product.available
        self.assertEqual(available, True)

    def test_orderitem_product(self):
        product= self.orderitem.product
        self.assertEqual(product, self.product)

    def test_orderitem_count(self):
        count= self.orderitem.count
        self.assertEqual(count, 3)

    def test_orderitem_price(self):
        price = self.orderitem.price
        self.assertEqual(price, 3)

    
    def test_order_user(self):
        user = self.order.user
        self.assertEqual(user, self.user)

