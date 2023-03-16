import datetime
import traceback
import time

from instagrapi import Client
from instagrapi import types

IG_USERNAME = "nextgengenie"
IG_PASSWORD = "botjdid99"

cl = Client()
CURRENT_COMMENTS = []
CURRENT_COMMENTS_TEXT = []
CURRENT_PROMPT = ""


def login():
    global cl
    cl.login(IG_USERNAME, IG_PASSWORD)


def getLastMediaComments():
    global CURRENT_COMMENTS
    lastMedia = cl.user_medias(cl.user_id, amount=1)[0]
    print("Last media is: ", lastMedia)
    comments = cl.media_comments(lastMedia.id)
    comments = sorted(comments, key=sortingFunction)
    CURRENT_COMMENTS = comments
    return treatComments(comments)


def getUsersTags():
    users_ids = []
    txtLength = 0
    for c in CURRENT_COMMENTS:
        if txtLength + len(c.text) < 400:
            if c.user.pk not in users_ids:
                users_ids.append(c.user.pk)
                txtLength += len(c.text)

    users_tags = []
    xx = .9
    yy = .9
    for pk in users_ids:
        usr_short = cl.user_info(pk)
        user_tag = types.Usertag(user=usr_short, x=xx, y=yy)
        users_tags.append(user_tag)
        xx *= .9
        yy *= .9

    return users_tags


def treatComments(comments):
    global CURRENT_COMMENTS_TEXT
    commentsText = [c.text for c in comments]
    CURRENT_COMMENTS_TEXT = commentsText
    return commentsText


def combineCommentsText(commentsText, charsLimit=360):
    return " ".join(commentsText)[:charsLimit]


def postNewMedia(imgPath):
    print("Image to post: ", imgPath)


def sortingFunction(comment):
    return comment.like_count * (datetime.datetime.now().timestamp() - comment.created_at_utc.timestamp()) / (
                24 * 60 * 60)


def getPrompt():
    global CURRENT_PROMPT
    try:
        cmts_text = getLastMediaComments()
        prompt_text = combineCommentsText(cmts_text)
        CURRENT_PROMPT = prompt_text
        print(prompt_text)
        return prompt_text
    except:
        traceback.print_exc()
        login()
        time.sleep(10)
        return getPrompt()


def newPost(imgPath, caption):
    cl.photo_upload(imgPath, caption, usertags=getUsersTags())


if __name__ == "__main__":
    login()
    cmtsText = getLastMediaComments()
    promptText = combineCommentsText(cmtsText)
    print(promptText)
