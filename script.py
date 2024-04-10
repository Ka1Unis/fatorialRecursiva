def fatorial(n):
  """
  Função recursiva para calcular o fatorial de um número.

  Argumentos:
    n: O número para calcular o fatorial.

  Retorno:
    O fatorial de n.
  """

  # Casos base
  if n == 0:
    return 1
  elif n == 1:
    return 1

  # Caso recursivo
  else:
    return n * fatorial(n - 1)

# Exemplo de uso
numero = 5
resultado = fatorial(numero)
print(f"O fatorial de {numero} é {resultado}")
