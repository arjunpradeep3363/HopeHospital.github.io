from django.shortcuts import render, redirect
from hospapp.models import DepartmentDb,DoctorDb,NurseDb,MedicineDb,StaffLoginDb,PatientDb
from webapp.models import Registrationdb,Contactdb,MedicineCartdb,CheckOutdb,Appointmentdb
from django.contrib import messages
import random
from django.contrib.auth.decorators import login_required


# Create your views here.

def homepage(request):
    data = DepartmentDb.objects.all()
    return render(request, "Home.html",{'data':data})

def aboutpage(request):
    doc = DoctorDb.objects.all()
    data = DepartmentDb.objects.all()
    return render(request, "Aboutpage.html",{'data':data,'doc':doc})

def departmentpage(request):
    data = DepartmentDb.objects.all()
    return render(request, "Department.html", {'data':data})

def singledepartmentpage(request,dataid):
    dep = DepartmentDb.objects.all()
    data = DepartmentDb.objects.get(id=dataid)
    return render(request, "SingleDepartmentpage.html",{'data':data,'dep':dep})

def servicespage(request):
    dep = DepartmentDb.objects.all()
    return render(request, "Servicespage.html",{'dep':dep})

def doctorpage(request):
    data = DoctorDb.objects.all()
    department = DepartmentDb.objects.all()
    return render(request, "Doctorpage.html", {'data':data, 'department':department})
def doctorsinglepage(request,dataid):
    dep = DepartmentDb.objects.all()
    doc = DoctorDb.objects.all()
    data = DoctorDb.objects.get(id=dataid)
    return render(request, "DoctorSinglePage.html", {'data':data,'dep':dep,'doc':doc})



def appointmentpage(request):
    dep = DepartmentDb.objects.all()
    doc = DoctorDb.objects.all()
    return render(request, "Appointmentpage.html",{'dep':dep, 'doc':doc})


def appointmentsave(request):
    if request.method == "POST":
        dn = request.POST.get('depname')
        dna = request.POST.get('dname')
        da = request.POST.get('date')
        ti = request.POST.get('time')
        na = request.POST.get('name')
        ph = request.POST.get('phone')
        mes = request.POST.get('message')
        obj = Appointmentdb(Department_Name=dn,Doctor_Name=dna,Date=da,Time=ti,Name=na,Phone=ph,Message=mes)
        obj.save()
        messages.success(request, "Appointment successful")
        return redirect(appointmentconfirmationpage)




def appointmentconfirmationpage(request):
    dep = DepartmentDb.objects.all()
    return render(request, "AppointmentConfirmationPage.html",{'dep':dep})

def nursepage(request):
    data = NurseDb.objects.all()
    department = DepartmentDb.objects.all()
    return render(request, "NursePage.html", {'data':data, 'department':department})

def singlenursepage(request,dataid):
    dep = DepartmentDb.objects.all()
    data = NurseDb.objects.get(id=dataid)
    return render(request,"SingleNurse.html",{'data':data,'dep':dep})

def medicinepage(request):
    dep = DepartmentDb.objects.all()
    data = MedicineDb.objects.all()
    return render(request, "MedicinePage.html", {'data':data,'dep':dep})

def singlemedicine(request,dataid):
    dep = DepartmentDb.objects.all()
    data = MedicineDb.objects.get(id=dataid)
    return render(request, "SingleMedicine.html",{'data':data, 'dep':dep})

def registerloginpage(request):
    return render(request, "RegisterAndLogin.html")

def registerloginsave(request):
    if request.method == "POST":
        una = request.POST.get('name')
        ema = request.POST.get('email')
        mob = request.POST.get('mobile')
        img = request.FILES['image']
        pawd = request.POST.get('password')
        obj = Registrationdb(User_Name=una, Email=ema, Mobile=mob, Profile_Image=img, Password=pawd)
        obj.save()
        return redirect(registerloginpage)

def userlogin(request):
    if request.method == "POST":
        uname = request.POST.get('uname')
        pwd = request.POST.get('pass')
        if Registrationdb.objects.filter(User_Name=uname, Password=pwd).exists():
            request.session['User_Name'] = uname
            request.session['Password'] = pwd
            messages.success(request, "Login successfully")
            return redirect(homepage)
        else:
            messages.error(request, "Login Error")
            return redirect(registerloginpage)
    return redirect(registerloginpage)

