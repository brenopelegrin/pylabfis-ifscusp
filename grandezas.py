import math

def sin(x: float, deltax=0.0, und=""):
  return Grandeza(medida=math.sin(x), incerteza=math.cos(x)*deltax, und="")

def cos(x: float, deltax=0.0, und=""):
  return Grandeza(medida=math.cos(x), incerteza=math.sin(x)*deltax, und="")

class Grandeza:
  def __init__(self, medida: float, incerteza=0.0, unidade="", casasdecimais=16):
    self.casasdecimais = casasdecimais
    self.medida = round(medida, casasdecimais)
    self.incerteza = round(incerteza, casasdecimais)
    self.unidade = unidade

  def latex(self, fatorconversao=1):
    if fatorconversao != 1:
      string = r"({} \pm {}) \times {} \text".format(self.medida*fatorconversao, self.incerteza*fatorconversao, 1/fatorconversao)+'{ '+self.unidade+'}'
    else:
      string = r"({} \pm {}) \text".format(self.medida, self.incerteza)+'{ '+self.unidade+'}'
    return string

  def readable(self, fatorconversao=1):
    if fatorconversao != 1:
      string = r"({} +- {}) * {} {}".format(self.medida*fatorconversao, self.incerteza*fatorconversao, 1/fatorconversao, self.unidade)
    else:
      string = r"({} +- {}) {}".format(self.medida, self.incerteza, self.unidade)
    return string

  def __add__(self, other):
    medida = self.medida + other.medida
    incerteza = self.incerteza + other.incerteza
    unidade=""

    return Grandeza(medida, incerteza, unidade)

  def __sub__(self, other):
    medida = self.medida - other.medida
    incerteza = self.incerteza + other.incerteza
    unidade=""

    return Grandeza(medida, incerteza, unidade)

  def __mul__(self, other):
    if isinstance(other, Grandeza):
      medida = self.medida * other.medida
      incerteza = self.medida*other.incerteza + other.medida*self.incerteza
      unidade=""

      return Grandeza(medida, incerteza, unidade)
    elif isinstance(other, float):
      medida = self.medida * other
      incerteza = self.medida*abs(other)
      unidade=""
      return Grandeza(medida, incerteza, unidade)
    else:
      raise TypeError("A biblioteca só suporta multiplicação de Grandeza por Grandeza ou float.")
  def __rmul__(self, other):
      print("primeiro argumento: {} / segundo argumento: {}".format(self.medida, other))
      medida = self.medida*other
      incerteza = abs(other)*self.incerteza
      unidade=""
      return Grandeza(medida, incerteza, unidade)

  def __truediv__(self, other):
    medida = self.medida / other.medida
    incerteza = (self.medida*other.incerteza + other.medida*self.incerteza)/(other.medida**2)
    unidade=""

    return Grandeza(medida, incerteza, unidade)

  def __pow__(self, other):
    if isinstance(other, float):
      medida = self.medida**other
      incerteza = other*(self.medida**(other-1))*self.incerteza
      unidade = ""
      return Grandeza(medida, incerteza, unidade)

    else:
      raise Exception("Essa classe só suporta expoentes floats.")

  def pow_cte(self, expoente: float):
    medida = self.medida ** expoente
    incerteza = (expoente-1)*(self.medida**(expoente-1))*self.incerteza
    unidade = self.unidade

    return Grandeza(medida, incerteza, unidade)
