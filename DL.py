from tqdm import tqdm
import requests
import sys

dlFile = 'breakingBadS2dl.txt'

def dlEpisode(fileName, url):
    response = requests.get(url, stream=True)
    # Transfer Encoding = chunked so can't set progress bar yet. Fix coming soon
    # total_length = response.headers.get('content-length')
    print "Currently downloading URL", response.url
    with open(fileName, "wb") as handle:
        # dl = 0
        # totalLength = int(total_length)
        for data in tqdm(response.iter_content(chunk_size=4096)):
            # dl += 1
            handle.write(data)
            # done = int(50 * dl / total_length)
            # sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)))
            # sys.stdout.flush()
# Testing
# url = "http://play.xmovies8.tv/player_v3.php?tham=1477800766&lt=dr&li=85844&ty=sr&k=126a74d987fdf3a067fa71b0c99b65bded161eb36885b5a8dcf4f693e6672410b6f629652e778b5a99f1461848ddaac522079770cc3b217955bf3f92d0bb6d994d6da6c70c69af8aee0f2001bc9b1371&st=5b59af664b9f90b4d00f73cc3916bb66e89634c06ea7d1c0fe5bb9964e6a348f9268cee5b0e3f434dc502f91b7b072a7292e60a839ac2f21056bd4020ba0942705de3eeca245ae0f78251cbba9185268bee7044843ffba42d8666481002fe309ab7f37c906065221cd20f5304d530d75&q=0&key=b2bceaaa5898b7f17b88d3b657805cc2&download=BREAKING+BAD%3A+SEASON+2+%282009%29"
# dlEpisode("Episode 13", url)
with open(dlFile, 'r') as file:
    url = [line.strip() for line in file]
    for i in range(len(url)):
        print "This is DL", i
        fileName = "Episode", i
        dlEpisode(fileName, url)

