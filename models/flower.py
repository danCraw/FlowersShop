import sqlalchemy
import os
import random
from main import db, app
from flask_admin.contrib import sqla
from flask_admin import form

metadata = sqlalchemy.MetaData()


class FlowerModel(db.Model):
    __tablename__ = "flowers"

    flower_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String, unique=True)


class FlowerAdminModel(sqla.ModelView):
    form_extra_fields = {
        'file': form.FileUploadField('file')
    }

    def _change_path_data(self, _form):
        try:
            storage_file = _form.file.data

            if storage_file is not None:
                hash = random.getrandbits(128)
                ext = storage_file.filename.split('.')[-1]
                path = '%s.%s' % (hash, ext)

                storage_file.save(
                    os.path.join(app.config['STORAGE'], path)
                )

                _form.name.data = _form.name.data or storage_file.filename
                _form.path.data = path
                _form.type.data = ext

                del _form.file

        except Exception as ex:
            pass