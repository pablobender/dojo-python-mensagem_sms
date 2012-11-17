import unittest
import sms

class TestTecla(unittest.TestCase):
   def test_tecla_de_a_he_2(self):
     tecla = sms.Tecla()
     numero_a_ser_digitado = tecla.valor_de('a')
     self.assertEquals('2', numero_a_ser_digitado)

   def test_tecla_de_b_he_2(self):
     tecla = sms.Tecla()
     numero_a_ser_digitado = tecla.valor_de('b')
     self.assertEquals('2', numero_a_ser_digitado)

   def test_tecla_de_d_he_3(self):
     tecla = sms.Tecla()
     numero_a_ser_digitado = tecla.valor_de('d')
     self.assertEquals('3', numero_a_ser_digitado)

   def test_tecla_de_e_he_3(self):
     tecla = sms.Tecla()
     numero_a_ser_digitado = tecla.valor_de('e')
     self.assertEquals('3', numero_a_ser_digitado)
   
   def test_tecla_de_f_he_3(self):
     tecla = sms.Tecla()
     numero_a_ser_digitado = tecla.valor_de('f')
     self.assertEquals('3', numero_a_ser_digitado)

   def test_tecla_de_1_he_1(self):
     tecla = sms.Tecla()
     numero_a_ser_digitado = tecla.valor_de('1')
     self.assertEquals('1', numero_a_ser_digitado)

   def test_tecla_de_5_he_5(self):
     tecla = sms.Tecla()
     numero_a_ser_digitado = tecla.valor_de('5')
     self.assertEquals('5', numero_a_ser_digitado)

   ###############################################

   def test_letra_a_digita_1x(self):
     tecla = sms.Tecla()
     qtd = tecla.qtd_toques('a')
     self.assertEquals(1, qtd)

   def test_letra_b_digita_2x(self):
     tecla = sms.Tecla()
     qtd = tecla.qtd_toques('b')
     self.assertEquals(2, qtd)
  
   def test_letra_c_digita_3x(self):
     tecla = sms.Tecla()
     qtd = tecla.qtd_toques('c')
     self.assertEquals(3, qtd)

   def test_letra_1_digita_1x(self):
     tecla = sms.Tecla()
     qtd = tecla.qtd_toques('1')
     self.assertEquals(1, qtd)
  
class TestSms(unittest.TestCase):
  
  def test_a_eh_2(self):
    self.sms = sms.SMS()
    sequencia = self.sms.converter('a')
    self.assertEquals('2', sequencia)

  def test_b_eh_2(self):
    self.sms = sms.SMS()
    sequencia = self.sms.converter('b')
    self.assertEquals('22', sequencia)
  
  def test_q_eh_7(self):
    self.sms = sms.SMS()
    sequencia = self.sms.converter('q')
    self.assertEquals('77', sequencia)

  def test_ad_eh_23(self):
    self.sms = sms.SMS()
    sequencia = self.sms.converter('ad')
    self.assertEquals('23', sequencia)
  
  def test_aa_eh_2_2(self):
    self.sms = sms.SMS()
    sequencia = self.sms.converter('aa')
    self.assertEquals('2_2', sequencia)

  def test_hudson_eh_48376_6(self):
    self.sms = sms.SMS()
    sequencia = self.sms.converter('hudson')
    self.assertEquals('448837777666_66', sequencia)
  def test_ola_mundo_eh_66655520688663666(self):
    self.sms = sms.SMS()
    sequencia = self.sms.converter('ola mundo')
    self.assertEquals('66655520688663666', sequencia)

  def test_python_e_10_eh_7999844666_660330100(self):
    self.sms = sms.SMS()
    sequencia = self.sms.converter('python e 10')
    self.assertEquals('7999844666_660330100', sequencia)

  def test_150_eh_1555500(self):
    self.sms = sms.SMS()
    sequencia = self.sms.converter('150')
    self.assertEquals('1555500', sequencia)

