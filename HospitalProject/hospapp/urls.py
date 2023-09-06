from django.urls import path
from hospapp import views


urlpatterns = [
path('indexpage/',views.indexpage,name="indexpage"),
path('adddoctor/',views.adddoctor,name="adddoctor"),
path('doctorsave/',views.doctorsave,name="doctorsave"),
path('doctordisplay/',views.doctordisplay,name="doctordisplay"),
path('doctoredit/<int:dataid>/',views.doctoredit,name="doctoredit"),
path('updatedoctordata/<int:dataid>/',views.updatedoctordata,name="updatedoctordata"),
path('deletedoctor/<int:dataid>/',views.deletedoctor,name="deletedoctor"),
path('addnurse/',views.addnurse,name="addnurse"),
path('nursesave/',views.nursesave,name="nursesave"),
path('nursedisplay/',views.nursedisplay,name="nursedisplay"),
path('nurseedit/<int:dataid>/',views.nurseedit,name="nurseedit"),
path('updatenursedata/<int:dataid>/',views.updatenursedata,name="updatenursedata"),
path('deletenurse/<int:dataid>/',views.deletenurse,name="deletenurse"),
path('adddepartment/',views.adddepartment,name="adddepartment"),
path('departmentsave/',views.departmentsave,name="departmentsave"),
path('departmentdisplay/',views.departmentdisplay,name="departmentdisplay"),
path('departmentedit/<int:dataid>/',views.departmentedit,name="departmentedit"),
path('updatedepartmentdata/<int:dataid>/',views.updatedepartmentdata,name="updatedepartmentdata"),
path('deletedepartment/<int:dataid>/',views.deletedepartment,name="deletedepartment"),
path('addpatient/',views.addpatient,name="addpatient"),
path('patientsave/',views.patientsave,name="patientsave"),
path('patientdisplay/',views.patientdisplay,name="patientdisplay"),
path('patientedit/<int:dataid>/',views.patientedit,name="patientedit"),
path('updatepatientdata/<int:dataid>/',views.updatepatientdata,name="updatepatientdata"),
path('deletepatientdata/<int:dataid>/',views.deletepatientdata,name="deletepatientdata"),
path('addmedicine/',views.addmedicine,name="addmedicine"),
path('medicinesave/',views.medicinesave,name="medicinesave"),
path('medicinedisplay/',views.medicinedisplay,name="medicinedisplay"),
path('medicineedit/<int:dataid>/',views.medicineedit,name="medicineedit"),
path('updatemedicinedata/<int:dataid>/',views.updatemedicinedata,name="updatemedicinedata"),
path('deletemedicinedata/<int:dataid>/',views.deletemedicinedata,name="deletemedicinedata"),
path('adminloginpage/',views.adminloginpage,name="adminloginpage"),
path('adminlogin/',views.adminlogin,name="adminlogin"),
path('adminlogout/',views.adminlogout,name="adminlogout"),
path('contactpagedisplay/',views.contactpagedisplay,name="contactpagedisplay"),
path('deletecontact/<int:dataid>/',views.deletecontact,name="deletecontact"),
path('appointmentspage/',views.appointmentspage,name="appointmentspage"),
path('deleteappointment/<int:dataid>/',views.deleteappointment,name="deleteappointment"),
path('patientdbregisterpage/',views.patientdbregisterpage,name="patientdbregisterpage"),
path('staffloginsave/',views.staffloginsave,name="staffloginsave"),



]