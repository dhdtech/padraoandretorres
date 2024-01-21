"""
URL configuration for padraoandretorres project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.urls import include


@api_view(["GET"])
@permission_classes([AllowAny])
def health(_):
    return Response({"status": "ok!"})


urlpatterns = [
    path("admin/", include("massadmin.urls")),
    path("admin/", admin.site.urls),
    path("health/", health),
]

# allow DRF Spectacular in the dev environment
if settings.DEBUG or settings.ENV == "dev":
    # DRF SPECTACULAR (SWAGGER CONFIG)
    from drf_spectacular.views import (
        SpectacularAPIView,
        SpectacularJSONAPIView,
        SpectacularSwaggerView,
    )

    SWAGGER_TEMPLATE_PATH = "dhdadmin/templates/swagger-ui.html"

    urlpatterns += [
        path(
            "api/swagger/",
            SpectacularSwaggerView.as_view(url_name="schema-swagger-json"),
            name="schema-swagger-ui",
        ),
        path(
            "api/swagger.yaml/",
            SpectacularAPIView.as_view(),
            name="schema-swagger-yaml",
        ),
        path(
            "api/swagger.json/",
            SpectacularJSONAPIView.as_view(),
            name="schema-swagger-json",
        ),
    ]


admin.site.site_header = "#PADRÃOANDRETORRES Admin"
admin.site.site_title = "#PADRÃOANDRETORRES Admin"
admin.site.index_title = "Bem vindo ao #PADRÃOANDRETORRES Admin"
admin.site.site_url = "/admin"
