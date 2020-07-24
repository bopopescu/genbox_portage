# test_stackDictList.py -- Portage Unit Testing Functionality
# Copyright 2006 Gentoo Foundation
# Distributed under the terms of the GNU General Public License v2
# $Id$

from unittest import TestCase

class StackDictListTestCase(TestCase):

	def testStackDictList(self):
		from portage_util import stack_dictlist
		
		tests = [ ({'a':'b'},{'x':'y'},False,{'a':['b'],'x':['y']}) ]
		tests.append(( {'KEYWORDS':['alpha','x86']},{'KEYWORDS':['-*']},True,{} ))
		tests.append(( {'KEYWORDS':['alpha','x86']},{'KEYWORDS':['-x86']},True,{'KEYWORDS':['alpha']} ))
		for test in tests:
			self.assertEqual(
			stack_dictlist([test[0],test[1]],incremental=test[2]), test[3] )