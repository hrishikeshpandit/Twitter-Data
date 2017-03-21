from twython import Twython
import json
APP_KEY='RRhgPJ9*******l6mJ2zgK' #enter your own account details from apps.twitter.com here all the secret keys are scrambled :)
APP_SECRET= 'zV*******IbcqfneNWEtsGikr8H6kZStymt8vR9IvD5zon4'
OAUTH_TOKEN= '20005**/*/*/*/**YhhizaUE1lYlmvsWwLKCTPkFyiQ'
OAUTH_TOKEN_SECRET= 'rZiM/*//*/*/*/*/*//*w33nxKI1UFmdquqJV424';
twitter = Twython(APP_KEY, APP_SECRET,OAUTH_TOKEN, OAUTH_TOKEN_SECRET);
#twitter.verify_credentials();
file1=open("a.txt","a")
#twitter.update_status(status='See how easy using Twython is!')
count=0;
while(1):
   print("Enter your option from the menu \n 1: UPDATE STATUS \n 2:GET TIME LINE \n 3: SEARCH FOR A TWEET \n 4: POST A PHOTO  \n 5: EXIT ")
   u=input();
   count=count+1
   if u==1 :
       print("enter the status that you would want to post/tweet");
       t=raw_input(":")
       twitter.update_status(status=t);
       file1.write("\nTweet Number ")
       file1.write(str(count)+"\n")
       file1.write(t);
               
   elif u==2 :
         print("The time line is as follows")
         timeline=twitter.get_home_timeline();
         file1.write("\nTwitter TimeLine Obtained ")
         file1.write(str(count)+"\n")
         for tweetdata in timeline:
                print tweetdata['text']
                #file1.write(tweetdata['text']);    
   elif u==3:
         
         print("enter the #tag OR SUBJECT YOU WOULFD LIKE TO SEARCH");
         s=raw_input(":")
         file1.write("\nTwitter Search Results ")
         file1.write(str(count)+"\n")
         results = twitter.cursor(twitter.search, q=s)
         for result in results:
                 print result['text']
         
         #file1.write(s);    
   elif u==4 :
        print("photo posted")
        photo = open('/home/hrishikesh/Downloads/index.jpg', 'rb')
        response = twitter.upload_media(media=photo)
        twitter.update_status(status='Checkout this cool image!', media_ids=[response['media_id']])
         
   elif u==5 :
        file1.close()
        print("Exiting the Twitter API \n Thank you for using the services\n")
        exit();
       
  
    #print("Enter your option again");    