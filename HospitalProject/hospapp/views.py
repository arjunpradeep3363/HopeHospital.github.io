from django.shortcuts import render, redirect
from hospapp.models import DoctorDb,NurseDb,DepartmentDb,PatientDb,MedicineDb,StaffLoginDb
from webapp.models import Contactdb,Appointmentdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages

# Create your views here.


def indexpage(request):
    return render(request, "index.html")

def adddoctor(request):
    data = DepartmentDb.objects.all()
    return render(request, "AddDoctorDetails.html",{'data':data})

def doctorsave(request):
    if request.method == "POST":
        na = request.POST.get('name')
        spl = request.POST.get('department')
        ema = request.POST.get('email')
        ph = request.POST.get('phone')
        bi = request.POST.get('bio')
        pp = request.FILES['image']
        obj = DoctorDb(Name=na,Department_Name=spl,Contact_Email=ema,Contact_Phone=ph,Bio=bi,Profile_Picture=pp)
        obj.save()
        messages.success(request, "Doctor data Saved Successfully")
        return redirect(adddoctor)
def doctordisplay(request):
    data = DoctorDb.objects.all()
    return render(request, "DisplayDoctorDetails.html",{'data':data})

def doctoredit(request,dataid):
    department = DepartmentDb.objects.all()
    data = DoctorDb.objects.get(id=dataid)
    return render(request, "EditDoctorDetails.html",{'data':data, 'department':department})

def updatedoctordata(request, dataid):
    if request.method == "POST":
        na = request.POST.get('name')
        spl = request.POST.get('department')
        ema = request.POST.get('email')
        ph = request.POST.get('phone')
        bi = request.POST.get('bio')
        try:
            pp = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(pp.name,pp)
        except MultiValueDictKeyError:
            file = DoctorDb.objects.get(id=dataid).Profile_Picture
        DoctorDb.objects.filter(id=dataid).update(Name=na,Department_Name=spl,Contact_Email=ema,Contact_Phone=ph,Bio=bi,Profile_Picture=file)
        messages.success(request, "Data edited successfully!!")
        return redirect(doctordisplay)

def deletedoctor(request, dataid):
    data = DoctorDb.objects.filter(id=dataid)
    data.delete()
    return redirect(doctordisplay)
def addnurse(request):
    data = DepartmentDb.objects.all()
    return render(request, "AddNurseDetails.html",{'data':data})

def nursesave(request):
    if request.method == "POST":
        na = request.POST.get('name')
        ph = request.POST.get('phone')
        bi = request.POST.get('bio')
        dep = request.POST.get('department')
        pp = request.FILES['image']
        obj = NurseDb(Name=na,Contact_Phone=ph,Bio=bi,Assigned_Department=dep,Profile_Picture=pp)
        obj.save()
        messages.success(request, "Nurse data Saved Successfully")
        return redirect(addnurse)

def nursedisplay(request):
    data = NurseDb.objects.all()
    return render(request, "DisplayNurseDetails.html",{'data':data})

def nurseedit(request,dataid):
    department = DepartmentDb.objects.all()
    data = NurseDb.objects.get(id=dataid)
    return render(request, "EditNurseDetails.html",{'data':data, 'department':department})

def updatenursedata(request, dataid):
    if request.method == "POST":
        na = request.POST.get('name')
        ph = request.POST.get('phone')
        bi = request.POST.get('bio')
        dep = request.POST.get('department')
        try:
            pp = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(pp.name, pp)
        except MultiValueDictKeyError:
            file = NurseDb.objects.get(id=dataid).Profile_Picture
        NurseDb.objects.filter(id=dataid).update(Name=na,Contact_Phone=ph,Bio=bi,Assigned_Department=dep,Profile_Picture=file)
        messages.success(request, "Data edited successfully!!")
        return redirect(nursedisplay)

def deletenurse(request, dataid):
    data = NurseDb.objects.filter(id=dataid)
    data.delete()
    return redirect(nursedisplay)

def adddepartment(request):
    return render(request, "AddDepartment.html")

def departmentsave(request):
    if request.method == "POST":
        dna = request.POST.get('name')
        des = request.POST.get('description')
        img = request.FILES['image']
        obj = DepartmentDb(Department_Name=dna,Description=des,Department_Image=img)
        obj.save()
        messages.success(request, "Department data Saved Successfully")
        return redirect(adddepartment)

def departmentdisplay(request):
    data = DepartmentDb.objects.all()
    return render(request, "DisplayDepartmentDetails.html",{'data':data})

def departmentedit(request,dataid):
    data = DepartmentDb.objects.get(id=dataid)
    return render(request, "EditDepartmentDetails.html",{'data':data})

def updatedepartmentdata(request, dataid):
    if request.method == "POST":
        dna = request.POST.get('name')
        des = request.POST.get('description')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = DepartmentDb.objects.get(id=dataid).Department_Image
        DepartmentDb.objects.filter(id=dataid).update(Department_Name=dna,Description=des,Department_Image=file)
        messages.success(request, "Data edited successfully!!")
        return redirect(departmentdisplay)

def deletedepartment(request, dataid):
    data = DepartmentDb.objects.filter(id=dataid)
    data.delete()
    return redirect(departmentdisplay)

def addpatient(request):
    data = DepartmentDb.objects.all()
    doctor = DoctorDb.objects.all()
    return render(request,"AddPatientDetails.html",{'data':data, 'doctor':doctor})

