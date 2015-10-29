from django.test import TestCase
from django import forms
#from django.forms import ModelFor

# Create your tests here.

from .forms import create_enterprise_form, create_calification_form
from .models import Enterprise, Calification


class TestRunninE(TestCase):
	def test_c_e(self):
		e=Enterprise(name='test',town='ttest',sector='stest')
		e.save()
		self.assertEqual(e.name,'test')
		print("Your Enterprise was created succesfully, Test=OK")


class TestRunninC(TestCase):
	def test_c_c(self):
		enter=Enterprise(name='ntest',town='tttest',sector='sstest')
		enter.save()
		c=Calification(player='playertest',calification=10,enterprise=enter)
		c.save()
		self.assertEqual(c.enterprise,enter)
	
		print("Your Calification was created succesfully, Test=OK")

class TestRunninFE(TestCase):
	def test_e_f(self):
		
		data_form={'name' : 'test','town' : 'testt','sector' : 'stest'}
		form=create_enterprise_form(data=data_form)
		self.assertTrue(form.is_valid(),True)
		print("Enterprise form was created, Test=OK")

class TestRunninFC(TestCase):
	def test_c_f(self):
		em=Enterprise(name='ntest',town='tttest',sector='sstest')
		em.save()
		data_form={'player' : 'ptest','calification' : 10,'enterprise' : em.id}
		form=create_calification_form(data=data_form)
		self.assertTrue(form.is_valid(),True)
		print("Calification form was created, Test=OK")