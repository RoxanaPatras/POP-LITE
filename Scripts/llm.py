import os
from lxml import etree
from llama_cpp import Llama
import json

model_path = "D:/Meta-Llama-3.1-8B-Instruct-Q3_K_L.gguf"

llm = Llama(
    model_path=model_path,
    n_gpu_layers=-1,  # GPU acceleration
    seed=1337,  # specific seed
    n_ctx=2048,  # context window
    n_threads=4,
    n_batch=2048,
    verbose=False
)


def get_entities(sentence):
    output = llm.create_chat_completion(
        messages=[
            {
                "role": "system",
                "content": """Ești un excelent asistent pentru Named Entity Recognition! Trebuie să identifici entitățile din textul dat. Folosește următoarele etichete pentru entități: PER - Persoană, ORG - Organizație, LOC - Locație, GPE - Entitate politică, DATE - Dată, TIME - Timp, MONEY - Sume de bani, PERCENT - Procentaje, FAC - Facilități, EVENT - Evenimente, PRODUCT - Produse, NORP - Grupuri naționale, etnice sau religioase, LANGUAGE - Limbi, LAW - Legi, WORK_OF_ART - Opere de artă, QUANTITY - Cantități, ORDINAL - Ordinal, CARDINAL - Numerale cardinale, O - Altele."""
            },
            {
                "role": "user",
                "content": "Identifică toate entitățile pentru următorul text:" + sentence
            }
        ],
        response_format={
            "type": "json_object",
            "schema": {
                "type": "object",
                "properties": {
                    "entities": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "word": {"type": "string"},
                                "entity": {"type": "string"}
                            },
                            "required": ["word", "entity"]
                        }
                    }
                }
            }

        }
    )
    return output["choices"][0]["message"]["content"]


def process_sentence(sentence):
    entities = json.loads(get_entities(sentence)).get('entities', [])
    word_entities = {entity['word']: entity['entity'] for entity in entities}
    print(word_entities)
    new_sentence = ''

    for word in sentence.split():
        entity = word_entities.get(word, 'O')
        new_sentence += f'{word}/{entity} '

    return new_sentence.strip()


def process_tei_file(input_file, output_file):
    parser = etree.XMLParser(remove_blank_text=True)
    tree = etree.parse(input_file, parser)
    root = tree.getroot()

    for element in root.iter():
        if element.tag == '{http://www.tei-c.org/ns/1.0}p':
            sentence = ''.join(element.itertext()).strip()
            new_sentence = process_sentence(sentence)
            element.clear()
            element.text = f"<s>${new_sentence}</s>"

    tree.write(output_file, pretty_print=True, encoding='utf-8', xml_declaration=True)


def process_directory(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith('.xml'):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, f'processed_{filename}')
            process_tei_file(input_path, output_path)
            print(f'Processed {filename}')


process_directory('Corpus POP-LITE_extensie', 'Processed Corpus POP-LITE_extensie')