def UserLogout(request):
    del request.session['User_Name']
    del request.session['Password']
    return redirect(registerloginpage)


def contactpage(request):
    dep = DepartmentDb.objects.all()
    return render(request, "ContactPage.html",{'dep':dep})


def savecontactpage(request):
    if request.method == "POST":
        na = request.POST.get('name')
        ema = request.POST.get('email')
        que = request.POST.get('query')
        ph = request.POST.get('phone')
        mes = request.POST.get('message')
        obj = Contactdb(Name=na,Email=ema,Query_Topic=que,Phone=ph,Message=mes)
        obj.save()
        messages.success(request, "Contacted successfully")
        return redirect(contactpage)

def medicinecartpage(request):
    dep = DepartmentDb.objects.all()
    data = MedicineCartdb.objects.filter(User_Name=request.session['User_Name'])
    return render(request, "MedicineCart.html",{'data':data,'dep':dep})

def medicinecartsave(request):
    if request.method == "POST":
        una = request.POST.get('uname')
        mna = request.POST.get('name')
        man = request.POST.get('manuf')
        des = request.POST.get('description')
        prc = request.POST.get('pprice')
        qt = request.POST.get('qty')
        obj = MedicineCartdb(User_Name=una,Medicine_Name=mna,Manufacturer=man,Description=des,Total_Price=prc,Quantity=qt)
        obj.save()
        messages.success(request, "Added to Cart Successfully!!")
        return redirect(checkoutpage)

def deletecart(request, dataid):
    data = MedicineCartdb.objects.filter(id=dataid)
    data.delete()
    return redirect(medicinecartpage)

def checkoutpage(request):
    dep = DepartmentDb.objects.all()
    data = MedicineCartdb.objects.all()
    return render(request, "CheckOut.html",{'data':data,'dep':dep})

def savecheckout(request):
    if request.method == "POST":
        invoice_number = random.randint(10000, 99999)
        x = request.POST.get('nname')
        y = request.POST.get('email')
        a = request.POST.get('add')
        b = request.POST.get('city')
        c = request.POST.get('state')
        d = request.POST.get('pin')
        i = request.POST.get('cname')
        e = request.POST.get('cnum')
        f = request.POST.get('year')
        g = request.POST.get('expm')
        h = request.POST.get('cvv')
        mna = request.POST.get('name')
        prc = request.POST.get('pprice')
        man = request.POST.get('manuf')
        data = MedicineCartdb(Medicine_Name=mna,Manufacturer=man,Total_Price=prc)
        obj = CheckOutdb(Name=x, Email=y, Address=a, City=b, State=c, Pin=d, Cname=i,  Cnum=e, Expyear=f, Expm=g,  Cvv=h)
        obj.save()

        context = {
            'x': x,
            'y': y,
            'a': a,
            'b': b,
            'c': c,
            'd': d,
            'data':data,
            'invoice_number':invoice_number


        }
        messages.success(request, "Purchased Successfully!!")
        return render(request, 'Invoice.html', {'context': context})



def invoicepage(request):
    invoice_number = random.randint(10000, 99999)
    context = {
        'invoice_number': invoice_number
    }
    return render(request, "Invoice.html",context=context, )

def logintopatientdb(request):
    return render(request, "LoginToPatientDb.html")



def stafflogin(request):
    if request.method == "POST":
        uname = request.POST.get('user')
        pwd = request.POST.get('pass')
        if StaffLoginDb.objects.filter(Name=uname, Password=pwd).exists():
            request.session['Name'] = uname
            request.session['Password'] = pwd
            return redirect(patientpage)
        else:
            messages.error(request, "Wrong Credentials or You do not have access to this page")
            return redirect(logintopatientdb)
    return redirect(logintopatientdb)
def stafflogout(request):
    del request.session['Name']
    del request.session['Password']
    return redirect(logintopatientdb)



def patientpage(request):
    data = PatientDb.objects.all()
    return render(request, "PatientsPage.html", {'data':data})





