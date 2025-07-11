
# data_manager/models.py

from django.db import models

class ExperimentData(models.Model):
    # 試験日: 日付型
    test_date = models.DateField(
        verbose_name='試験日'
    )
    # 配合名: 文字列型、最大200文字
    mix_name = models.CharField(
        max_length=200,
        verbose_name='配合名'
    )
    # 配合量1: 浮動小数点数型
    mix_amount_1 = models.FloatField(
        verbose_name='配合量1'
    )
    # 配合量2: 浮動小数点数型
    mix_amount_2 = models.FloatField(
        verbose_name='配合量2'
    )
    # 試験結果: 浮動小数点数型 (または必要に応じてCharFieldなど)
    test_result = models.FloatField(
        verbose_name='試験結果'
    )

    class Meta:
        # 管理サイトや表示でのモデル名を指定
        verbose_name = '実験データ'
        verbose_name_plural = '実験データ'
        # 試験日の新しい順に並べる
        ordering = ['-test_date']

    def __str__(self):
        # オブジェクトが文字列として表示されるときの表現
        return f"{self.test_date} - {self.mix_name}"