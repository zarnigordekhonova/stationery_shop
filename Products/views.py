from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from Products.models import Items, ItemsMake, CategoryItems, Reviews
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AddReviewForm, ReviewUpdateForm

# Create your views here.


class CategoryListView(View):
    def get(self, request):
        category = CategoryItems.objects.all()
        context = {
            'category' : category
        }
        search_post = request.GET.get('search')
        if search_post:
            s = Items.objects.filter(
                Q(name__icontains=search_post) |
                Q(color__icontains=search_post) |
                Q(price__icontains=search_post)
            )
            if not s.exists():
                messages.warning(request, 'No results found...')

        return render(request, 'Products/category_list.html', context=context)


class ProductsDetailView(View):
    def get(self, request, pk):
        items = Items.objects.filter(category=pk)
        context = {
           'items' : items
        }

        return render(request, 'Products/products_detail_view.html', context=context)


class DetailView(View):
    def get(self, request, pk):
        product = Items.objects.get(pk=pk)
        things = Reviews.objects.filter(product_name_id=pk).order_by('-id')
        result = [review.star_given for review in things if 1 < review.star_given < 6]
        average = round(sum(result) / len(result), 1) if result else None

        context = {
            'product': product,
            'things': things,
            'average': average,
        }

        return render(request, 'Products/detail_view.html', context=context)


class AddReviewView(LoginRequiredMixin, View):
    def get(self, request, pk):
        item = Items.objects.get(pk=pk)
        add_review_form = AddReviewForm()
        context = {
            'item': item,
            'add_review_form': add_review_form
        }
        return render(request, 'Products/add_review.html', context=context)

    def post(self, request, pk):
        item = Items.objects.get(pk=pk)
        add_review_form = AddReviewForm(request.POST)
        if add_review_form.is_valid():
            review = Reviews.objects.create(
                comment=add_review_form.cleaned_data['comment'],
                product_name=item,
                user=request.user,
                star_given=add_review_form.cleaned_data['star_given']
            )

            review.save()
            messages.success(request, "Review added successfully.")
            return redirect('products:details', pk=pk)
        else:
            messages.error(request, "Failed to add review. Please check the form.")
            return render(request, 'Products/add_review.html', {'item': item, 'add_review_form': add_review_form})

class FilterProductsView(View):
    def get(self, request):
        expensive = Items.objects.order_by('-price')[:10]
        cheap = Items.objects.order_by('price')[:10]
        context = {
            'expensive' : expensive,
            'cheap' : cheap
        }

        return render(request, 'Products/filter_product.html', context=context)






