# from decimal import Decimal
#
# from tifa.models.channel import ProductVariantChannelListing
# from tifa.models.product import ProductVariant, Product, ProductType
#
#
# def test_filtering_by_attribute(
#         adal,
#         color_attribute,
#         # size_attribute,
#         category,
#         # date_attribute,
#         # date_time_attribute,
#         # boolean_attribute,
# ):
#     product_type_a = ProductType.objects.create(
#         name="New class", slug="new-class1", has_variants=True
#     )
#     product_type_a.product_attributes.add(color_attribute)
#     product_type_b = ProductType.objects.create(
#         name="New class", slug="new-class2", has_variants=True
#     )
#     product_type_b.variant_attributes.add(color_attribute)
#     product_a = Product.objects.create(
#         name="Test product a",
#         slug="test-product-a",
#         product_type=product_type_a,
#         category=category,
#     )
#     variant_a = ProductVariant.objects.create(product=product_a, sku="1234")
#     # ProductVariantChannelListing.objects.create(
#     #     variant=variant_a,
#     #     channel=channel_USD,
#     #     cost_price_amount=Decimal(1),
#     #     price_amount=Decimal(10),
#     #     currency=channel_USD.currency_code,
#     # )
#     # product_b = Product.objects.create(
#     #     name="Test product b",
#     #     slug="test-product-b",
#     #     product_type=product_type_b,
#     #     category=category,
#     # )
#     # variant_b = ProductVariant.objects.create(product=product_b, sku="12345")
