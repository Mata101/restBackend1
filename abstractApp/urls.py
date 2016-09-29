from django.conf.urls import url


from . import views

urlpatterns = [
   
    url(r'smugglers/', views.smugglers, name='smugglers'),
    url(r'smuggler/(?P<id>[0-9]+)/',views.details, name='details'),
    url(r'product/', views.product, name='product'),
    url(r'save/', views.save, name='save'),
    url(r'login/', views.login, name='login'),
  	url(r'register/', views.register, name='register'),
  	url(r'id/', views.id, name='id'),
    url(r'removeorder/', views.removeorder, name='removeorder'),
    url(r'deliverorder/', views.deliverorder, name='deliverorder'),
    url(r'addproduct1/', views.addproduct1, name='addproduct1'),
    url(r'showp/', views.showp, name='showp'),
  	url(r'order/', views.order, name='order'),
  	url(r'get/', views.get, name='get'),
    url(r'getallhistory/', views.getallhistory, name='getallhistory'),
    url(r'getall/', views.getall, name='getall'),
    url(r'deletep/', views.deletep, name='deletep'),
    url(r'showhistory/', views.showhistory, name='showhistory'),

  	



]
