from marshmallow import Schema, fields


class SearchLoadSchema(Schema):
    keywordsString = fields.String(attribute="keywords_string")

    class Meta:
        ordered = True
