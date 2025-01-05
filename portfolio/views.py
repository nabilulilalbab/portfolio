from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from .forms import ContactForm
from .models import Profile,Technology,Project
# Create your views here.
def index(request):
    profile_all = Profile.objects.all()
    technology_all = Technology.objects.all()
    context = {
        'title': 'Home',
        'profile_all': profile_all,
        'technology_all': technology_all,
    }
    return render(request, 'portfolio/index.html',context)


def profile_view(request):
    # Ambil profil pertama (atau sesuaikan logika pengambilan profil)
    try:
        profile = Profile.objects.first()
    except Profile.DoesNotExist:
        profile = None
    technology_all = Technology.objects.all()
    context = {
        'profile': profile,
        'technology_all': technology_all,
        'title': 'Profil Saya'
    }

    return render(request, 'portfolio/profile.html', context)

def project_list(request):
    projects = Project.objects.prefetch_related('technologies').all()
    context = {
        'title': 'Project',
        'projects': projects
    }
    return render(request, 'portfolio/project.html', context)


def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    # Ambil teknologi yang digunakan dalam proyek
    technologies = project.technologies.all()

    context = {
        'title': 'Project',
        'project': project,
        'technologies': technologies
    }

    return render(request, 'portfolio/project_detail.html', context)


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Simpan pesan
            contact = form.save()

            # Tambahkan pesan sukses
            messages.success(request, 'Pesan Anda berhasil dikirim. Terima kasih!')

            # Redirect atau tetap di halaman
            return redirect('portfolio:contact')
    else:
        form = ContactForm()

    context = {
        'form': form,
        'title': 'Hubungi Kami'
    }
    return render(request, 'portfolio/contact.html', context)