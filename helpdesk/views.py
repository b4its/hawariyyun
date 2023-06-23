from django.shortcuts import render,redirect,HttpResponse
from .models import kritik_saran
from account.models import Profile
from .forms import TeknisiForm
from django.contrib.auth.decorators import login_required
from .forms import JenisForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages

def administration(user):
    return user.groups.filter(name='sekretaris').exists()
# Create your views here.

# function untuk menambahkan

# Create your views here.
TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)

def index_helpdesk(request):
    return render(request, 'index_helpdesk.html')


# def update_informasi_keluhan(request, id):
#   if request.method == 'POST':
#     print("tes")
#     pi = FileUpload.objects.get(pk=id)
#     fm = TeknisiFileUploadForm(request.POST,request.FILES, instance=pi)
#     if fm.is_valid():
#       fm.save()
#       return redirect('tampilan_gambar')
#   else:
#     pi = FileUpload.objects.get(pk=id)
#     fm = TeknisiFileUploadForm(instance=pi)
#   return render(request, 'update_file.html', {'form':fm})


@login_required(login_url='customerlogin')
@user_passes_test(administration,login_url='index_helpdesk')
def update_kritik_saran(request, id):
  if request.method == 'POST':
    pi = kritik_saran.objects.get(pk=id)
    fm = TeknisiForm(request.POST, instance=pi)
    if fm.is_valid():
      fm.save()
      return redirect('list_kritik_saran')
  else:
    pi = kritik_saran.objects.get(pk=id)
    fm = TeknisiForm(instance=pi)
  context ={
     'form':fm,
     'pi':pi
  }
  return render(request, 'pengurus/update_kritik_saran.html',context)


@login_required(login_url='customerlogin')
def saran(request):
   profil = Profile.objects.get(user = request.user)
   cek = Profile.objects.filter(user = request.user, role = 7).exists()
   if request.method == 'POST':
        form = JenisForm(request.POST, request.FILES)
        print(form.as_p)
        if form.is_valid():
            user = request.user
            jenis = form.cleaned_data['jenis']
            pembahasan = form.cleaned_data['pembahasan']
            status = 1
            kritik_saran(user = user, jenis=jenis,pembahasan=pembahasan, status=status).save()
            messages.success(request,'Terima kasih atas kritik atau saran nya :)')
            return redirect('index_helpdesk')
        else:
            messages.error(request, 'Data tidak bisa terkirim :)')
            return redirect('index_helpdesk')
   else:
        context = {
            'form':JenisForm(),
            'cek':cek
        }
   return render(request, 'saran.html',context)
@login_required
@user_passes_test(administration,login_url='index_helpdesk')
def list_kritik_saran(request):
    pengurus = Profile.objects.get(user = request.user)
    saran = kritik_saran.objects.all().order_by('-date_posted')
    context = {
        'pengurus':pengurus,
        'saran':saran,
    }
    return render(request, 'pengurus/list_kritik_saran.html',context)
@login_required
@user_passes_test(administration,login_url='index_helpdesk')
def list_kritik(request):
    pengurus = Profile.objects.get(user = request.user)
    saran = kritik_saran.objects.filter(jenis = 1)
    context = {
        'pengurus':pengurus,
        'saran':saran,
    }
    return render(request, 'pengurus/list_kritik.html',context)
@login_required
@user_passes_test(administration,login_url='index_helpdesk')
def list_saran(request):
    pengurus = Profile.objects.get(user = request.user)
    saran = kritik_saran.objects.filter(jenis = 2)
    context = {
        'pengurus':pengurus,
        'saran':saran,
    }
    return render(request, 'pengurus/list_saran.html',context)

@login_required
@user_passes_test(administration,login_url='index_helpdesk')
def list_nama(request):
    pengurus = Profile.objects.get(user = request.user)
    saran = kritik_saran.objects.all()
    if request.method == "POST":
        pencarian = request.POST['pencarian']
        hasil = kritik_saran.objects.filter(user__first_name__contains=pencarian)
        context = {
            'pengurus':pengurus,
            'saran':saran,
            'hasil':hasil,
            'pencarian':pencarian
        }
        return render(request, 'pengurus/list_nama.html',context)
    else:
        return render(request, 'pengurus/list_nama.html',{})

