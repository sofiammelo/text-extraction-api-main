from werkzeug.datastructures import FileStorage
from app.models.Document import Document
from pypdf import PdfReader
from pypdf.errors import PdfReadError
import re

from app.extensions import db
class ExtractionService:

    def extraction_method_service(self, pdf_file: FileStorage) -> Document: 
        self.validar_pdf(pdf_file)
        texto_extraido = self.extrair_texto(pdf_file)
        texto_limpo = self.limpar_texto(texto_extraido)

        document = Document(
            name = pdf_file.filename,
            content = texto_limpo,
            source_type="pdf"
        )

        db.session.add(document)
        db.session.commit()

        return document

    def validar_pdf(self, pdf_recebido: FileStorage) -> None:
        try:
            leitor = PdfReader(pdf_recebido.stream)

            numero_paginas = len(leitor.pages)
            if numero_paginas == 0:
                raise ValueError("O PDF está vazio ou não possui páginas.")

        except PdfReadError:
            raise ValueError("O arquivo não é um PDF válido ou está corrompido.")

        except Exception as erro:
            raise ValueError(f"Erro ao validar o PDF: {erro}")

    def extrair_texto(self, pdf_valido: FileStorage) -> str:
        try:
            pdf_valido.stream.seek(0) 
            leitor = PdfReader(pdf_valido.stream)
            texto_completo = ""

            for pagina in leitor.pages:
                texto_pagina = pagina.extract_text()

                if texto_pagina:
                    texto_completo += texto_pagina

            if not texto_completo.strip():
                raise ValueError("Não foi possível extrair texto do PDF.")

            return texto_completo

        except Exception as erro:
            raise ValueError(f"Erro ao extrair texto do PDF: {erro}")

    def limpar_texto(self, texto_extraido: str) -> str:
        texto = texto_extraido.replace("\t", " ")
        texto = re.sub(r"[ ]{2,}", " ", texto)
        texto = re.sub(r"\n{3,}", "\n\n", texto)

        return texto.strip()