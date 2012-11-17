class Tecla:
  def valor_de(self, letra):
    conjunto = self._conjunto_para(letra)
    return conjunto[len(conjunto)-1]

  def qtd_toques(self, letra):
    letras = self._conjunto_para(letra)
    return letras.find(letra)+1

  def _conjunto_para(self, letra):
    if(letra == "1"):
      return "1"
    if(letra in "abc2"):
      return "abc2"
    if(letra in "def3"):
      return "def3"
    if(letra in "ghi4"):
      return "ghi4"
    if(letra in "jkl5"):
      return "jkl5"
    if(letra in "mno6"):
      return "mno6"
    if(letra in "pqrs7"):
      return "pqrs7"
    if(letra in "tuv8"):
      return "tuv8"
    if(letra in "wxyz9"):
      return "wxyz9"
    if(letra in " 0"):
      return " 0"
class SMS:

  def converter(self,msg):
    tecla = Tecla()
    resultado = ''
    ultima_tecla = ""
    for c in msg:
      proxima_tecla = tecla.valor_de(c)
      if (proxima_tecla ==  ultima_tecla):
        resultado += "_"
      resultado += proxima_tecla * tecla.qtd_toques(c)
      ultima_tecla = proxima_tecla
    return resultado

    




  
    
