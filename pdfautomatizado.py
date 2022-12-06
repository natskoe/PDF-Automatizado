#!/usr/bin/env python
# coding: utf-8


descricaoProjeto = input("Insira a descrição do projeto: ")
horasEstimadas = input("Insira o total de horas estimadas: ")
valorHora = input("Insira o valor da hora trabalhada: ")
prazoEstimado = int(horasEstimadas)/24
valorTotal = int(horasEstimadas)*int(valorHora)

if prazoEstimado == round(prazoEstimado):
      dias = prazoEstimado
else: 
      dias = round(prazoEstimado + 0.5)

print("---------------------------------" +
      "\nDescrição: "+ descricaoProjeto + "\nHoras estimadas: " + horasEstimadas + "\nValor por hora: " + 
      valorHora + "\nPrazo estimado em dias: " + str(dias) + "\nValor total: " + str(valorTotal))

from fpdf import FPDF

pdf = FPDF()

pdf.add_page()
pdf.set_font("Arial")

pdf.image("template.png", x = 0, y = 0)
pdf.text(115, 145, descricaoProjeto)
pdf.text(115, 160, horasEstimadas + "h")
pdf.text(115, 175, valorHora)
pdf.text(115, 190, str(dias) + " dias")
pdf.text(115, 205, str(valorTotal))

pdf.output("Orçamento.pdf")

print("---------------------------\nOrçamento gerado com sucesso!")

