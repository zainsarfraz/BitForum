from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField(max_length=254,unique=True)
    name = models.TextField()
    password = models.TextField(max_length=15)
    status = models.TextField(max_length=250)
    profile_pic = models.ImageField(upload_to='')

    def __str__(self):
        return self.email

class Post(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    no_of_views = models.PositiveIntegerField(default=0)
    user_id = models.ForeignKey(User,related_name='post_author',on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Topic(models.Model):
    topic_name = models.CharField(max_length=50)

    def __str__(self):
        return self.topic_name

class Contains(models.Model):
    postId = models.ForeignKey(Post,related_name='contains',on_delete=models.CASCADE)
    topicId = models.ForeignKey(Topic,related_name='contains',on_delete=models.CASCADE)


class Upvote(models.Model):
    postId = models.ForeignKey(Post,related_name='upvote',on_delete=models.CASCADE)
    userId = models.ForeignKey(User,related_name='upvote',on_delete=models.CASCADE,default='')


class Downvote(models.Model):
    postId = models.ForeignKey(Post, related_name='downvote', on_delete=models.CASCADE)
    userId = models.ForeignKey(User, related_name='downvote', on_delete=models.CASCADE,default='')

class FollowersFollowings(models.Model):

    followerId = models.ForeignKey(User, related_name='follower', on_delete=models.CASCADE)
    followingId = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)


    def __str__(self):
        return str(self.followerId.email + " --> " + self.followingId.email)
# class Followings(models.Model):
#     userId = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
#     followingId = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE,null=True,blank=True)
#     topicId = models.ForeignKey(Topic, related_name='topic', on_delete=models.CASCADE,null=True,blank=True)


class TopicFollower(models.Model):
    followerId = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    topicId = models.ForeignKey(Topic,related_name='followedTopic',on_delete=models.CASCADE)

    def __str__(self):
        return self.followerId.email + " --- > " +self.topicId.topic_name

class Comment(models.Model):
    userId = models.ForeignKey(User,related_name='commentAuthor',on_delete=models.CASCADE)
    postId = models.ForeignKey(Post,related_name='on_post',on_delete=models.CASCADE)
    content = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    no_of_up = models.PositiveIntegerField(default=0)
    no_of_down = models.PositiveIntegerField(default=0)

class PostImage(models.Model):
    image = models.ImageField(upload_to='')
    postId = models.ForeignKey(Post,related_name='postImage',on_delete=models.CASCADE)

class Notification(models.Model):
    seen = models.BooleanField(default=False)
    reciever_id = models.ForeignKey(User,related_name='recieving_user',on_delete=models.CASCADE)
    sender_id = models.ForeignKey(User,related_name='sending_user',on_delete=models.CASCADE)
    postId = models.ForeignKey(Post,related_name='related_post',on_delete=models.CASCADE,default=None,null=True)
    type = models.TextField()

    def __str__(self):
        return str(self.sender_id) + " " +str(self.type) +" "+ str(self.reciever_id)