
from urlparse import urlparse
import sys, urllib2
# url_trunk = 'http://213.246.39.124:8081/live/adm/dvr_v_p1_10974620.ts?nimblesessionid=16009971'
# http://213.246.39.124/live/adm/chunks_dvr.m3u8?nimblesessionid=16011912

segment_list = []

def download_ts_file(url, channel_id, path):


    urlgroup = urlparse(url)

    print "parse result:" , urlgroup , ' \r\n'

    domain = ""

    trunk_path =  urlgroup.netloc + '/'.join(urlgroup.path.split('/')[0:-1])

    response = urllib2.urlopen(url)
    content = response.read()



    m3u8_content = content

    print "--- start ---- \r\n"
    if not m3u8_content or not m3u8_content.startswith("#"):
        return None

    segments = m3u8_content.split("\n")

    valid_segment = None

    for segment in segments:
        if not segment or segment.startswith("#"):
            continue
        valid_segment = segment.replace("\r", "").replace("../", "").strip()
        break



    print 'seg: ' , valid_segment

    if valid_segment:
        if valid_segment not in segment_list:
            segment_list.append(valid_segment)
        else:
            return None

        if valid_segment.find('.m3u8') > 0 and valid_segment.find('.ts') < 0:
            if valid_segment.find("http:") < 0:
                elements = domain.split('/')
                for i in range(0, len(elements)):
                    trunk_url = "http://" + trunk_path + '/'.join(elements[0: len(elements) - i]) + '/' + valid_segment
                    print "===== Trunk url: === " ,trunk_url
                    content = urllib2.urlopen(trunk_url)

                    line = content.readline().strip()
                    count = 0
                    while line:
                        print 'line: ' , line
                        if not line.startswith('#') and line != '':
                            ts = urllib2.urlopen("http://" + trunk_path +'/' + line)
                            with open("live.mp4", 'ab') as code:
                                code.write(ts.read())
                            count += 1
                            print 'part %s done!' % count
                        line = content.readline().strip()

        else:
            if valid_segment.find("http:") < 0:
                elements = domain.split('/')
                for i in range(0, len(elements)):
                    trunk_url = "http://" + trunk_path + '/'.join(elements[0: len(elements) - i]) + '/' + valid_segment

                    file = urllib2.urlopen(trunk_url)
                    data = file.read()
                    with open("live.mp4", "wb") as code:
                        code.write(data)
                    if file:
                        return file
            file_name = urllib2.download_file(valid_segment, path + "live.mp4")
            if file_name:
                return file_name
    return None