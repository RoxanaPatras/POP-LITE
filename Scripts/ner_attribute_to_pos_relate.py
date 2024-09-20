import xml.etree.ElementTree as ET
from collections import defaultdict
import os


def remove_namespace(tree):
    for elem in tree.iter():
        if '}' in elem.tag:
            elem.tag = elem.tag.split('}', 1)[1]
    return tree


def parse_and_check_xml(xml_file, word_ner_file, output_file):
    word_ner_dict = defaultdict(list)
    with open(word_ner_file, 'r', encoding='utf-8') as file:
        for line in file:
            word, ner = line.strip().split(' = ')
            word_ner_dict[word.lower()].append(ner)

    def process_element(element, word_ner_dict):
        try:
            if element.text:
                element_text_lower = element.text.lower()
                for word, ner_list in word_ner_dict.items():
                    if word in element_text_lower and ner_list:
                        ner = ner_list.pop(0)
                        element.set('ner', ner)
                        # print(
                        #     f"Added NER '{ner}' to <{element.tag}> tag for word '{word}': {ET.tostring(element, encoding='unicode')}")
                        if not ner_list:  # If no more NER tags for this word, remove it from the dict
                            del word_ner_dict[word]
                            print(f"Removed '{word}' from word_ner_dict")
                        return True
        except ET.ParseError:
            print(f"Skipping malformed element: {element}")
        return False

    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse(xml_file, parser=parser)

    tree = remove_namespace(tree)
    root = tree.getroot()

    for element in root.iter():
        if element.tag in ['w', 'pc']:
            process_element(element, word_ner_dict)

    tree.write(output_file, encoding='utf-8', xml_declaration=True)

    print("\nRemaining words in word_ner_dict:")
    for word, ner_list in word_ner_dict.items():
        for ner in ner_list:
            print(f"{word} = {ner}")



def parse_from_dir(xml_dir):

    if not os.path.exists('output'):
        os.makedirs('output')

    for filename in os.listdir(xml_dir):
        if filename.endswith(".xml"):
            print(f"\nParsing file: {filename}")
            parse_and_check_xml(os.path.join(xml_dir, filename), 'Corpus Pop-Lite Pos Tagged_Ner Tagged/Versiune roner + spacy/' + filename.replace('.xml', '_ner.txt'),
                                'output/' + filename)

parse_from_dir('Corpus Pop-Lite Pos Tagged_Ner Tagged/Versiune RELATE')
