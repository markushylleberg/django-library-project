from django.shortcuts import render
from .models import Addmaterial

def add_material(req):
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

    return render(req, 'add_material.html', context)