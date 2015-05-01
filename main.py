import webapp2
from webapp2_extras import routes
from application.views import source as view



app = webapp2.WSGIApplication([
    routes.DomainRoute(r'<:.*>', [
        webapp2.Route('/', handler=view.IndexHandler, name="www-index"),
    ])
])
