from django.contrib import admin
from .models import Post

admin.site.register(Post)  	#macht unser Modell Post auf
							# der Admin-Seite sichtbar
