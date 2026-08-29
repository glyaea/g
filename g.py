import builtins
import time


def range(start, stop=None, step=1):
	if stop is None:
		return builtins.range(start + 1)
	return builtins.range(start, stop + (1 if step > 0 else -1), step)


def type(_object_):
	class Type:
		def __eq__(self, _type_):
			return isinstance(_object_, _type_)

		def __repr__(self):
			return repr(builtins.type(_object_))
	return Type()


def concat(*lists):
	concatenation = []
	for _list_ in lists:
		concatenation.extend(_list_)
	return concatenation


def merge(*dicts):
	merger = {}
	for _dict_ in dicts:
		merger.update(_dict_)
	return merger


def now(_format_):
	return time.strftime(
		_format_.replace("YYYY-MM-DD", "%Y-%m-%d")
			.replace("HH:MM:SS", "%H:%M:%S")
	)


def union(*sets):
	return set().union(*sets)
