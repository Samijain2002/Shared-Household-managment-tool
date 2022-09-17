from django.urls import path,include
from . import views
urlpatterns = [
    path("", views.index, name = "index"),
    path("todo", views.todo_lst, name = "todolist"),
    path("maid", views.maid, name = "maid"),
    path("water", views.water_sup, name = "water_supply"),
    
    path("new_tiffin", views.new_tiffin, name="new_tifiin"),
    path("dlt/<id>/", views.delete_tfn, name="delete_tfn"),
    path("dlt_all_tfn", views.delete_all_tfn, name="delete_all_tfn"),

    path("new_task", views.new_task, name = "new_task"),
    path("dlt_task/<id>/", views.delete_task, name="delete_task"),
    path("dlt_all_task", views.delete_all_task, name="delete_all_task"),

    path("new_water", views.new_water, name = "new_water"),
    path("dlt_water/<id>/", views.delete_water, name="delete_water"),
    path("dlt_all_water", views.delete_all_water, name="delete_all_water"),

    path("new_maid", views.new_maid, name = "new_maid"),
    path("dlt_maid/<id>/", views.delete_maid, name="delete_maid"),
    path("dlt_all_maid", views.delete_all_maid, name="delete_all_maid"),
    

]
