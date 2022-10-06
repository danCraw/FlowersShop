from flask_admin import Admin, BaseView, expose, AdminIndexView

from main import app, db
from models.flower import FlowerAdminModel, FlowerModel


class DashBoardView(AdminIndexView):
    @expose('/')
    def add_data_db(self):
        return self.render('admin/dashboard_index.html')


admin = Admin(app, name='Цветочный магазин', template_mode='bootstrap3', index_view=DashBoardView(), endpoint='admin')
admin.add_view(FlowerAdminModel(FlowerModel, db.session, name='Цветы'))