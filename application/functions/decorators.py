def login_required(fn):
    '''So we can decorate any RequestHandler with #@login_required'''
    def wrapper(self, *args, **kwargs):
        if not self.user:
            if self.request.get('redirect'):
                self.redirect(self.uri_for('www-index', redirect=self.request.get('redirect')))
                return
            else:
                self.redirect(self.uri_for('www-index'))
                return
        else:
            return fn(self, *args, **kwargs)
    return wrapper


def login_required_no_redirect(fn):
    '''Returns 401 if not logged in'''
    def wrapper(self, *args, **kwargs):
        if not self.user:
            self.error(401)
            return
        else:
            return fn(self, *args, **kwargs)
    return wrapper
