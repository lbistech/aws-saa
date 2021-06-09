
import time
import requests

s3_object_url = 'https://lbistech-cf-lab.s3.amazonaws.com/bloomberg_animationglut-1280x600.jpg'
cloudfront_object_url = 'http://d2qu1e5bex56jz.cloudfront.net/bloomberg_animationglut-1280x600.jpg'


def downloadFile(url):
    start_time = time.time()
    response = requests.get(url)
    end_time = time.time() - start_time
    return round(float(end_time), 3)


s3List = []
cFList = []
iteration_size = 5

for x in range(0, iteration_size):
    print("S3 File Download Iteration: %d" % (x+1))
    s3List.append(downloadFile(s3_object_url))

for x in range(0, iteration_size):
    print("CloudFront File Download Iteration: %d" % (x+1))
    cFList.append(downloadFile(cloudfront_object_url))

print("<---Test Complete--->")
print("Average Download Time For S3: %.3f Seconds" % (sum(s3List)/iteration_size))
print("Average Download Time For CloudFront: %.3f Seconds" % (sum(cFList)/iteration_size))
