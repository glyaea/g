from datetime import datetime
import builtins


def range(start, stop=None, step=1):
	# make range(...) include endpoint """
	if stop is None:
		return builtins.range(start + 1)
	return builtins.range(start, stop + (1 if step > 0 else -1), step)


def type(_object_):
	# make type(...) work like isinstance(...)
	class Type:
		def __eq__(self, _type_):
			return isinstance(_object_, _type_)
	return Type()


def concat(*lists):
	# concatenate lists
	out = lists[0].copy()
	for _list_ in lists[1:]:
		out.extend(_list_)
	return out


def constant(_object_):
	# make set, list, or dict immutable
	match _object_:
		case set():
			return frozenset(constant(subobject) for subobject in _object_)
		case list():
			return tuple(constant(subobject) for subobject in _object_)
		case dict():
			return frozenset(
				(constant(key), constant(value))
				for key, value in _object_.items()
			)


def merge(*dicts, keep="right"):
	# merge dicts
	if keep == "left":
		dicts = dicts[::-1]
	out = dicts[0].copy()
	for _dict_ in dicts[1:]:
		out.update(_dict_)
	return out


def time(_format_):
	# return time in YYYY-MM-DD or HH:MM:SS format
	match _format_:
		case "YYYY-MM-DD":
			return datetime.now().strftime("%Y-%m-%d")
		case "HH:MM:SS":
			return datetime.now().strftime("%H:%M:%S")


def union(*sets):
	# union sets
	return set.union(*sets)
