import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
import json
import os


file_path_input = "/veld/input/in.json"
file_path_output = "/veld/output/out.xml"


def dict_to_xml(d, node_current=None):
    if node_current is None:
        node_current = ET.Element("root")
    k_v_pairs = None
    if type(d) is dict:
        k_v_pairs = [(ET.Element(k), v) for k, v in d.items()]
    elif type(d) is list:
        k_v_pairs = [(ET.Element("li"), v) for v in d]
    for node_k, v in k_v_pairs:
        if type(v) is dict or type(v) is list:
            dict_to_xml(v, node_k)
        else:
            node_k.text = str(v)
        node_current.append(node_k)
    return node_current


if __name__ == "__main__":
    print(f"loading from: {file_path_input}")
    with open(file_path_input, "r") as fi:
        d = json.load(fi)
        print(f"d: {d}")
        xml_content = dict_to_xml(d)
        xml_str = minidom.parseString(ET.tostring(xml_content)).toprettyxml(indent="  ")
        print(f"xml_str: {xml_str}")
        print(f"writing to: {file_path_output}")
        with open(file_path_output, "w") as fo:
            fo.write(xml_str)

