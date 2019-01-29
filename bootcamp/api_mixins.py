class CommonAPIMixin(object):

    @property
    def user(self):
        return self.context['request']._request.user
