from django.urls import include, path

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.views import ReferralCodeViewSet, ReferralCodeByEmail, UserRegister


router = DefaultRouter()
router.register("referral_codes", ReferralCodeViewSet)

urlpatterns = [
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/registration/', UserRegister.as_view()),
    path('referral_code_by_email/<str:email>/', ReferralCodeByEmail.as_view()),
    path("", include(router.urls)),
]
