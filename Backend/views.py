from django.shortcuts import render,redirect
from Backend.models import category_db,product_db
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from webapp.models import contact_db
from django.contrib import messages

# Create your views here.
def index_page(request):
    return render(request,"index.html")
def category_page(request):
    return render(request,"category.html")
def save_category(request):
    if request.method=="POST":
        cn=request.POST.get('categoryname')
        dis=request.POST.get('description')
        img=request.FILES['image']
        obj=category_db(Category_Name=cn,Description=dis,Category_Image=img)
        obj.save()
        messages.success(request,"Category Saved Successfully")
        return redirect(category_page)
def display_category(request):
    data=category_db.objects.all()
    return render(request,"display_category.html",{'data':data})
def edit_category(request,ctg_id):
    data=category_db.objects.get(id=ctg_id)
    return render(request,"edit_category.html",{'data':data})
def update_category(request,ctg_id):
    if request.method=="POST":
        cn= request.POST.get('categoryname')
        dis= request.POST.get('description')
    try:
        img=request.FILES['image']
        fs=FileSystemStorage()
        file=fs.save(img.name, img)
    except MultiValueDictKeyError:
        file=category_db.objects.get(id=ctg_id).Category_Image
    category_db.objects.filter(id=ctg_id).update(Category_Name=cn,Description=dis,Category_Image=img)
    messages.success(request,"Updated Successfully")
    return redirect(display_category)
def delete_category(request,ctg_id):
    x=category_db.objects.filter(id=ctg_id)
    x.delete()
    messages.error(request,"Category Deleted Successfully")
    return redirect(display_category)
def login_page(request):
    return render(request,"admin_login.html")
def admin_login(request):
    if request.method=="POST":
        un = request.POST.get('username')
        pwd = request.POST.get('pass')
        if User.objects.filter(username__contains=un).exists():
            x = authenticate(username=un, password=pwd)
            if x is not None:
              login(request, x)
              request.session['username']=un
              request.session['password']=pwd
              messages.success(request,"Welcome")
              return redirect(index_page)
        else:
            messages.error(request,"Invalid Password")
            return redirect(login_page)
    else:
        messages.warning(request,"user not found")
        return redirect(login_page)
def admin_logout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request,"Logout Successfully")
    return redirect(login_page)
def product_page(request):
    cat=category_db.objects.all()
    return render(request,"Products.html",{'cat':cat})
def save_product(request):
    if request.method=="POST":
        cn=request.POST.get('cname')
        pn=request.POST.get('pname')
        pr=request.POST.get('price')
        dis=request.POST.get('description')
        img=request.FILES['pimage']
        obj=product_db(Category=cn,Product_Name=pn,Price=pr,Description=dis,Product_Image=img)
        obj.save()
        messages.success(request,"Product Saved Successfully")
        return redirect(product_page)
def display_product(request):
    data=product_db.objects.all()
    return render(request,"display_product.html",{'data':data})
def edit_product(request,pro_id):
    pro=product_db.objects.get(id=pro_id)
    cat=category_db.objects.all()
    return render(request,"edit_product.html",{'pro':pro,'cat':cat})
def update_product(request,pro_id):
    if request.method=="POST":
        cn = request.POST.get('cname')
        pn = request.POST.get('pname')
        pr = request.POST.get('price')
        dis = request.POST.get('description')
    try:
        img = request.FILES['pimage']
        fs = FileSystemStorage()
        file = fs.save(img.name, img)
    except MultiValueDictKeyError:
        file = category_db.objects.get(id=pro_id).Product_Image
    product_db.objects.filter(id=pro_id).update(Category=cn,Product_Name=pn,Price=pr,Description=dis,Product_Image=img)
    messages.success(request,"Updated Successfully")
    return redirect(display_product)
def delete_product(request,pro_id):
    x=product_db.objects.filter(id=pro_id)
    x.delete()
    messages.error(request,"Product Deleted Successfully")
    return redirect(display_product)
def contact_details(request):
    data=contact_db.objects.all()
    return render(request,"contact_details.html",{'data':data})
def delete_contact(request,cnt_id):
    x=contact_db.objects.filter(id=cnt_id)
    x.delete()
    return redirect(contact_details)
