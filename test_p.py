import codecs
from importlib import reload

import CourseModel_pb2
import json

# cat sitecustomize.py
# encoding=utf8


# parse json into python
with open('./test.json', 'rt', encoding='utf-8') as f:
    data = json.load(codecs.open('./test.json', 'r', 'utf-8-sig'))
# print(data['courses'][0]['subjects'][0]['topics'][0]['videos'])
# for i in range(len(data['courses'])):
# 	for j in range(len(data['courses'][0]['subjects'])):
# 		print(data['courses'][i]['subjects'][j]['subjectname'])


a = CourseModel_pb2.FullProto()  # coursesappend
for i in range(len(data['courses'])):
    b = CourseModel_pb2.CourseModelProto()
    b.courseID = data['courses'][i]['courseID']
    b.courseName = data['courses'][i]['coursename']
    for j in range(len(data['courses'][i]['subjects'])):
        c = CourseModel_pb2.SubjectModelProto()
        c.subjectID = data['courses'][i]['subjects'][j]['subjectID']
        c.subjectName = data['courses'][i]['subjects'][j]['subjectname']
        for k in range(len(data['courses'][i]['subjects'][j]['topics'])):
            d = CourseModel_pb2.TopicModelProto()
            d.topicID = data['courses'][i]['subjects'][j]['topics'][k]['topicID']
            d.topicName = data['courses'][i]['subjects'][j]['topics'][k]['topicname']
            # print(len(data['courses'][i]['subjects'][j]['topics'][k]['videos']))
            for l in range(len(data['courses'][i]['subjects'][j]['topics'][k]['videos'])):
                e = CourseModel_pb2.VideosModelProto()
                e.videoUID = data['courses'][i]['subjects'][j]['topics'][k]['videos'][l]['videoUID']
                e.videoName = data['courses'][i]['subjects'][j]['topics'][k]['videos'][l]['videoname']
                e.videoDescription = data['courses'][i]['subjects'][j]['topics'][k]['videos'][l]['videoDescription']
                e.videoURL = data['courses'][i]['subjects'][j]['topics'][k]['videos'][l]['videoURL']
                #e.videoThumbnailUID = data['courses'][i]['subjects'][j]['topics'][k]['videos'][l]['videoThumbnailUID']
                d.videos.extend([e])
            for m in range(len(data['courses'][i]['subjects'][j]['topics'][k]['ebooks'])):
                f = CourseModel_pb2.EbooksModelProto()
                f.ebookUID = data['courses'][i]['subjects'][j]['topics'][k]['ebooks'][m]['ebookUID']
                f.ebookName = data['courses'][i]['subjects'][j]['topics'][k]['ebooks'][m]['ebookname']
                f.ebookDescription = data['courses'][i]['subjects'][j]['topics'][k]['ebooks'][m]['ebookDescription']
                f.ebookURL = data['courses'][i]['subjects'][j]['topics'][k]['ebooks'][m]['ebookURL']
                f.ebookThumbnailUID = data['courses'][i]['subjects'][j]['topics'][k]['ebooks'][m]['ebookThumbnailUID']
                d.ebooks.extend([f])
                
            for t in range(len(data['courses'][i]['subjects'][j]['topics'][k]['tests'])):
                model_ref=CourseModel_pb2.TestModelProto()
                model_ref.testUID = data['courses'][i]['subjects'][j]['topics'][k]['tests'][t]['testUID']
                model_ref.testName = data['courses'][i]['subjects'][j]['topics'][k]['tests'][t]['testName']
                model_ref.testDescription = data['courses'][i]['subjects'][j]['topics'][k]['tests'][t]['testDescription']
                for n in range(len(data['courses'][i]['subjects'][j]['topics'][k]['tests'][t]['mcqs'])):
                    g = CourseModel_pb2.MCQsModelProto()
                    g.mcqUID = data['courses'][i]['subjects'][j]['topics'][k]['tests'][t]['mcqs'][n]['mcqUID']
                    g.isMcqSingleCorrect = data['courses'][i]['subjects'][j]['topics'][k]['tests'][t]['mcqs'][n]['isMcqSingleCorrect']
                    g.mcqQuestion = data['courses'][i]['subjects'][j]['topics'][k]['tests'][t]['mcqs'][n]['mcquestion']
                    for o in range(4):
                        g.mcqOptions.extend([data['courses'][i]['subjects'][j]['topics'][k]['tests'][t]['mcqs'][n]['mcqOptions'][o]])
                    for p in range(4):
                        g.mcqAnswer.extend([data['courses'][i]['subjects'][j]['topics'][k]['tests'][t]['mcqs'][n]['mcqAnswer'][p]])
                    g.mcqSolution = data['courses'][i]['subjects'][j]['topics'][k]['tests'][t]['mcqs'][n]['mcqSolution']
                    d.mcqs.extend([g])
                d.tests.extend([model_ref])
            c.topics.extend([d])
        b.subjects.extend([c])
    a.courses.extend([b])
           
            	
                

            
        
    # assert len(b.subjects) == 2
    
# assert len(a.courses) == 2

# print(a.SerializeToString())
file = open('proto_test.txt', 'wb')
file.write(a.SerializeToString())
file.close()
with open('proto_test.txt', 'rb') as qwer:
    ewq = CourseModel_pb2.FullProto()
    ewq.ParseFromString(qwer.read())
    # assert len(ewq.courses) == 2
    # for i in range(0, len(ewq.courses)):
        # assert len(ewq.courses[i].subjects) == 2


