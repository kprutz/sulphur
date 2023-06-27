from django.db import models
from .enums import DocType, DocSubType, Media, DocFunction


class Document(models.Model):
  edms_id = models.IntegerField()  # id of document in EDMS  system
  ai = models.IntegerField()  # ai of chemical plant associated with document  --- if multiple ais on doc, separate Document objects are created
  dtype = models.CharField(  # document type
    max_length=2,
    choices=[(tag, tag.value) for tag in DocType],
    default=DocType.OT
  )
  dsubtype = models.CharField(  # document subtype
    max_length=2,
    choices=[(tag, tag.value) for tag in DocSubType],
    default=DocSubType.OT
  )
  datetime = models.DateTimeField(auto_now=False)  # datetime when document was made
  entry_datetime = models.DateTimeField(auto_now=False)  # datetime when document was added into edms db
  description = models.TextField()  # description of doc
  media = models.CharField(  # media type
    max_length=2,
    choices=[(tag, tag.value) for tag in Media],
    default=Media.OT
  )
  dfunction = models.CharField(  # function type
    max_length=2,
    choices=[(tag, tag.value) for tag in DocFunction],
    default=DocFunction.OT
  )
  num_pages = models.IntegerField()  # number of pages in document
  converted_text = models.TextField()  # document pdf converted to text

  def __str__(self):
    return '{} - {}'.format(self.ai, self.description)
