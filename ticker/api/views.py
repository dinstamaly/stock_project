from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import (
    TickerSerializer,
    HistorySerializer,
)
from ..models import Ticker, History
from ..pd_populate import get_yahoo_ticker_data


class TickerViewSet(viewsets.ModelViewSet):
    queryset = Ticker.objects.all()
    serializer_class = TickerSerializer

    @action(detail=True, methods=['POST'])
    def get_history(self, request, pk=None):
        obj = Ticker.objects.get(id=pk)
        t_obj = History.objects.filter(ticker=obj.id).first()

        if t_obj:
            history = History.objects.filter(ticker=obj.id)
            serializer = HistorySerializer(history, many=True)
            response = serializer.data
            return Response(response, status=status.HTTP_200_OK)
        else:

            data = get_yahoo_ticker_data(ticker=obj.title)
            print(data)
            if data is not None:
                for vals in data.itertuples():
                    history = History(
                            ticker=obj,
                            datetime=vals[1],
                            open=vals[2],
                            high=vals[3],
                            low=vals[4],
                            close=vals[5],
                            adj_close=vals[5],
                            volume=vals[6]
                    )
                    history.save()
                history = History.objects.filter(ticker=obj.id)
                serializer = HistorySerializer(history, many=True)
                response = {
                    'message': 'created', 'result': serializer.data
                }
                return Response(response, status=status.HTTP_200_OK)
            else:
                response = {
                    'message': 'has no enough data'
                }
                return Response(response, status=status.HTTP_200_OK)


class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer

    def update(self, request, *args, **kwargs):
        response = {'message': 'You can not provide the operation'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        response = {'message': 'You can not provide the operation'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

