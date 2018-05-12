
# import m3u8
import download_tool

# exemple m3u8 link, change it as your wish
link1 = 'http://213.246.39.124:8081/live/adm/playlist_dvr.m3u8'

# change to your own path
path = '/Users/jialiangliu/Documents/2018IMT/PIST-projet4/project/data/play1/'

# def reader(link):
#
#     m3u8_obj = m3u8.load(link)
#     print "segments: " , m3u8_obj.segments
#     print "target_duration: " , m3u8_obj.target_duration
#
#     print 'keys len: ', len(m3u8_obj.keys)
#     for key in m3u8_obj.keys:
#         if key:  # First one could be None
#             print "uri: " , key.uri
#             print "method: ", key.method
#             print "iv: " , key.iv

if __name__ == '__main__':
    # print 'Read from a url : '
    # reader(link1)

    print '\r\n =====Download Start======'

    #print 'Read from a file :'
    #reader(file)

    download_tool.download_ts_file(link1, 1, path)

