from pathlib import Path
import layoutparser as lp  # For visualization
from vila.pdftools.pdf_extractor import PDFExtractor
from vila.predictors import HierarchicalPDFPredictor
import os

if __name__ == '__main__':
    pdf_extractor = PDFExtractor("pdfplumber")

    vision_model = lp.EfficientDetLayoutModel("lp://PubLayNet")
    pdf_predictor = HierarchicalPDFPredictor.from_pretrained("allenai/hvila-block-layoutlm-finetuned-docbank")

    type_list = os.getenv('TYPES', 'paragraph').split(',')

    for path in Path('reports').rglob('*.pdf'):
        page_tokens, page_images = pdf_extractor.load_tokens_and_image(path.absolute())

        output_file_path = 'output/' + path.name[:-3] + 'txt'

        if Path(output_file_path).is_file():
            print('[!] File ' + output_file_path + ' already exists')
        else:
            with open(output_file_path, 'w') as outfile:
                for idx, page_token in enumerate(page_tokens):
                    blocks = vision_model.detect(page_images[idx])
                    page_token.annotate(blocks=blocks)
                    pdf_data = page_token.to_pagedata().to_dict()
                    predicted_tokens = pdf_predictor.predict(pdf_data, page_token.page_size)
                    for block in predicted_tokens._blocks:
                        if block.type in type_list:
                            outfile.write(block.text + ' ')
            print(path.name + 'successfully processed')
