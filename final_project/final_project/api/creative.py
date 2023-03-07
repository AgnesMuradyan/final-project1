# import json

# from django.core.exceptions import ObjectDoesNotExist
# from django.views.generic import View
# from final_project.game.models import Category
# from .helper_functions import *


# class CategoryView(View):

#     def get(self, request):
#         categories = Category.objects.all()
#         data = []
#         for category in categories:
#             data.append(({'code': category.code, 'name': category.name}))
#         return data_status(data)

#     def post(self, request):
#         data = json.loads(request.body)
#         if 'code' in data and 'name' in data:
#             category = Category.objects.create(
#                 code=Category.objects.get(pk=data['pk']),
#                 name=data['name']
#             )
#         else:
#             return failed_status("invalid_post_data")
#         category.save()
#         return ok_status()

#     @staticmethod
#     def check_view(request, id):
#         if request.method == "GET":
#             return CategoryView.get_single(request, id)
#         if request.method == "DELETE":
#             return CategoryView.delete(request, id)
#         # if request.method == "PATCH":
#         #     return edit(request, id)

#     @staticmethod
#     def get_single(request, id):
#         try:
#             category = Category.objects.get(id=id)
#         except ObjectDoesNotExist:
#             return failed_status("object_not_found")
#         return data_status(
#             {"code": category.code,"name":category.name})

#     @staticmethod
#     def delete(request, id):
#         try:
#             category = Category.objects.get(id=id)
#         except ObjectDoesNotExist:
#             return failed_status("object_not_found")
#         category.delete()
#         return ok_status()

#     # @staticmethod
#     # def edit(request, ID):
#     #     data = json.loads(request.body)
#     #     try:
#     #         customer = Customer.objects.get(id=ID)
#     #     except ObjectDoesNotExist:
#     #         return CategoryView.failed_status("obj_not_found")
#     #     if "id" in data:
#     #         customer.user = User.objects.get(id=data["id"])
#     #     if "avatar" in data:
#     #         customer.avatar = data["avatar"]
#     #     customer.save()
#     #     return CategoryView.ok_status()
