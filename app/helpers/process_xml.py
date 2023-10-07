import xmltodict, json


def process_xml_data(payload: bytes):
    return json.dumps(xmltodict.parse(
        xml_input=payload,
        process_namespaces=True,
        process_comments=True,
    ))
