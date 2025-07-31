from django.core.management.base import BaseCommand
from recommend.utils.pdf_rag import process_pdf_to_faiss

class Command(BaseCommand):
    help = 'Process a PDF and create FAISS index'

    def handle(self, *args, **kwargs):
        process_pdf_to_faiss("recommend/docs/Academic_Calendar-145-158.pdf")
        self.stdout.write(self.style.SUCCESS('PDF processed and FAISS index created.'))
