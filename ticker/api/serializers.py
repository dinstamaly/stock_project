from rest_framework import serializers
from ticker.models import Ticker, History


class TickerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticker
        fields = (
            'id', 'title'
        )


class HistorySerializer(serializers.ModelSerializer):
    ticker = TickerSerializer(read_only=True)

    class Meta:

        model = History
        fields = (
            'id', 'ticker',
            'datetime', 'high',
            'low', 'close',
            'adj_close', 'volume'
        )
