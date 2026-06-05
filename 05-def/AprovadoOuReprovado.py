#Vou criar uma simples função de aprovado ou reprovado

def vareficar_notas(nota):
    if nota >= 7:
        return "Aprovado"
    elif nota <= 5:
        return "Reprovado"
    else:
        return "Digite apenas números"
    
resultado = vareficar_notas(10)

print(resultado)