from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed

class UploadForm(FlaskForm):
    file = FileField('File Upload', validators=[FileRequired(), FileAllowed(['jpg','png','jpeg'], 'Images only!')], description='Please select an Image to upload')