from django.db import models



class Equipment(models.Model):

    class Meta:
        verbose_name = "设备"
        verbose_name_plural = "设备"

    name = models.CharField('名称',max_length = 30)
    point_number = models.IntegerField('测点数', default = 1)
    seat = models.IntegerField('机位', default = 1)
    device = models.CharField('装置', max_length =30)
    add_time = models.DateTimeField('添加时间', auto_now_add=True)
    remarks = models.TextField('备注信息')

    def __str__(self):
        return self.name

class Data(models.Model):

    class Meta:
        verbose_name = "数据"
        verbose_name_plural = "数据"

    x = models.FloatField('x坐标')
    y = models.FloatField('y坐标')
    equipment = models.ForeignKey(Equipment)
    point = models.IntegerField('测点', default = 1)



    def __str__(self):
        return u'%s' % self.id


