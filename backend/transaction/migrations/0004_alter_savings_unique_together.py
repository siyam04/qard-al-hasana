# Generated by Django 4.1.2 on 2023-05-03 01:00

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("peoples", "0002_alter_member_team_delete_team"),
        ("transaction", "0003_savings_transaction_type"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="savings",
            unique_together={("member", "date", "transaction_type")},
        ),
    ]
