import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20200528_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='detail',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]