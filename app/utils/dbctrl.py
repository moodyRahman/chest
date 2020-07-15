import mongoengine as mg
from os import environ

# mg.connect("sitedata", 
# 	host=environ["atlasurl"])

mg.connect("sitedata")

class Character(mg.Document):
	name = mg.StringField()
	ptype = mg.StringField() # class
	inventory = mg.ListField(mg.StringField())
	charid = mg.IntField()
	pass


class Item(mg.EmbeddedDocument):
	name = mg.StringField()
	count = mg.IntField()
	description = mg.StringField()
	weight = mg.FloatField()
	tags = mg.ListField(mg.StringField)
	equipped = mg.BooleanField()


class NPC(mg.EmbeddedDocument):
	name = mg.StringField()
	race = mg.StringField()
	description = mg.StringField()
	secrets = mg.StringField()


class Location(mg.EmbeddedDocument):
	description = mg.StringField()
	residents = mg.EmbeddedDocumentListField(NPC)
	pass


class UserInfo(mg.Document):
	username = mg.StringField()
	hashed_password = mg.StringField()
	salt = mg.StringField()
	allcharacters = mg.ListField(mg.ReferenceField("Character"))
	allcampaigns = mg.ListField(mg.ReferenceField("Campaign"))
	pass

class Campaign(mg.Document):
	name = mg.StringField()
	dm = mg.StringField()
	players = mg.ListField(mg.StringField)
	characters = mg.ListField(mg.ReferenceField("Character"))
	allnpc = mg.EmbeddedDocumentListField(NPC)
	alllocation = mg.EmbeddedDocumentField(Location)
	pass
