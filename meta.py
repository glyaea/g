import datetime


def type(_object_):
	class Type:
		def __eq__(self, _type_):
			return isinstance(_object_, _type_)
	return Type()


def constant(D):
	if type(D) == set:
		return frozenset(constant(d) for d in D)
	elif type(D) == list:
		return tuple(constant(d) for d in D)
	elif type(D) == dict:
		return frozenset((constant(k), constant(v)) for k, v in D.items())
	else:
		return D


def time(_format_):
	now = datetime.datetime.now()
	if _format_ == "YYYY-MM-DD":
		return now.strftime("%Y-%m-%d")
	elif _format_ == "HH:MM:SS":
		return now.strftime("%H:%M:%S")
