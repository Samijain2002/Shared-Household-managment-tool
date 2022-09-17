from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo_list, Water, Tiffin, Maid
from django.urls import reverse_lazy
from . import views

def index(request):
    todo_count = len(Todo_list.objects.all())
    water = Water.objects.all()
    water_cnt = 0
    for i in water:
        water_cnt += i.count
    arr = [0,0,0,0]
    tiffin = Tiffin.objects.all()
    for i in tiffin:
        arr[0] += i.sami
        arr[1] += i.utsi
        arr[2] += i.vanshi
        arr[3] += i.meetu
    maid = Maid.objects.all()
    amt_paid = 0
    for i in maid:
        amt_paid += i.amount
    data = {"water_cnt":water_cnt, "todo_cnt":todo_count, "sami":arr[0],
    "utsi":arr[1], "vanshi":arr[2], "meetu":arr[3], "amt_paid":amt_paid}
    # Create your views here.

    data["tiffin"] = Tiffin.objects.all()
    return render(request, "index.html", data)

def todo_lst(request):
    todo_count = len(Todo_list.objects.all())
    water = Water.objects.all()
    water_cnt = 0
    for i in water:
        water_cnt += i.count
    arr = [0,0,0,0]
    tiffin = Tiffin.objects.all()
    for i in tiffin:
        arr[0] += i.sami
        arr[1] += i.utsi
        arr[2] += i.vanshi
        arr[3] += i.meetu
    maid = Maid.objects.all()
    amt_paid = 0
    for i in maid:
        amt_paid += i.amount
    data = {"water_cnt":water_cnt, "todo_cnt":todo_count, "sami":arr[0],
    "utsi":arr[1], "vanshi":arr[2], "meetu":arr[3], "amt_paid":amt_paid}
    # Create your views here.
    data["todo_lst"] = Todo_list.objects.all()
    return render(request, "todo.html", data)

def maid(request):
    todo_count = len(Todo_list.objects.all())
    water = Water.objects.all()
    water_cnt = 0
    for i in water:
        water_cnt += i.count
    arr = [0,0,0,0]
    tiffin = Tiffin.objects.all()
    for i in tiffin:
        arr[0] += i.sami
        arr[1] += i.utsi
        arr[2] += i.vanshi
        arr[3] += i.meetu
    maid = Maid.objects.all()
    amt_paid = 0
    for i in maid:
        amt_paid += i.amount
    data = {"water_cnt":water_cnt, "todo_cnt":todo_count, "sami":arr[0],
    "utsi":arr[1], "vanshi":arr[2], "meetu":arr[3], "amt_paid":amt_paid}
    # Create your views here.

    data["maid"] = Maid.objects.all()
    return render(request, "maid.html", data)

def water_sup(request):
    todo_count = len(Todo_list.objects.all())
    water = Water.objects.all()
    water_cnt = 0
    for i in water:
        water_cnt += i.count
    arr = [0,0,0,0]
    tiffin = Tiffin.objects.all()
    for i in tiffin:
        arr[0] += i.sami
        arr[1] += i.utsi
        arr[2] += i.vanshi
        arr[3] += i.meetu
    maid = Maid.objects.all()
    amt_paid = 0
    for i in maid:
        amt_paid += i.amount
    data = {"water_cnt":water_cnt, "todo_cnt":todo_count, "sami":arr[0],
    "utsi":arr[1], "vanshi":arr[2], "meetu":arr[3], "amt_paid":amt_paid}
    # Create your views here.

    data["water"] = Water.objects.all()
    return render(request, "water.html", data)


def new_tiffin(request):
    msg = ""
    if request.method == "POST":
        sami = int(request.POST["sami"])
        utsi = int(request.POST["utsi"])
        vanshi = int(request.POST["vanshi"])
        meet = int(request.POST["meet"])
        shift = request.POST.get("shift", None)
        if all ([i == 0 for i in [sami, utsi, vanshi, meet]]):
            msg = "check your inputs"
            return render(request, "new_tiffin.html", {"msgs":msg})
        temp = Tiffin.objects.create(sami = sami, utsi = utsi, vanshi = vanshi, meetu = meet, shift = shift)
        print(temp)
        return redirect(index)
    return render(request, "new_tiffin.html", {"msgs":msg})
    

def delete_tfn(request, id = None):
    if id != None:
        obj = Tiffin.objects.get(id = id)
        obj.delete()
        return redirect(index)
    else:
        return HttpResponse("some eroor")

def delete_all_tfn(request):
    tfn = Tiffin.objects.all()
    for i in tfn: 
        obj = Tiffin.objects.get(id = i.id)
        obj.delete()
    return redirect(index)

def new_task(request):
    msg = ""
    if request.method == "POST":
        title = request.POST["title"]
        desc = request.POST["desc"]
        if title:
            Todo_list.objects.create(title = title, desc = desc)
            return redirect(todo_lst)
        else:
            return render(request, "new_task.html", {"msgs":"Please write a valid title"})
    return render(request, "new_task.html", {"msgs":""})

def delete_task(request, id = None):
    if id != None:
        obj = Todo_list.objects.get(id = id)
        obj.delete()
        return redirect(todo_lst)
    else:
        return HttpResponse("some eroor")

def delete_all_task(request):
    tfn = Todo_list.objects.all()
    for i in tfn: 
        obj = Todo_list.objects.get(id = i.id)
        obj.delete()
    return redirect(todo_lst)
def new_water(request):
    msg = ""
    if request.method == "POST":
        count = request.POST["count"]
        if count:
            Water.objects.create(count = count)
            return redirect(water_sup)
        else:
            return render(request, "new_water.html", {"msgs":"Please write a valid count"})
    return render(request, "new_water.html", {"msgs":""})
def delete_water(request, id = None):
    if id != None:
        obj = Water.objects.get(id = id)
        obj.delete()
        return redirect(water_sup)
    else:
        return HttpResponse("some eroor")

def delete_all_water(request):
    tfn = Water.objects.all()
    for i in tfn: 
        obj = Water.objects.get(id = i.id)
        obj.delete()
    return redirect(water_sup)


def new_maid(request):
    msg = ""
    if request.method == "POST":
        amount = request.POST["amount"]
        if amount:
            Maid.objects.create(amount = amount)
            return redirect(maid)
        else:
            return render(request, "new_maid.html", {"msgs":"Please write a valid count"})
    return render(request, "new_maid.html", {"msgs":""})
    pass

def delete_maid(request, id = None):
    if id != None:
        obj = Maid.objects.get(id = id)
        obj.delete()
        return redirect(maid)
    else:
        return HttpResponse("some eroor")

def delete_all_maid(request):
    tfn = Maid.objects.all()
    for i in tfn: 
        obj = Maid.objects.get(id = i.id)
        obj.delete()
    return redirect(maid)


