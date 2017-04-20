from django.db import models



class Equipment(models.Model):

    ABLINE_CHOICES = (
        ('A', 'A线'),
        ('B', 'B线')
    )

    class Meta:
        verbose_name = "设备"
        verbose_name_plural = "设备"

    name = models.CharField('名称',max_length = 30)
    workshop = models.IntegerField('车间', default = 1)
    seat = models.IntegerField('机位', default = 1)
    abline = models.CharField('AB线', choices = ABLINE_CHOICES, max_length = 1)
    add_time = models.DateTimeField('添加时间', auto_now_add=True)
    remarks = models.TextField('备注信息')

    def __str__(self):
        return self.name

class Point(models.Model):

    DIRECTION_CHOICES = (
        ('v', '垂直'),   # 垂直
        ('a', '轴向'),      # 轴向
        ('r', '径向'),     # 径向
    )

    class Meta:
        verbose_name = "测点"
        verbose_name_plural = "测点"

    equipment = models.ForeignKey(Equipment)
    number = models.CharField('测点编号', max_length = 10)
    level = models.IntegerField('级数', default = 1)
    direction = models.CharField('方向', choices = DIRECTION_CHOICES, max_length = 1)
    warning_line = models.FloatField('警告线')
    danger_line = models.FloatField('危险线')
    add_time = models.DateTimeField('添加时间', auto_now_add = True)

    def __str__(self):
        return '%d' % self.id


class Data(models.Model):

    class Meta:
        verbose_name = "数据"
        verbose_name_plural = "数据"

    equipment = models.ForeignKey(Equipment)
    point = models.ForeignKey(Point)
    amplitude = models.FloatField('振幅')
    add_time = models.DateTimeField('添加时间')
    def __str__(self):
        return u'%s' % self.id


