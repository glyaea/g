import builtins
import datetime


def range(start, stop=None, step=1):
""" make range(...) include endpoint """
	if stop is None:
		return builtins.range(start + 1)
	return builtins.range(start, stop + (1 if step > 0 else -1), step)


def type(_object_):
""" make type(...) work like isinstance(...) """
	class Type:
		def __eq__(self, _type_):
			return isinstance(_object_, _type_)
	return Type()


def concat(*lists):
""" concatenate lists """
	out = []
	for _list_ in lists:
		out.extend(_list_)
	return out


def constant(D):
""" make set, list, or dict immutable """
	if type(D) == set:
		return frozenset(constant(d) for d in D)
	elif type(D) == list:
		return tuple(constant(d) for d in D)
	elif type(D) == dict:
		return frozenset((constant(k), constant(v)) for k, v in D.items())
	else:
		return D


def time(_format_):
""" return time in YYYY-MM-DD or HH:MM:SS format """
	now = datetime.datetime.now()
	if _format_ == "YYYY-MM-DD":
		return now.strftime("%Y-%m-%d")
	elif _format_ == "HH:MM:SS":
		return now.strftime("%H:%M:%S")


def union(*sets):
""" union sets """
	return set().union(*sets)
