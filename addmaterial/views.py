from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Addmaterial, Publishmaterial
from django.contrib.auth.models import User


@login_required(login_url='/account/login/')
def publish_material(req):
    context = {
        'materials': Addmaterial.objects.all().order_by('title'),
    }
    if req.method == 'POST':
        material_to_publish = Addmaterial.objects.filter(id=req.POST['material_entry'])[0]
        new_published_book = Publishmaterial()
        new_published_book.material_id = material_to_publish
        new_published_book.published_by = req.user
        new_published_book.save()
        context = {
            'message': f'You have succesfully published { new_published_book }! - You can now see it on the dashboard.',
            'materials': Addmaterial.objects.all(),
        }
    return render(req, 'add_material.html', context)


@login_required(login_url='/account/login/')
def register_material(req):
    context = {}
    if req.method == 'POST':
        ### Submitted data
        material_type = req.POST['material_type']
        author = req.POST['material_author']
        title = req.POST['material_title']
        language = req.POST['material_language']
        year = req.POST['material_year']
        pages = req.POST['material_pages']
        quantity = req.POST['material_quantity']
        ###
        if material_type == 'book': ### Check if submit is book or magazine
            new_book = Addmaterial()
            new_book.material_type = material_type
            new_book.author = author
            new_book.title = title
            new_book.language = language
            new_book.year = year
            new_book.pages = pages
            new_book.quantity_available = quantity
            new_book.save()
            context = {
                'message': f'You have successfully added \'{title}\' written by {author} from {year}!'
            }
        else:
            new_magazine = Addmaterial()
            new_magazine.material_type = material_type
            new_magazine.title = title
            new_magazine.language = language
            new_magazine.year = year
            new_magazine.pages = pages
            new_magazine.quantity_available = quantity
            new_magazine.save()
            context = {
                'message': f'You have successfully added the {material_type} {title}!'
            }

    return render(req, 'register_material.html', context)