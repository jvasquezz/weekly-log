import os
import xml.etree.cElementTree as xml
from xml.etree import ElementTree
from xml.etree.ElementTree import Element
from xml.dom import minidom
import xml.dom.pulldom as pulldom
import re

try:
    tree = xml.parse('db.xml')
except IOError as e:
    tmproot = xml.Element('courses')
    tmpcourse = xml.Element('course')
    tmproot.append(tmpcourse)
    tmpsub = xml.SubElement(tmpcourse, 'name')
    tmpsub2 = xml.SubElement(tmpcourse, 'time_invested')
    tree = xml.ElementTree(tmproot)
    with open("db.xml", "w") as fh:
        tree.write(fh)

root = tree.getroot()
course = xml.Element('course')
root.append(course)

# root = xml.Element('courses')
# course = xml.Element('course')
# root.append(course)


print ('You can input your hours worked per session,\nI\'ll keep track of them for you')
print ('Please pick a course from the following list?\n')
course_options = [line.rstrip('\n') for line in open('list.txt')]
for opt in course_options:
    print opt
print '\n0. See logs'

index = raw_input('\nYour choice: ')

if int(index) is 0:
    print 'zero'
else:
    session_t = raw_input('\nThis session time in hours: ')

    index = int(index)-1
    selected = course_options[int(index)]
    course_title = selected[:0] + selected[0 + 3:]

    '''
    increments time count
    '''
    i = 0
    for name in root.iter('name'):
        for time in root.iter('time_invested'):
            if name.text == course_title:
                i = i + 1
                time.text = int(time.text) + int(session_t)


    if not i:


    # for a in root.findall(course_title):
        # print a.text
    # root.findall("")
    # i = 0
    # for course in root.iter('name'):
    #     i = i + 1
    #     if course.text == course_title:
    #         print 'break'
    #         break
    #
    # print i
    # course_name = xml.SubElement(course, "name")
    # course_name.text = course_title
    #
    # course_time = xml.SubElement(course, "time_invested")
    # course_time.text = session_t
    #
    # tree.write('db.xml')

    print 'added '+session_t+' hours invested to ' + course_title

