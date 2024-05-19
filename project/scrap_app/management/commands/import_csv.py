import csv
from django.core.management.base import BaseCommand
from scrap_app.models import Quote

class Command(BaseCommand):
    help = 'Import CSV data into the database'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        csv_file_path = options['csv_file']

        try:
            with open(csv_file_path, 'r') as csv_file:
                csv_reader = csv.reader(csv_file)
                # Skip header if needed
                next(csv_reader)
                for row_number, row in enumerate(csv_reader, start=2):  # Start counting from row 2
                    try:
                        # Ensure the row has at least two elements (quote and author)
                        if len(row) >= 2:
                            quote_text = row[0].strip()  
                            author_name = row[1].strip() 
                            Quote.objects.create(quote=quote_text, author=author_name)
                        else:
                            self.stderr.write(self.style.ERROR(f"Skipped row {row_number}: Insufficient data"))
                    except Exception as e:
                        self.stderr.write(self.style.ERROR(f"Error processing row {row_number}: {e}"))
        except FileNotFoundError:
            self.stderr.write(self.style.ERROR(f"File not found: {csv_file_path}"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error: {e}"))
