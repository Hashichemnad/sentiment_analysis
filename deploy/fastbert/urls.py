from django.urls import path

urlpatterns=[
	path('model/',views.call_model.as_view)
]
