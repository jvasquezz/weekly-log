import os
import xml.etree.cElementTree as xml
from xml.etree import ElementTree
from xml.etree.ElementTree import Element
from xml.dom import minidom
import xml.dom.pulldom as pulldom
import re

def take_input():
    print ('You can input your hours worked per session,\nI\'ll keep track of them for you')
    print ('Please pick a course from the following list?\n')
    course_options = [line.rstrip('\n') for line in open('list.txt')]
    for opt in course_options:
        print opt
    print '\n0. See logs'
    ind = raw_input('\nYour choice: ')
    sn_t = raw_input('\nThis session time in hours: ')
    return ind, sn_t,course_options

def get_title(iindex, oopts):
    iindex = int(iindex)-1
    select = oopts[int(iindex)]
    tit = select[:0] + select[0 + 3:]
    return tit

def set_attributes(rroot, elem, ttitle, ssession_t):
    rroot.append(elem)
    '''new course to add'''
    course_name = xml.SubElement(elem, "name")
    course_name.text = ttitle
    '''new time to add'''
    course_time = xml.SubElement(elem, "time_invested")
    course_time.text = ssession_t

try:
    tree = xml.parse('db.xml')
    root = tree.getroot()

    '''take user's input '''
    index, session_t, course_opts = take_input()

    if int(index) is 0:
        print 'zero'
    else:
        course_title = get_title(index, course_opts)

        ''' increments hours '''
        i = 0
        for name in root.iter('name'):
            for time in root.iter('time_invested'):
                if name.text == course_title:
                    i = 1
                    time.text = str(int(time.text) + int(session_t))
                    name.text = name.text
                    break


        if not i:
            course = xml.Element('course')

            set_attributes(root, course, course_title, session_t)

            # root.append(course)
            # '''new course to add'''
            # course_name = xml.SubElement(course, "name")
            # course_name.text = course_title
            # '''new time to add'''
            # course_time = xml.SubElement(course, "time_invested")
            # course_time.text = session_t

        tree.write('db.xml')

        print 'added '+session_t+' hours invested to ' + course_title

except IOError as e:
    i, time, opts = take_input()

    fst_root = xml.Element('courses')
    fst_course = xml.Element('course')
    title = get_title(i, opts)

    set_attributes(fst_root, fst_course, title, time)

    # fst_root.append(fst_course)
    # name_se = xml.SubElement(fst_course, 'name')
    # name_se.text = title
    # time_se = xml.SubElement(fst_course, 'time_invested')
    # time_se.text = time

    tree = xml.ElementTree(fst_root)

    with open("db.xml", "w") as fh:
        tree.write(fh)

    print 'added '+time+' hours invested to ' + title

