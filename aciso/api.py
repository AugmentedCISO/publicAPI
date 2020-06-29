import requests
from aciso.metric import get_metrics_list, put_metrics, MetricList, get_metric, Metric, put_one_metric, \
    delete_one_metric


class Api:
    def __init__(self, api_key: str, is_dev=False):
        self.url_prod = ''
        self.url_dev = 'http://localhost:5481/api/public/'

        self.api_url = self.url_prod
        if is_dev:
            self.api_url = self.url_dev

        self.is_dev = is_dev
        self.api_key = api_key

    def get_access_url(self, endpoint: str):
        return self.api_url + endpoint + '?api_key=' + self.api_key

    def get_key_information(self):
        r = requests.get(self.get_access_url('me'))

        if r.status_code is 200:
            response = (r.json())
            if response['ok']:
                response.pop('ok', None)
                return response
        return None

    def get_metrics_list(self):
        return get_metrics_list(self.get_access_url('metrics'))

    def get_metrics_perimeter_list(self, perimeter: str):
        return get_metrics_list(self.get_access_url('metrics/%s' % perimeter))

    def get_metrics_perimeter_one(self, perimeter: str, metric: str):
        return get_metric(self.get_access_url('metrics/%s/%s' % (perimeter, metric)))

    def put_metrics(self, metric_list: MetricList):
        return put_metrics(self.get_access_url('metrics'), metric_list)

    def put_metrics_perimeter(self, metric_list: MetricList, perimeter:str):
        return put_metrics(self.get_access_url('metrics/%s' % perimeter), metric_list)

    def put_one_metric(self, metric: Metric):
        return put_one_metric(self.get_access_url('metrics/%s/%s' % (metric.perimeter, metric.metric)), metric.value)

    def delete_one_metric(self, metric: Metric):
        return delete_one_metric(self.get_access_url('metrics/%s/%s' % (metric.perimeter, metric.metric)))