
def generate_auto_id(model):
    last_id = model.objects.order_by('-auto_id').first()
    if last_id:
        return last_id.auto_id + 1
    else:
        return 1

# def save_image(images, creator, updater):
#     for image in images:
#         image = ProductImages.objects.create(
#                                         auto_id =  generate_auto_id,
#                                         creator = creator,
#                                         updater = updater,
#                                         **image
#         )
#         image.save()