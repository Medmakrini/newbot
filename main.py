import traceback

import dallEClient as dalle
import instaClient as ic
import random
import time
import traceback

captionsList = [
    "Welcome to NextGenGenie, your go-to source for creative content ideas! 💡 I'm excited to start this journey with you, and I can't wait to see what kind of amazing content we can create together. Whether you're looking for inspiration for your blog, Instagram page, or just some fun ideas to share with your friends, I'm here to help. So go ahead, leave a comment and tell me what kind of post you'd like to see next. Let's get creative! ✨                                   #contentcreation #genieinabottle #creativity #contentideas #nextgengenie"
    "Your comments today will shape our content tomorrow, so speak up and let's create something amazing together in our next post!                                   #AImarketing #AIstrategy #smartcontent #innovation #tech #digitaltransformation",
    "Comment now and influence what we post next. Your voice matters!                                 #AI #artificialintelligence #contentcreation #genieinabottle #creativity #contentideas #nextgengenie",
    "Shape our next post with your comments. Join the conversation now!                               #AI #artificialintelligence #chatgpt #graphicdesign #visualcontent #brandingtips #startuplife",
    "Be a part of our next post! Comment below and let your voice be heard.                           #socialmediastrategy #marketingtips #digitalmarketing #branding #brandidentity ",
    "Comment now to co-create incredible content. Your voice matters for our next post!               #AI #artificialintelligence   #contentcreation #contentideas #creativity #collaboration #inspiration #newbeginnings #instagramnewbie #nextgengenie #communitybuilding #creativecommunity "]

captionPrefix = "\n" + "-" * 30 + "\nChosen comments will be tagged on the next post (^_^)"

def sleeping(duration):
    ti = time.time()
    while time.time() < ti + duration:
        print("sleeping for another: ", (ti + duration - time.time()) / 60, " minutes")
        time.sleep(60)


if __name__ == '__main__':
    while True:
        try:
            prompt = ic.getPrompt()
            image_path = dalle.generate(promptText=prompt)
            caption = random.choice(captionsList) + captionPrefix
            ic.newPost(image_path, caption)
            ic.cl.logout()
            sleeping(4*3600)
        except:
            traceback.print_exc()
