import camelot

# Arquivo que você já baixou
pdf_file = "C:/Users/Educação/Downloads/Diário Oficial da Prefeitura do Recife.pdf"


# Extrair tabelas das páginas (nesse caso o PDF já tem só pág. 5 e 6, mas vou manter por segurança)
tables = camelot.read_pdf(pdf_file, pages="all", flavor="stream")

print(f"Tabelas encontradas: {len(tables)}")

# Salvar todas as tabelas em Excel
for i, table in enumerate(tables):
    table.to_excel(f"tabela_{i+1}.xlsx")
    print(f"Tabela {i+1} salva em tabela_{i+1}.xlsx")

