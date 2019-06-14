from channels.routing import ProtocolTypeRouter, URLRouter
import app.routing

application = ProtocolTypeRouter({
    'http': URLRouter(app.routing.urlpatterns),
})