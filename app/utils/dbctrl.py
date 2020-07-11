import mongoengine as mg

mg.connect("sitedata")

class Character(mg.EmbeddedDocument):
	name = mg.StringField()
	ptype = mg.StringField() # class
	inventory = mg.ListField(mg.StringField())
	pass

class Item(mg.EmbeddedDocument):
	name = mg.StringField()
	count = mg.IntField()
	description = mg.StringField()
	weight = mg.FloatField()
	tags = mg.ListField(mg.StringField)
	equipped = mg.BooleanField()


class UserInfo(mg.Document):
	username = mg.StringField()
	hashed_password = mg.StringField()
	salt = mg.StringField()
	allcharacters = mg.EmbeddedDocumentListField(Character)
	pass


class NPC(mg.EmbeddedDocument):
	name = mg.StringField()
	race = mg.StringField()
	description = mg.StringField()
	secrets = mg.StringField()


class Campaign(mg.Document):
	dm = mg.StringField()
	# if dm field matches the username in session, enable dm mode
	allplayers = mg.EmbeddedDocumentListField(Character)
	allnpc = mg.EmbeddedDocumentListField(NPC)
	pass
