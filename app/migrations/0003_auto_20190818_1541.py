# Generated by Django 2.1.2 on 2019-08-18 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190803_1457'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='i_01_fossil_ID',
        ),
        migrations.RemoveField(
            model_name='item',
            name='i_02_category_CD',
        ),
        migrations.RemoveField(
            model_name='item',
            name='i_03_fossil_name',
        ),
        migrations.RemoveField(
            model_name='item',
            name='i_04_nickname',
        ),
        migrations.RemoveField(
            model_name='item',
            name='i_05_binomen',
        ),
        migrations.RemoveField(
            model_name='item',
            name='i_06_kingdom',
        ),
        migrations.RemoveField(
            model_name='item',
            name='i_07_phylum',
        ),
        migrations.RemoveField(
            model_name='item',
            name='i_08_subphylum',
        ),
        migrations.RemoveField(
            model_name='item',
            name='i_09_lass_nm',
        ),
        migrations.RemoveField(
            model_name='item',
            name='i_10_subclass',
        ),
        migrations.RemoveField(
            model_name='item',
            name='i_11_infraclass',
        ),
        migrations.RemoveField(
            model_name='item',
            name='i_12_superorder',
        ),
        migrations.RemoveField(
            model_name='item',
            name='i_13_order',
        ),
        migrations.RemoveField(
            model_name='item',
            name='i_14_suborder',
        ),
        migrations.RemoveField(
            model_name='item',
            name='i_15_infraorder',
        ),
        migrations.RemoveField(
            model_name='item',
            name='i_16_group',
        ),
        migrations.RemoveField(
            model_name='item',
            name='i_17_superfamily',
        ),
        migrations.RemoveField(
            model_name='item',
            name='i_18_family',
        ),
        migrations.RemoveField(
            model_name='item',
            name='i_19_subfamily',
        ),
        migrations.RemoveField(
            model_name='item',
            name='i_20_genus',
        ),
        migrations.RemoveField(
            model_name='item',
            name='i_21_subgenus',
        ),
        migrations.RemoveField(
            model_name='item',
            name='i_22_part',
        ),
        migrations.RemoveField(
            model_name='item',
            name='i_23_part_size',
        ),
        migrations.RemoveField(
            model_name='item',
            name='i_24_estimate_length',
        ),
        migrations.RemoveField(
            model_name='item',
            name='i_25_product_CD',
        ),
        migrations.RemoveField(
            model_name='item',
            name='i_26_zip_CD',
        ),
        migrations.RemoveField(
            model_name='item',
            name='i_27_prefecture',
        ),
        migrations.RemoveField(
            model_name='item',
            name='i_28_city',
        ),
        migrations.RemoveField(
            model_name='item',
            name='i_29_stratum',
        ),
        migrations.RemoveField(
            model_name='item',
            name='i_30_discovery_date',
        ),
        migrations.RemoveField(
            model_name='item',
            name='i_31_discoverer',
        ),
        migrations.RemoveField(
            model_name='item',
            name='i_32_discoverer_job',
        ),
        migrations.RemoveField(
            model_name='item',
            name='i_33_announced_flag',
        ),
        migrations.RemoveField(
            model_name='item',
            name='i_34_announced_date',
        ),
        migrations.RemoveField(
            model_name='item',
            name='i_35_reporter',
        ),
        migrations.RemoveField(
            model_name='item',
            name='i_36_reporter_job',
        ),
        migrations.RemoveField(
            model_name='item',
            name='i_37_geologic_CD',
        ),
        migrations.RemoveField(
            model_name='item',
            name='i_38_eon',
        ),
        migrations.RemoveField(
            model_name='item',
            name='i_39_era',
        ),
        migrations.RemoveField(
            model_name='item',
            name='i_40_period',
        ),
        migrations.RemoveField(
            model_name='item',
            name='i_41_epoch',
        ),
        migrations.RemoveField(
            model_name='item',
            name='i_42_age',
        ),
        migrations.RemoveField(
            model_name='item',
            name='i_43_year_ago',
        ),
        migrations.RemoveField(
            model_name='item',
            name='i_44_outline',
        ),
        migrations.RemoveField(
            model_name='item',
            name='i_45_details',
        ),
        migrations.RemoveField(
            model_name='item',
            name='i_46_collect_museum',
        ),
        migrations.RemoveField(
            model_name='item',
            name='i_47_sumple_number',
        ),
        migrations.RemoveField(
            model_name='item',
            name='i_48_works_cited1',
        ),
        migrations.RemoveField(
            model_name='item',
            name='i_49_works_cited2',
        ),
        migrations.RemoveField(
            model_name='item',
            name='i_50_works_cited3',
        ),
        migrations.RemoveField(
            model_name='item',
            name='i_51_attach1',
        ),
        migrations.RemoveField(
            model_name='item',
            name='i_52_attach1_comment',
        ),
        migrations.RemoveField(
            model_name='item',
            name='i_53_attach2',
        ),
        migrations.RemoveField(
            model_name='item',
            name='i_54_attach2_comment',
        ),
        migrations.RemoveField(
            model_name='item',
            name='i_55_attach3',
        ),
        migrations.RemoveField(
            model_name='item',
            name='i_56_attach3_comment',
        ),
        migrations.RemoveField(
            model_name='item',
            name='i_57_last_update',
        ),
        migrations.AddField(
            model_name='item',
            name='col01_fossil_ID',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='ID'),
        ),
        migrations.AddField(
            model_name='item',
            name='col02_category_CD',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='分類CD'),
        ),
        migrations.AddField(
            model_name='item',
            name='col03_fossil_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='名称'),
        ),
        migrations.AddField(
            model_name='item',
            name='col04_nickname',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='愛称'),
        ),
        migrations.AddField(
            model_name='item',
            name='col05_binomen',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='学名'),
        ),
        migrations.AddField(
            model_name='item',
            name='col06_kingdom',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='界'),
        ),
        migrations.AddField(
            model_name='item',
            name='col07_phylum',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='門'),
        ),
        migrations.AddField(
            model_name='item',
            name='col08_subphylum',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='亜門'),
        ),
        migrations.AddField(
            model_name='item',
            name='col09_lass_nm',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='綱'),
        ),
        migrations.AddField(
            model_name='item',
            name='col10_subclass',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='亜綱'),
        ),
        migrations.AddField(
            model_name='item',
            name='col11_infraclass',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='下綱'),
        ),
        migrations.AddField(
            model_name='item',
            name='col12_superorder',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='上目'),
        ),
        migrations.AddField(
            model_name='item',
            name='col13_order',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='目'),
        ),
        migrations.AddField(
            model_name='item',
            name='col14_suborder',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='亜目'),
        ),
        migrations.AddField(
            model_name='item',
            name='col15_infraorder',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='下目'),
        ),
        migrations.AddField(
            model_name='item',
            name='col16_group',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='類'),
        ),
        migrations.AddField(
            model_name='item',
            name='col17_superfamily',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='上科'),
        ),
        migrations.AddField(
            model_name='item',
            name='col18_family',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='科'),
        ),
        migrations.AddField(
            model_name='item',
            name='col19_subfamily',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='亜科'),
        ),
        migrations.AddField(
            model_name='item',
            name='col20_genus',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='属'),
        ),
        migrations.AddField(
            model_name='item',
            name='col21_subgenus',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='亜属'),
        ),
        migrations.AddField(
            model_name='item',
            name='col22_part',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='発掘部位'),
        ),
        migrations.AddField(
            model_name='item',
            name='col23_part_size',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='部位サイズ'),
        ),
        migrations.AddField(
            model_name='item',
            name='col24_estimate_length',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='推定体長'),
        ),
        migrations.AddField(
            model_name='item',
            name='col25_product_CD',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name='産地CD'),
        ),
        migrations.AddField(
            model_name='item',
            name='col26_zip_CD',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='郵便番号'),
        ),
        migrations.AddField(
            model_name='item',
            name='col27_prefecture',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='産地(県)'),
        ),
        migrations.AddField(
            model_name='item',
            name='col28_city',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='産地(市)'),
        ),
        migrations.AddField(
            model_name='item',
            name='col29_stratum',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='地層'),
        ),
        migrations.AddField(
            model_name='item',
            name='col30_discovery_date',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='発見年'),
        ),
        migrations.AddField(
            model_name='item',
            name='col31_discoverer',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='発見者'),
        ),
        migrations.AddField(
            model_name='item',
            name='col32_discoverer_job',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='発見者職業'),
        ),
        migrations.AddField(
            model_name='item',
            name='col33_announced_flag',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='発表区分'),
        ),
        migrations.AddField(
            model_name='item',
            name='col34_announced_date',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='発表年'),
        ),
        migrations.AddField(
            model_name='item',
            name='col35_reporter',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='報告者'),
        ),
        migrations.AddField(
            model_name='item',
            name='col36_reporter_job',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='報告者職業'),
        ),
        migrations.AddField(
            model_name='item',
            name='col37_geologic_CD',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='地質年代CD'),
        ),
        migrations.AddField(
            model_name='item',
            name='col38_eon',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='累代'),
        ),
        migrations.AddField(
            model_name='item',
            name='col39_era',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='代'),
        ),
        migrations.AddField(
            model_name='item',
            name='col40_period',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='紀'),
        ),
        migrations.AddField(
            model_name='item',
            name='col41_epoch',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='世'),
        ),
        migrations.AddField(
            model_name='item',
            name='col42_age',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='期'),
        ),
        migrations.AddField(
            model_name='item',
            name='col43_year_ago',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='年代'),
        ),
        migrations.AddField(
            model_name='item',
            name='col44_outline',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='概要'),
        ),
        migrations.AddField(
            model_name='item',
            name='col45_details',
            field=models.TextField(blank=True, null=True, verbose_name='詳細'),
        ),
        migrations.AddField(
            model_name='item',
            name='col46_collect_museum',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='所蔵館'),
        ),
        migrations.AddField(
            model_name='item',
            name='col47_sumple_number',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='標本番号'),
        ),
        migrations.AddField(
            model_name='item',
            name='col48_works_cited1',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='参考文献1'),
        ),
        migrations.AddField(
            model_name='item',
            name='col49_works_cited2',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='参考文献2'),
        ),
        migrations.AddField(
            model_name='item',
            name='col50_works_cited3',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='参考文献3'),
        ),
        migrations.AddField(
            model_name='item',
            name='col51_attach1',
            field=models.FileField(blank=True, max_length=255, null=True, upload_to='uploads/%Y/%m/%d/', verbose_name='添付データ1'),
        ),
        migrations.AddField(
            model_name='item',
            name='col52_attach1_comment',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='添付データ1コメント'),
        ),
        migrations.AddField(
            model_name='item',
            name='col53_attach2',
            field=models.FileField(blank=True, max_length=255, null=True, upload_to='uploads/%Y/%m/%d/', verbose_name='添付データ2'),
        ),
        migrations.AddField(
            model_name='item',
            name='col54_attach2_comment',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='添付データ2コメント'),
        ),
        migrations.AddField(
            model_name='item',
            name='col55_attach3',
            field=models.FileField(blank=True, max_length=255, null=True, upload_to='uploads/%Y/%m/%d/', verbose_name='添付データ3'),
        ),
        migrations.AddField(
            model_name='item',
            name='col56_attach3_comment',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='添付データ3コメント'),
        ),
        migrations.AddField(
            model_name='item',
            name='col57_last_update',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='更新日'),
        ),
    ]
