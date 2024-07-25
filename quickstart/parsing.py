
import quickstart.models as models


def parseData(data):
    attributeValues: dict[int, models.AttributeValue] = {}
    attributeNames: dict[int, models.AttributeName] = {}
    attributes: dict[int, models.Attribute] = {}
    products: dict[int, models.Product] = {}
    images: dict[int, models.Image] = {}
    if type(data) == list:
        for i in data:
            if type(i) == dict:
                key = list(i.keys())[0]
                print(key)
                if key == None:
                    return
                if type(val := i.get(key)) == dict:
                    match key:
                        case "AttributeName":
                            if (id := val.get('id')) != None:
                                obj, created = models.AttributeName.objects.update_or_create(id=id, defaults=val)
                                attributeNames[obj.id] = obj
                        case "AttributeValue":
                            if (id := val.get('id')) != None:
                                obj, created = models.AttributeValue.objects.update_or_create(id=id, defaults=val)
                                attributeValues[obj.id] = obj
                        case "Attribute":
                            if (id := val.get('id')) != None and (name := val.get('nazev_atributu_id')) != None and (value := val.get('hodnota_atributu_id')) != None:
                                if (name := attributeNames.get(name)) != None and (value := attributeValues.get(value)) != None:
                                    obj, created = models.Attribute.objects.update_or_create(
                                        id=id,
                                        nazev_atributu_id=name,
                                        hodnota_atributu_id=value)
                                    attributes[obj.id] = obj
                        case "Product":
                            if (id := val.get('id')) != None:
                                obj, created = models.Product.objects.update_or_create(id=id, defaults=val)
                                products[obj.id] = obj
                        case "ProductAttributes":
                            if (id := val.get('id')) != None and (product := val.get('product')) != None and (attribute := val.get('attribute')) != None:
                                if (product := products.get(product)) != None and (attribute := attributes.get(attribute)) != None:
                                    obj, created = models.ProductAttributes.objects.update_or_create(
                                        id=id,
                                        product=product,
                                        attribute=attribute
                                    )
                        case "Image":
                            if (id := val.get('id')) != None:
                                obj, created = models.Image.objects.update_or_create(id=id, defaults=val)
                                images[obj.id] = obj
                        case "ProductImage":
                            if (id := val.get('id')) != None and (product := val.get('product')) != None and (image := val.get('obrazek_id')) != None:
                                if (product := products.get(product)) != None and (image := images.get(image)) != None:
                                    del val['product']
                                    del val['obrazek_id']
                                    obj, created = models.ProductImage.objects.update_or_create(id=id, product=product, obrazek_id=image, defaults=val)
                        case "Catalog":
                            if (id := val.get('id')) != None:
                                if (image := val.get('obrazek_id')) != None:
                                    val['obrazek_id'] = images.get(image)
                                if (products_l := val.get('products_ids')) != None:
                                    products_l = [products.get(i) for i in products_l]
                                    del val['products_ids']
                                if (attributes_l := val.get('attributes_ids')) != None:
                                    attributes_l = [attributes.get(i) for i in attributes_l]
                                    del val['attributes_ids']

                                obj, created = models.Catalog.objects.update_or_create(id=id, defaults=val)
                                if products_l != None:
                                    obj.products_ids.set(products_l)
                                if attributes_l != None:
                                    obj.attributes_ids.set(attributes_l)
                        case _:
                            pass


# def setWanted(target: dict, new, newD: dict):
#     if (l := target.get(new.id)) == None:
#         target[new.id] = new
#     else:
#         target[new.id] = l.merge(newD)