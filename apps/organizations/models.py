from django.db import models

from apps.users.models import BaseModel


# 城市
class City(BaseModel):
    name = models.CharField(max_length=20, verbose_name="城市名")
    desc = models.CharField(max_length=200, verbose_name="描述")

    class Meta:
        verbose_name = "城市"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 课程机构
class CourseOrg(BaseModel):
    name = models.CharField(max_length=50, verbose_name="机构名称")
    desc = models.TextField(verbose_name="描述")
    tag = models.CharField(default="全国知名", verbose_name="机构类型", max_length=10)
    category = models.CharField(default="pxjg", verbose_name="机构类别", max_length=4,
                                choices=(("pxjg", "培训机构"), ("gr", "个人"), ("gx", "高校")))
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏数")
    image = models.ImageField(upload_to="org/%Y/%m", verbose_name="logo", max_length=100)
    students = models.IntegerField(default=0, verbose_name="学习人数")
    address = models.CharField(max_length=50, verbose_name="机构地址")
    courses_nums = models.IntegerField(default=0, verbose_name="课程数")
    is_auth = models.BooleanField(default=False, verbose_name="是否认证")
    is_gold = models.BooleanField(default=False, verbose_name="是否金牌")
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="所在城市")

    class Meta:
        verbose_name = "课程机构"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    # # 普通方法取课程信息
    # def courses(self):
    #     # 若把引用发在前面，会因为机构和课程两应用循环引用报错
    #     from apps.courses.models import Course
    #     courses = Course.objects.filter(course_org=self)
    #     return courses

    # course表反向取
    def courses(self):
        courses = self.course_set.filter(is_classics=True)[:3]  # 选前三个经典课程
        return courses


class Teacher(BaseModel):
    org = models.ForeignKey(CourseOrg, on_delete=models.CASCADE, verbose_name="所属机构")
    name = models.CharField(max_length=50, verbose_name="教师名")
    work_years = models.IntegerField(default=0 , verbose_name="工作年限")
    work_company = models.CharField(max_length=50 ,verbose_name="就职公司")
    work_position = models.CharField(max_length=50, verbose_name="公司职位")
    points = models.CharField(max_length=50, verbose_name="教学特长")
    click_num = models.IntegerField(default=0, verbose_name="点击数")
    fav_num = models.IntegerField(default=0, verbose_name="收藏数")
    age = models.IntegerField(default=18, verbose_name="年龄")
    image = models.ImageField(upload_to="teacher/%Y/m", verbose_name="头像", max_length=100)

    class Meta:
        verbose_name = "课程讲师"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
