from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)  # 이름
    phone = models.CharField(max_length=20)  # 전화번호

    def __str__(self):
        return self.name


class ImageComponent(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='contact_images/')  # 이미지 파일 저장
    diary = models.TextField()  # 이미지 설명

    def __str__(self):
        return f"Image for {self.contact.name} - {self.diary[:20]}..."