def patientsave(request):
    if request.method == "POST":
        pna = request.POST.get('pname')
        ag = request.POST.get('age')
        add = request.POST.get('address')
        ph = request.POST.get('phone')
        his = request.POST.get('history')
        dep = request.POST.get('department')
        ins = request.POST.get('insurance')
        adoc = request.POST.get('adoctor')
        obj = PatientDb(Patient_Name=pna,Age=ag,Address=add,Contact_Phone=ph,Medical_History=his,Admitted_Department=dep,Insurance_Information=ins,Assigned_Doctor=adoc)
        obj.save()
        messages.success(request, "Patient data Saved Successfully")
        return redirect(addpatient)

def patientdisplay(request):
    data = PatientDb.objects.all()
    return render(request,"DisplayPatientDetails.html",{'data':data})

def patientedit(request,dataid):
    data = PatientDb.objects.get(id=dataid)
    department = DepartmentDb.objects.all()
    doctor = DoctorDb.objects.all()
    return render(request, "EditPatientDetails.html",{'data':data,'doctor':doctor,'department':department})

def updatepatientdata(request, dataid):
    if request.method == "POST":
        pna = request.POST.get('pname')
        ag = request.POST.get('age')
        add = request.POST.get('address')
        ph = request.POST.get('phone')
        his = request.POST.get('history')
        dep = request.POST.get('department')
        ins = request.POST.get('insurance')
        adoc = request.POST.get('adoctor')
        PatientDb.objects.filter(id=dataid).update(Patient_Name=pna,Age=ag,Address=add,Contact_Phone=ph,Medical_History=his,Admitted_Department=dep,Insurance_Information=ins,Assigned_Doctor=adoc)
        messages.success(request, "Data edited successfully!!")
        return redirect(patientdisplay)

def deletepatientdata(request, dataid):
    data = PatientDb.objects.filter(id=dataid)
    data.delete()
    return redirect(patientdisplay)

def addmedicine(request):
    return render(request, "AddMedicine.html")


def medicinesave(request):
    if request.method == "POST":
        mna = request.POST.get('mname')
        man = request.POST.get('manufacturer')
        qty = request.POST.get('quantity')
        prc = request.POST.get('price')
        des = request.POST.get('description')
        mi = request.FILES['image']
        obj = MedicineDb(Medicine_Name=mna,Manufacturer=man,Quantity_Stock=qty,Price=prc,Description=des,Medicine_Image=mi)
        obj.save()
        messages.success(request, "Medicine data added successfully")
        return redirect(addmedicine)

def medicinedisplay(request):
    data = MedicineDb.objects.all()
    return render(request,"DisplayMedicine.html",{'data':data})

def medicineedit(request, dataid):
    data = MedicineDb.objects.get(id=dataid)
    return render(request, "EditMedicineDetails.html",{'data':data})


def updatemedicinedata(request, dataid):
    if request.method == "POST":
        mna = request.POST.get('mname')
        man = request.POST.get('manufacturer')
        qty = request.POST.get('quantity')
        prc = request.POST.get('price')
        des = request.POST.get('description')
        try:
            mi = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(mi.name,mi)
        except MultiValueDictKeyError:
            file = MedicineDb.objects.get(id=dataid).Medicine_Image
        MedicineDb.objects.filter(id=dataid).update(Medicine_Name=mna,Manufacturer=man,Quantity_Stock=qty,Price=prc,Description=des,Medicine_Image=file)
        messages.success(request, "Data edited successfully!!")
        return redirect(medicinedisplay)

def deletemedicinedata(request, dataid):
    data = MedicineDb.objects.filter(id=dataid)
    data.delete()
    return redirect(medicinedisplay)

def adminloginpage(request):
    return render(request, "LoginPage.html")

def adminlogin(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        pswrd = request.POST.get('password')
        if User.objects.filter(username__contains=uname).exists():
            user = authenticate(username=uname,password=pswrd)

            if user is not None:
                login(request, user)
                request.session['username'] = uname
                request.session['password'] = pswrd
                messages.success(request, "Login successfully")
                return redirect(indexpage)
            else:
                messages.error(request, "Login Error")
                return redirect(adminloginpage)
        else:
            messages.error(request, "Login Error")
            return redirect(adminloginpage)

def adminlogout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "Logout Successfully")
    return redirect(adminloginpage)

def contactpagedisplay(request):
    data = Contactdb.objects.all()
    return render(request, "DisplayContactPage.html",{'data':data})

def deletecontact(request, dataid):
    data = Contactdb.objects.filter(id=dataid)
    data.delete()
    return redirect(contactpagedisplay)

def appointmentspage(request):
    data = Appointmentdb.objects.all()
    return render(request, "DisplayAppointment.html", {'data':data})

def deleteappointment(request, dataid):
    data = Appointmentdb.objects.filter(id=dataid)
    data.delete()
    return redirect(appointmentspage)

def patientdbregisterpage(request):
    return render(request,"PatientDbRegister.html")

def staffloginsave(request):
    if request.method == "POST":
        na = request.POST.get('name')
        em = request.POST.get('email')
        pa = request.POST.get('pass')
        pas = request.POST.get('passw')
        obj = StaffLoginDb(Name=na,Email=em,Password=pa,Re_Password=pas)
        obj.save()
        return redirect(patientdbregisterpage)






















