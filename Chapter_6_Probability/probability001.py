import enum, random, math
SQRT_TWO_PI = math.sqrt(2*math.pi)

#Enum é um conjunto tipado de valores enumarados
#que deixa o código mais descritivo e legível

class Kid(enum.Enum):
  BOY = 0
  GIRL = 1

def random_kid() -> Kid:
  return random.choice([Kid.BOY, Kid.GIRL])

def uniform_pdf(x: float) -> float:
  return 1 if 0<= x < 1 else 0

def uniform_cdf(x:float) ->float:
  """Retorna a probabilidade de uma variável aleatória ser <=x"""
  if x < 0:  return 0 # a aleatória uniforme nunca e menor que 0
  elif x<1: return x #Ex.: P(X<=0.4) = 0.4
  else: return 1 #a aleatoria uniforme sempre e menor que 1

def normal_pdf(x:float, mu:float = 0, sigma:float = 1)->float:
  return(math.exp(-(x-mu)**2/2/sigma**2)/(SQRT_TWO_PI*sigma))

def normal_cdf(x: float, mu:float = 0, sigma:float =1)->float:
  return(1+math.erf((x-mu) / math.sqrt(2)/sigma)) /2


import matplotlib.pyplot as plt
#Plotemos algumas funções de densidade de probabilidade (PDFs) para conferir seu visual
xs=[x/10.0 for x in range (-50,50)]
plt.plot(xs,[normal_pdf(x,sigma=1)for x in xs],'-',label='mu=0, sigma=1')
plt.plot(xs,[normal_pdf(x,sigma=0.5)for x in xs],':',label='mu=0, sigma=0.5')
plt.plot(xs,[normal_pdf(x,sigma=2)for x in xs],'--',label='mu=0, sigma=2')
plt.plot(xs,[normal_pdf(x,mu=-1)for x in xs],'-.',label='mu=-1, sigma=1')
plt.legend()
plt.title("Várias PDFs normais")
plt.show()
#------------------------------------------
#Plotemos algumas funções de distribuição cumulativa(CDFs) agora

plt.plot(xs,[normal_cdf(x,sigma=1)for x in xs],'-',label='mu=0, sigma=1')
plt.plot(xs,[normal_cdf(x,sigma=0.5)for x in xs],':',label='mu=0, sigma=0.5')
plt.plot(xs,[normal_cdf(x,sigma=2)for x in xs],'--',label='mu=0, sigma=2')
plt.plot(xs,[normal_cdf(x,mu=-1)for x in xs],'-.',label='mu=-1, sigma=1')
plt.legend(loc = 4) # Canto inferior direito
plt.title("Várias CDFs normais")
plt.show()