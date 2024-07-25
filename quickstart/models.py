from django.db import models

class AttributeName(models.Model):
    id = models.IntegerField(primary_key=True)
    nazev = models.TextField()
    kod = models.TextField(null=True)
    zobrazit = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.id}, {self.nazev}, {self.kod}, {self.zobrazit}"
    
    def merge(self, new: dict):
        return AttributeName(**{
            "id": self.id,
            "nazev": self.nazev,
            "kod": self.kod,
            "zobrazit": self.zobrazit,
            **new 
        })
        

class AttributeValue(models.Model):
    id = models.IntegerField(primary_key=True)
    hodnota = models.TextField()

    def merge(self, new: dict):
        return AttributeValue(**{
            "id": self.id,
            "hodnota": self.hodnota,
            **new 
        })

class Attribute(models.Model):
    id = models.IntegerField(primary_key=True)
    nazev_atributu_id = models.ForeignKey(AttributeName, on_delete=models.CASCADE)
    hodnota_atributu_id = models.ForeignKey(AttributeValue, on_delete=models.CASCADE)

    def merge(self, new: dict):
        return Attribute(**{
            "id": self.id,
            "nazev_atributu_id": self.nazev_atributu_id,
            "hodnota_atributu_id": self.hodnota_atributu_id,
            **new 
        })

class Image(models.Model):
    id = models.IntegerField(primary_key=True)
    obrazek = models.TextField()
    nazev = models.TextField(null=True)

    def merge(self, new: dict):
        return Image(**{
            "id": self.id,
            "obrazek": self.obrazek,
            "nazev": self.nazev,
            **new 
        })
    
    def __str__(self) -> str:
        return f"{self.obrazek}, {self.nazev}"

class Product(models.Model):
    id              = models.IntegerField(primary_key=True)
    nazev           = models.TextField(null=True)
    description     = models.TextField(null=True)
    cena            = models.TextField(null=True)
    mena            = models.TextField(null=True)
    published_on    = models.DateTimeField(null=True)
    is_published    = models.BooleanField(default=False)
    attributes      = models.ManyToManyField(Attribute, through="ProductAttributes")
    images          = models.ManyToManyField(Image, through="ProductImage")

    def merge(self, new: dict):
        return Product(**{
            "id":self.id,
            "nazev":self.nazev,
            "description":self.description,
            "cena":self.cena,
            "mena":self.mena,
            "published_on":self.published_on,
            "is_published":self.is_published,
            "attributes":self.attributes,
            "images":self.images,
            **new
        })
    
    def __str__(self) -> str:
        return f"{self.id}, {self.nazev}, {self.images}"

class ProductAttributes(models.Model):
    id = models.IntegerField(primary_key=True)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def merge(self, new: dict):
        return ProductAttributes(**{
            "id": self.id,
            "attribute": self.attribute,
            "product": self.product,
            **new
        })


class ProductImage(models.Model):
    id = models.IntegerField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    obrazek_id = models.ForeignKey(Image, on_delete=models.CASCADE, null=False)
    nazev = models.TextField(null=True)

    def merge(self, new: dict):
        return ProductImage(**{
            "id": self.id,
            "obrazek_id": self.obrazek_id,
            "product": self.product,
            "nazev": self.nazev,
            **new
        })
    
    def __str__(self) -> str:
        return f"{self.id}, {self.obrazek_id}, {self.nazev}"

class Catalog(models.Model):
    id = models.IntegerField(primary_key=True)
    nazev = models.TextField(null=True)
    obrazek_id = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True)
    products_ids = models.ManyToManyField(Product)
    attributes_ids = models.ManyToManyField(Attribute)

    def merge(self, new: dict):
        return Catalog(**{
            "id": self.id,
            "obrazek_id": self.obrazek_id,
            "products_ids": self.products_ids,
            "nazev": self.nazev,
            "attributes_ids": self.attributes_ids,
            **new
        })