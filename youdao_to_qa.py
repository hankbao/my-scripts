#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import pdb
import sys
import xml.dom.minidom as minidom

def print_usage():
    print "Usage: " + sys.argv[0].split('/')[-1] + " input_file"

def parse_input_xml(input_file):
    xmldoc = minidom.parse(input_file)
    rootElem = xmldoc.documentElement
    assert rootElem.tagName == "wordbook"

    items = rootElem.getElementsByTagName("item")
    qa_list = []
    for item in reversed(items):
        qa = {}
        childNodes_word = item.getElementsByTagName("word")[0].childNodes
        if len(childNodes_word) > 0:
            qa["word"] = childNodes_word[0].data
        else:
            qa["word"] = u""
        childNodes_trans = item.getElementsByTagName("trans")[0].childNodes
        if len(childNodes_trans) > 0:
            qa["trans"] = childNodes_trans[0].data
        else:
            qa["trans"] = u""
        childNodes_phonetic = item.getElementsByTagName("phonetic")[0].childNodes
        if len(childNodes_phonetic) > 0:
            qa["phonetic"] = childNodes_phonetic[0].data
        else:
            qa["phonetic"] = u""
        qa_list.append(qa)

    return qa_list
        

def print_qa_list(qa_list):
    for qa in qa_list:
        print (u"Q: " + qa["word"]).encode('utf-8')
        print (u"A: " + qa["phonetic"]).encode('utf-8')
        for tran in qa["trans"].splitlines():
            print (u"A: " + tran).encode('utf-8')
        print u""

    return True


if __name__ == "__main__":
    #pdb.set_trace()
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(2);

    input_file = sys.argv[1]
    qa_list = parse_input_xml(input_file)
    result = len(qa_list) > 0
    if not result:
        print "fail to create output."
    else:
        print_qa_list(qa_list)

    sys.exit(not result)
