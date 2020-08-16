from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from authapp.models import ShopUser
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from mainapp.models import ProductCategory

from mainapp.models import Product

from authapp.forms import ShopUserRegisterForm

from adminapp.forms import ShopUserAdminEditForm

from adminapp.forms import ProductCategoryEditForm

from adminapp.forms import ProductEditForm


# @user_passes_test(lambda u: u.is_superuser)
# def user_create(request):
#     title = 'пользователи / создание'
#
#     if request.method == 'POST':
#         update_form = ShopUserRegisterForm(request.POST, request.FILES)
#
#         if update_form.is_valid():
#             update_form.save()
#             return HttpResponseRedirect(reverse('admin:users'))
#     else:
#         update_form = ShopUserRegisterForm()
#
#     content = {
#         'title': title,
#         'update_form': update_form
#     }
#     return render(request, 'adminapp/user_update.html', content)


# @user_passes_test(lambda u: u.is_superuser)
# def users(request):
#     title = 'админка / пользователи'
#     users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')
#     content = {
#         'title': title,
#         'objects': users_list
#     }
#     return render(request, 'adminapp/users.html', content)

# @user_passes_test(lambda u: u.is_superuser)
# def user_update(request, pk):
#     title = 'пользователи / редактирование'
#     edit_user = get_object_or_404(ShopUser, pk=pk)
#     if request.method == 'POST':
#         edit_form = ShopUserAdminEditForm(request.POST, request.FILES, instance=edit_user)
#         if edit_form.is_valid():
#             edit_form.save()
#             return HttpResponseRedirect(reverse('admin:users'))
#     else:
#         edit_form = ShopUserAdminEditForm(instance=edit_user)
#     content = {
#         'title': title,
#         'update_form': edit_form
#     }
#     return render(request, 'adminapp/user_update.html', content)

# @user_passes_test(lambda u: u.is_superuser)
# def user_delete(request, pk):
#     title = 'пользователи / удаление'
#
#     user_item = get_object_or_404(ShopUser, pk=pk)
#
#     if request.method == 'POST':
#         if user_item.is_active:
#             user_item.is_active = False
#         else:
#             user_item.is_active = True
#         user_item.save()
#         return HttpResponseRedirect(reverse('admin:users'))
#     content = {
#         'title': title,
#         'user_to_delete': user_item
#     }
#
#     return render(request, 'adminapp/user_delete.html', content)


# @user_passes_test(lambda u: u.is_superuser)
# def categories(request):
#     title = 'админка / категории'
#     categories_list = ProductCategory.objects.all().order_by('-is_active', '-id')
#     content = {
#         'title': title,
#         'objects': categories_list
#     }
#     return render(request, 'adminapp/categories.html', content)

# @user_passes_test(lambda u: u.is_superuser)
# def category_update(request, pk):
#     title = 'категории / редактирование'
#
#     category_item = get_object_or_404(ProductCategory, pk=pk)
#
#     if request.method == 'POST':
#         update_form = ProductCategoryEditForm(request.POST, request.FILES, instance=category_item)
#
#         if update_form.is_valid():
#             update_form.save()
#             return HttpResponseRedirect(reverse('admin:categories'))
#     else:
#         update_form = ProductCategoryEditForm(instance=category_item)
#
#     content = {
#         'title': title,
#         'update_form': update_form
#     }
#     return render(request, 'adminapp/category_update.html', content)

# @user_passes_test(lambda u: u.is_superuser)
# def category_delete(request, pk):
#     title = 'категория/удаление'
#     category_item_delete = get_object_or_404(ProductCategory, pk=pk)
#     if request.method == 'POST':
#         category_item_delete.is_active = False
#         category_item_delete.save()
#         return HttpResponseRedirect(reverse('admin:categories'))
#     content = {
#         'title': title,
#         'category_to_delete': category_item_delete
#     }
#     return render(request, 'adminapp/category_delete.html', content)

