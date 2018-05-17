# PubDetector-
Pub Detector for live video 

Requires: urlparse, urllib2 (install by using 'pip install xxx') 
For using the download tool : After change your own path of output file and execute 
  >python reader.py

Output like : 


>
>seg:  chunks_dvr.m3u8?nimblesessionid=18071173 <br/>
>===== Trunk url: ===  http://213.246.39.124:8081/live/adm/chunks_dvr.m3u8?nimblesessionid=18071173 <br/>
>line:  #EXTM3U  <br/>
>line:  #EXT-X-VERSION:3 <br/>
>line:  #EXT-X-ALLOW-CACHE:NO<br/>
>line:  #EXT-X-TARGETDURATION:8<br/>
>line:  #EXT-X-MEDIA-SEQUENCE:1<br/>
>line:  #EXTINF:5.906,<br/>
>line:  dvr_v_p1_10926305.ts?nimblesessionid=18071173<br/>
>part 1 done!<br/>
>line:  #EXTINF:7.074,<br/>
>line:  dvr_v_p1_10932211.ts?nimblesessionid=18071173<br/>
>part 2 done!<br/>
>line:  #EXTINF:6.073,<br/>
>line:  dvr_v_p1_10939285.ts?nimblesessionid=18071173<br/>
>..... 
>
