class SocialMediaPost:
    def __init__(self, author :str, content: str):
        self.likes = 0
        self.author=author
        self.content=content

    def like(self):
        self.likes += 1

    def __str__(self):
        return f"{self.author} says: '{self.content}' (👍 {self.likes})"
    
post = SocialMediaPost("CodeNewbie", "Learning OOP in Python today!")
post.like()
post.like()

print(post)
#print("👍")