class UsersCreateView(CreateView):
    model = ShopUser
    form_class = ShopUserAdminEditForm
    template_name = 'adminapp/user_update.html'
    success_url = reverse_lazy('admin:users')

    # @method_decorator(user_passes_test(lambda u: u.is_superuser))
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return queryset.filter(is_active=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        content = super().get_context_data(**kwargs)
        content['title'] = 'пользователи / создание'
        return content


class UsersListView(ListView):
    model = ShopUser
    template_name = 'adminapp/users.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return queryset.filter(is_active=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        content = super().get_context_data(**kwargs)
        content['title'] = 'админка / пользователи'
        return content


class UsersUpdateView(UpdateView):
    model = ShopUser
    form_class = ShopUserAdminEditForm
    template_name = 'adminapp/user_update.html'
    success_url = reverse_lazy('admin:users')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return queryset.filter(is_active=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        content = super().get_context_data(**kwargs)
        content['title'] = 'пользователи / создание'
        return content


class UserDeleteView(DeleteView):
    model = ShopUser
    template_name = 'adminapp/user_delete.html'
    success_url = reverse_lazy('admin:users')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        content = super().get_context_data(**kwargs)
        content['title'] = 'пользователи / удаление'
        return content

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


class ProductCategoryCreateView(CreateView):
    model = ProductCategory
    form_class = ProductCategoryEditForm
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('admin:categories')
    # fields = '__all__'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        content = super().get_context_data(**kwargs)
        content['title'] = 'категории / создание'
        return content


class ProductCategoryListView(ListView):
    model = ProductCategory
    template_name = 'adminapp/categories.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        content = super().get_context_data(**kwargs)
        content['title'] = 'админка / категории'
        return content


class ProductCategoryUpdateView(UpdateView):
    model = ProductCategory
    form_class = ProductCategoryEditForm
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('admin:categories')
    # fields = '__all__'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        content = super().get_context_data(**kwargs)
        content['title'] = 'категории / редактирование'
        return content


class ProductCategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = 'adminapp/category_delete.html'
    success_url = reverse_lazy('admin:categories')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        content = super().get_context_data(**kwargs)
        content['title'] = 'категории / удаление'
        return content

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


# @user_passes_test(lambda u: u.is_superuser)
# def product_create(request, pk):
#     title = 'продукт / создание'
#     category = get_object_or_404(ProductCategory, pk=pk)
#     if request.method == 'POST':
#         product_form = ProductEditForm(request.POST, request.FILES)
#         if product_form.is_valid():
#             product_form.save()
#             return HttpResponseRedirect(reverse('admin:products', args=[pk]))
#     else:
#         product_form = ProductEditForm()
#     content = {
#         'title': title,
#         'update_form': product_form,
#         'category': category
#     }
#     return render(request, 'adminapp/product_update.html', content)


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductEditForm
    template_name = 'adminapp/product_update.html'
    success_url = reverse_lazy('admin:products')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_active=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        content = super().get_context_data(**kwargs)
        content['title'] = 'продукт / создание'
        return content


# @user_passes_test(lambda u: u.is_superuser)
# def products(request, pk):
#     title = 'админка / товары'
#     category_item = get_object_or_404(ProductCategory, pk=pk)
#     products_list = Product.objects.filter(category=category_item).order_by('-id')
#     content = {
#         'title': title,
#         'objects': products_list,
#         'category': category_item
#     }
#     return render(request, 'adminapp/products.html', content)

class ProductListView(ListView):
    model = Product
    template_name = 'adminapp/products.html'
    queryset = Product.objects.all()

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        content = super().get_context_data(**kwargs)
        content['title'] = 'админка / товары'
        return content

    def get_queryset(self):
        queryset = super(ProductListView, self).get_queryset()
        category_pk = self.kwargs.get('category_pk')
        if category_pk:
            category = get_object_or_404(ProductCategory, pk=category_pk)
            queryset = queryset.filter(category=category)
        return queryset

# @user_passes_test(lambda u: u.is_superuser)
# def product_update(request, pk):
#     title = 'продукт / редактирование'
#     edit_product = get_object_or_404(Product, pk=pk)
#     if request.method == 'POST':
#         edit_form = ProductEditForm(request.POST, request.FILES, instance=edit_product)
#         if edit_form.is_valid():
#             edit_form.save()
#             return HttpResponseRedirect(reverse('admin:product_update', args=[edit_product.pk]))
#     else:
#         edit_form = ProductEditForm(instance=edit_product)
#     content = {
#         'title': title,
#         'update_form': edit_form,
#         'category': edit_product.category
#     }
#     return render(request, 'adminapp/product_update.html', content)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductEditForm
    template_name = 'adminapp/product_update.html'
    success_url = reverse_lazy('admin:product_update')
    # fields = '__all__'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        content = super().get_context_data(**kwargs)
        content['title'] = 'продукт / редактирование'
        return content

# @user_passes_test(lambda u: u.is_superuser)
# def product_delete(request, pk):
#     title = 'продукт/удаление'
#     product = get_object_or_404(Product, pk=pk)
#     if request.method == 'POST':
#         product.is_active = False
#         product.save()
#         return HttpResponseRedirect(reverse('admin:products', args=[product.category.pk]))
#     content = {
#         'title': title,
#         'product_to_delete': product
#     }
#     return render(request, 'adminapp/product_delete.html', content)


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'adminapp/product_delete.html'
    success_url = reverse_lazy('admin:products')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        content = super().get_context_data(**kwargs)
        content['title'] = 'продукт / удаление'
        return content

    # def get_success_url(self):
    #     return reverse_lazy('admin:products', kwargs={'pk': self.kwargs.get('pk')})

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

# @user_passes_test(lambda u: u.is_superuser)
# def product_read(request, pk):
#     title = 'продукт/подробнее'
#     product = get_object_or_404(Product, pk=pk)
#     content = {
#         'title': title,
#         'object': product
#     }
#     return render(request, 'adminapp/product_read.html', content)


class ProductDetailsView(DetailView):
    model = Product
    template_name = 'adminapp/product_read.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        content = super().get_context_data(**kwargs)
        content['title'] = 'продукт / подробнее'
        return content


