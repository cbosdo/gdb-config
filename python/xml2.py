import gdb


class xmlNodePrinter(object):
	"Print an xmlNodePtr"

	class _iterator:
		def __init__(self, head):
			self.link = head
			self.count = 0

		def __iter__(self):
			return self

		def next(self):
			if self.link == 0:
				raise StopIteration
			data = self.link
			count = self.count
			self.link = self.link['next']
			self.count = self.count + 1
			return ('[%d]' % count, data)

	def __init__(self, val):
		self.val = val

	def children(self):
		return self._iterator(self.val['children'])

	def to_string(self):
		# Actually print the node recursively
		return "{0x%x, type:%s, name: %s}" % (long(self.val), self.val['type'], self.val['name'])

	def display_hint(self):
		return "array"

def pretty_printer_lookup(val):
	
    type = val.type.unqualified()

    # If it points to a reference, get the reference.
    if type.code == gdb.TYPE_CODE_REF:
        type = type.target ()

    if type.code == gdb.TYPE_CODE_PTR:
        type = type.target().unqualified()
        t = str(type)
        if t == "struct _xmlNode":
            return xmlNodePrinter(val)
    else:
        t = str(type)
        if t == "struct _xmlNode":
            return xmlNodePrinter(val)
    return None

def register(obj):
	if obj is None:
	    obj = gdb

	obj.pretty_printers.append(pretty_printer_lookup)

