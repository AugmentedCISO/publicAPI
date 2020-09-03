##############################################################
# Project : AugmentedCISO Public API
# Author : EXCUBE (contact@excube.fr)
##############################################################

import json

import requests


class Metric:
    def __init__(self, metric: str, value, perimeter=''):
        self.perimeter = perimeter
        self.metric = metric
        self.value = value

    def data(self):
        return {
            "perimeter_id": self.perimeter,
            "metric_id": self.metric,
            "value": self.value,
        }

    def __str__(self):
        return 'METRIC %s / PERIMETER %s / VALUE %s' % (str(self.metric), str(self.perimeter), str(self.value))


class MetricList:
    def __init__(self):
        self.collection = []
        self.total = 0

    def append_metric(self, metric: Metric):
        self.collection.append(metric)
        self.total = len(self.collection)

    def filter_by(self, **kwargs):
        return [n for n in self.collection
                if all(getattr(n, k) == v for k, v in kwargs.items())]

    def first(self):
        return self.collection[0]

    def to_json(self):
        data = {
            "metrics": []
        }
        for metric in self.collection:
            data["metrics"].append(metric.data())
        return data

    def __str__(self):
        s = ''
        for m in self.collection:
            s += ' - ' + str(m) + '\n'
        return s


def get_metrics_list(url: str):
    r = requests.get(url)
    if r.status_code is 200:
        metric_list = MetricList()
        response = r.json()
        if response['ok']:
            response.pop('ok', None)
            for obj in response['objects']:
                new_metric = Metric(perimeter=obj['perimeter_id'], metric=obj['metric_id'], value=obj['value'])
                metric_list.append_metric(new_metric)
            return metric_list
    return None


def get_metric(url: str):
    r = requests.get(url)
    if r.status_code is 200:
        metric_list = MetricList()
        response = r.json()
        if response['ok']:
            response.pop('ok', None)
            for obj in response['objects']:
                new_metric = Metric(perimeter=obj['perimeter_id'], metric=obj['metric_id'], value=obj['value'])
            return new_metric
    return None


def put_metrics(url: str, metric_list: MetricList):
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}

    r = requests.put(url, data=json.dumps(metric_list.to_json()), headers=headers)
    if r.status_code is 200:
        resp = r.json()
        return resp
    return r.json()


def put_one_metric(url: str, value: int):
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}

    r = requests.put(url, data=json.dumps({"value": value}), headers=headers)
    print(r.json())
    if r.status_code is 200:
        resp = r.json()
        return resp
    return r.json()


def delete_one_metric(url: str):
    r = requests.delete(url)
    print(r.json())
    if r.status_code is 200:
        resp = r.json()
        return resp
    return r.json()
