from application import base
import json as simplejson


class IndexHandler(base.BaseHandler):
	def get(self):
		self.tv["current_page"] = "INDEX"
		self.render('index.html')


