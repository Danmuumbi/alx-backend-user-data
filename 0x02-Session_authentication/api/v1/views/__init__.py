from flask import Blueprint

app_views = Blueprint('app_views', __name__)

# Import the views
from api.v1.views.index import *
from api.v1.views.users import *
