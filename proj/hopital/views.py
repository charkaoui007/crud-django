from django.shortcuts import render, redirect
from .models import Patient
from .forms import PatientForm
# Create your views here.
def patient_list(request):
    patients=Patient.objects.all()
    return render(request,'patient.html',{'patients':patients})

def create_patient(request):
    if request.method== 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()
    return  render(request, 'create_patient.html' , {'form':form})