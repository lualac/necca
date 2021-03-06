from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
    # url(r'^contato/', include('blog.urls')),
    # url(r'^login/', include('blog.urls')),
    # url(r'^membros/', include('blog.urls')),
    # url(r'^projetos/', include('blog.urls')),
    # url(r'^projeto/', include('blog.urls')),
    # url(r'^publicacoes/', include('blog.urls')),
    # url(r'^acessibilidade/', include('blog.urls')),
    # url(r'^sustentabilidadedoedificio/', include('blog.urls')),
    # url(r'^sustentabilidadeespacosurbanos/', include('blog.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
