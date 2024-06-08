from django.shortcuts import render,redirect
from Backend.models import product_db,category_db
from webapp.models import contact_db,login_db,Cart_db
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def homepage(request):
    cat=category_db.objects.all()
    return render(request,"home.html",{'cat':cat})
def aboutpage(request):
    cat = category_db.objects.all()
    return render(request,"about.html",{'cat':cat})
def contactpage(request):
    cat = category_db.objects.all()
    return render(request,"contact.html",{'cat':cat})
def save_contact(request):
    if request.method=="POST":
        na=request.POST.get('name')
        em=request.POST.get('email')
        ph=request.POST.get('phone')
        sub=request.POST.get('subject')
        mes=request.POST.get('message')
        obj=contact_db(Name=na,Email=em,Phone=ph,Subject=sub,Message=mes)
        obj.save()
        return redirect(contactpage)
def ourproduct(request):
    pro=product_db.objects.all()
    cat = category_db.objects.all()
    return render(request,"ourproduct.html",{'pro':pro,'cat':cat})
def product_filter(request,cat_name):
    data=product_db.objects.filter(Category=cat_name)
    return render(request,"product_filtered.html",{'data':data})
def single_page(request,prd_id):
    data=product_db.objects.get(id=prd_id)
    return render(request,"single_prd.html",{'data':data})
def login_pages(request):
    return render(request,"Login.html")
def save_user(request):
    if request.method=="POST":
        em=request.POST.get('email')
        pwd=request.POST.get('pass1')
    obj=login_db(Email=em,Password=pwd)
    if login_db.objects.filter(Email=em).exists():
        messages.warning(request,"Username Already exists..!")
        return redirect(login_pages)
    else:
         obj.save()
         messages.success(request,"Registered Successfully...!")
    return redirect(login_pages)
def user_login(request):
    if request.method=="POST":
        un=request.POST.get('uname')
        pwd=request.POST.get('password')
        if login_db.objects.filter(Email=un,Password=pwd).exists():
            request.session['Email']=un
            request.session['Password']=pwd
            messages.success(request, "Welcome")
            return redirect(homepage)
        else:
            messages.error(request, "Invalid Password")
            return redirect(login_pages)
    else:
        messages.warning(request, "user not found")
        return redirect(login_pages)
def user_logout(request):
    del request.session['Email']
    del request.session['Password']
    messages.success(request, "Logout Successfully")
    return redirect(homepage)

def save_cart(request):
    if request.method=="POST":
        em=request.POST.get('email')
        pn=request.POST.get('pname')
        qn=request.POST.get('qty')
        tp=request.POST.get('tprice')
        obj=Cart_db(Email=em,Product_Name=pn,Quantity=qn,Total_Price=tp)
        obj.save()
        messages.success(request, "Added to Cart")
        return redirect(homepage)
def cart_page(request):
    data=Cart_db.objects.filter(Email=request.session['Email'])
    total=0
    for d in data:
        total=total+d.Total_Price
    return render(request,"cart.html",{'data':data,'total':total})
def delete_item(request,p_id):
    x=Cart_db.objects.filter(id=p_id)
    x.delete()
    messages.success(request,"removed sucessfully")
    return redirect(cart_page)

