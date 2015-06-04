from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'organizations/(?P<organization_id>[0-9]+)/services', views.OrganizationServicesView, base_name='organizations')
router.register(r'organizations/(?P<organization_id>[0-9]+)/locations', views.OrganizationLocationsView, base_name='organizations')
router.register(r'organizations/(?P<organization_id>[0-9]+)/contacts', views.OrganizationContactsView, base_name='organizations')
router.register(r'organizations', views.OrganizationsView)
router.register(r'services', views.ServicesView)
router.register(r'locations', views.LocationsView)
router.register(r'contacts', views.ContactsView)
router.register(r'hours', views.HoursView)
router.register(r'eligibilities', views.EligibilitiesView)
router.register(r'tags', views.TagsView)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
]
