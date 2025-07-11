
# data_manager/admin.py

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin # ★追加★
from .models import ExperimentData

# ExperimentData モデルを管理サイトに登録
class ExperimentDataAdmin(ImportExportModelAdmin, admin.ModelAdmin): # ★変更★
    # 管理サイトの一覧画面に表示するフィールド
    list_display = ('test_date', 'mix_name', 'mix_amount_1', 'mix_amount_2', 'test_result')
    # 検索ボックスで検索可能にするフィールド
    search_fields = ('mix_name',)
    # フィルタリングできるフィールド
    list_filter = ('test_date', 'mix_name',)
    # 詳細画面でのフィールドの表示順序 (optional)
    # fields = ('test_date', 'mix_name', 'mix_amount_1', 'mix_amount_2', 'test_result')

admin.site.register(ExperimentData, ExperimentDataAdmin) # ★追加★