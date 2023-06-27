import requests
import json
from dateutil import parser

from document.models import Document
from document.enums import DocType, DocSubType, Media, DocFunction

"""
To run this scraper:
    python manage.py runscript documentscraper

Curl command for terminal:
    curl -X POST https://edms.deq.louisiana.gov/edmsv2/documentSearch/filter \
       -H "Content-Type: application/json" \
       -d '{"filter":{"descriptionMode":"Exact","descriptionFuzzy":false,"documentDateRange":{"start":null,"end":null},"entryDateRange":{"start":null,"end":null},"aiInformation":"26073;3585;1250;1255;19588;1244;5337;195519;11496;2538;16996;271;27518;9061;4013"},"refinerFilter":{"documentDates":[],"functions":[],"medias":[],"documentTypes":[],"documentSubtypes":[],"ais":[]},"start":0,"rows":100,"sort":"documentSubtype","asc":true,"highlight":false}'
"""

NUM_ROWS = 10

def run():
    scraper = DocumentScraper()
    scraper.scrapescrape()

class DocumentScraper:
    def scrapescrape(self):
        freshdoc = self.getFreshestDocument()
        print("\nfreshest doc in db:")
        print(freshdoc)
        unseen_docs = self.getDocSubmittedAfter(freshdoc.datetime if freshdoc else None)
        documents = [self.convertJsonToDocument(entry) for entry in unseen_docs]
        print("num documents added")
        print(len(documents))
        return

    def getFreshestDocument(self):
        # Document queryset - sort by date descending, get first doc
        return Document.objects.order_by("-datetime").first()

    def getDocSubmittedAfter(self, datetime):
        # get all data from website
        start, end = None, None
        if datetime:
            start=datetime.strftime("%Y-%m-%dT%H:%M:%SZ")
            end=datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
        print("\nadd docs added after this and before that:")
        print(start)
        print(end)

        response = self.makeRequest(start, end)
        print("\nresponse:")
        print(response)
        return response.json().get('data')

    def convertJsonToDocument(self, json_data):
        # if no ai number, don't create an object
        if len(json_data.get('aiNumbers')) == 0:
            return None

        rawDocType = json_data.get('documentType')
        rawDocSubType = json_data.get('documentSubtype')
        rawFunction = json_data.get('function')
        rawMediaList = json_data.get('media')

        docType = (DocType(rawDocType) if DocType.has_value(rawDocType) else None) or DocType.OT
        docSubType = (DocSubType(rawDocSubType) if DocSubType.has_value(rawDocSubType) else None) or DocSubType.OT
        dfunction = (DocFunction(rawFunction) if DocFunction.has_value(rawFunction) else None) or DocFunction.OT
        media = Media.OT
        if len(rawMediaList) > 0 and Media.has_value(rawMediaList[0]):
            media = Media(rawMediaList[0])

        # e.g. "2023-06-20T12:00:00Z"
        rawDocDatetime = json_data.get('documentDate')
        rawEntryDatetime = json_data.get('entryDate')
        docDatetime = parser.parse(rawDocDatetime)
        entryDatetime = parser.parse(rawEntryDatetime)

        # if multiple ai numbers, create separate Document objects for each
        for ai in json_data.get('aiNumbers'):
            Document.objects.get_or_create(
                edms_id=json_data.get('id'),
                ai=ai,
                dtype=docType,
                dsubtype=docSubType,
                datetime=docDatetime,
                entry_datetime=entryDatetime,
                description=json_data.get('description'),
                media=media,
                dfunction=dfunction,
                num_pages=json_data.get('pages'),
            )

    def makeRequest(self, start=None, end=None):
        url = "https://edms.deq.louisiana.gov/edmsv2/documentSearch/filter"
        headers = {
            'Content-Type': 'application/json',
        }
        json_data = {
            'filter': {
                'descriptionMode': 'Exact',
                'descriptionFuzzy': False,
                'documentDateRange': {
                    'start': start,
                    'end': end,
                },
                'entryDateRange': {
                    'start': None,
                    'end': None,
                },
                'aiInformation': '26073;3585;1250;1255;19588;1244;5337;195519;11496;2538;16996;271;27518;9061;4013',
            },
            'refinerFilter': {
                'documentDates': [],
                'functions': [],
                'medias': [],
                'documentTypes': [],
                'documentSubtypes': [],
                'ais': [],
            },
            'start': 0,
            'rows': NUM_ROWS,
            'sort': 'documentSubtype',
            'asc': True,
            'highlight': False,
        }
        return requests.post(url, headers=headers, json=json_data)
