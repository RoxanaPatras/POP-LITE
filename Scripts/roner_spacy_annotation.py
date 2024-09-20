import xml.etree.ElementTree as ET
import re
import os
import roner
import spacy


def tei_to_txt(tei_file, txt_file):
    tree = ET.parse(tei_file)
    root = tree.getroot()

    text_content = ""
    for elem in root.iter():
        if elem.text:
            text_content += elem.text + " "
        if elem.tail:
            text_content += elem.tail + " "

    text_content = re.sub(r'\s+', ' ', text_content)
    text_content = text_content.strip()

    with open(txt_file, 'w', encoding='utf-8') as f:
        f.write(text_content)


def apply_ner_and_pos(txt_file, ner_output_file, pos_output_file):
    ner = roner.NER()

    nlp = spacy.load("ro_core_news_sm")

    with open(txt_file, 'r', encoding='utf-8') as f:
        text = f.read()

    entities = ner(text)

    doc = nlp(text)

    with open(ner_output_file, 'w', encoding='utf-8') as f:
        for output_text in entities:
            for word in output_text['words']:
                f.write(f"{word['text']:>20} = {word['tag']}\n")

    with open(pos_output_file, 'w', encoding='utf-8') as f:
        for token in doc:
            f.write(f"{token.text:>20} = {token.pos_}\n")


def process_files(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith('.xml'):
            tei_file = os.path.join(input_dir, filename)
            txt_file = os.path.join(output_dir, filename[:-4] + '.txt')
            ner_file = os.path.join(output_dir, filename[:-4] + '_ner.txt')
            pos_file = os.path.join(output_dir, filename[:-4] + '_pos.txt')

            tei_to_txt(tei_file, txt_file)

            apply_ner_and_pos(txt_file, ner_file, pos_file)

            print(f"Processed {filename}")


process_files("Corpus", "Annotated Corpus")
