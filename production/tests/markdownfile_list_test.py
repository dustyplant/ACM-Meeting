"""
	Test for markdownfile List class

	Author: David Nuon
"""

#!/usr/bin/env python
from testhelper import *
import sys

clear()

sys.path.insert(0, '../')

import traceback

test = None
new_list = None

def init_test():
	global test
	from acm.util.markdownfile import MarkdownList

	class TestClass(MarkdownList):
		def reset(self):
			self._contents = ""
			self.level = ""

	test = TestClass()

def add_test(reset = True):
	global test
	from acm.util.markdownfile import MarkdownList

	x = MarkdownList(True)
	x.append("Deep")
	x.append("Deep")
	x.append("Deep")

	n = MarkdownList(True)
	n.append("toa1111st")
	n.append("toas111t")
	n.append("toas111t")
	n.append(x)

	g = MarkdownList(True)
	g.append("23232")
	g.append(n)

	test.append("This is a good list.")
	test.append(g)

	if reset:
		print test
		print 
		test.reset()

def fruit_test():
	from acm.util.markdownfile import MarkdownList as m

	class MarkdownList(m):
		def __init__(self, ordered = False):
			m.__init__(self, ordered)
			self._indent = " "

	root = MarkdownList(True)
	root.append("I am root")
	root.append("I am root also")

	leaf = MarkdownList()
	leaf.append("This is a leaf.")
	leaf.append("This is the leaf.")

	fruit = MarkdownList()
	fruit.append("I am a cherry.")
	fruit.append("I am too a cherry.")

	bug = MarkdownList(True)
	bug.append("I am a cherry.")
	bug.append("I am too a cherry.")

	fruit.append(bug)
	leaf.append(fruit)
	root.append(leaf)

	print root.markdown()

def markdown_test():
	from acm.util.markdownfile import MarkdownList as m

	class MarkdownList(m):
		def __init__(self, ordered = False):
			m.__init__(self, ordered)
			self._indent = " "

	lists = []
	
	root = MarkdownList()
	root.append("Foo")
	root.append("Bar")


	for n in xrange(0, 21):
		node = MarkdownList()
		node.append("First!")
		node.append(":(")
		node.append("This list is glorious!")
		lists.append(node)


	for index, n in enumerate(lists):
		if index + 1 < len(lists):
			lists[index + 1].append(n)

	root.append(lists[-1])
	print root.markdown()

do_test(init_test, "Initialization")
do_test(add_test, "Adding Strings and MarkdownLists")
do_test(markdown_test, "Markdown ouput")
do_test(fruit_test, "Markdown ouput with ordered and unordered lists")
