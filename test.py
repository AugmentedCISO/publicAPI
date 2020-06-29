from aciso import AugmentedCISOApi
from aciso.metric import Metric, MetricList



api = AugmentedCISOApi(api_key='nhsBfu8GbFlOo1rfDWWc', is_dev=True)
print(api.get_access_url('me'))
print(api.get_key_information())
print(api.get_metrics_list())
metric_list = api.get_metrics_list()
print(api.get_metrics_perimeter_list('P1_1'))

m = Metric(perimeter='gdjkh', metric='dgfjiklm', value='10')
print(m.value)

print(api.get_metrics_perimeter_one(perimeter='P1_1', metric='M006_1').value)


metric_list = MetricList()


metric = Metric(perimeter='P1_1', metric='M006_1', value=1)
metric_list.append_metric(metric)
print(api.put_metrics(metric_list))


metric = Metric(metric='M006_1', value=5)
metric_list.append_metric(metric)
print(api.put_metrics_perimeter(metric_list, 'P1_1'))



print(api.get_metrics_perimeter_one(perimeter='P1_1', metric='M006_1').value)
metric = Metric(perimeter='P1_1', metric='M006_1', value=88)
api.put_one_metric(metric)
print(api.get_metrics_perimeter_one(perimeter='P1_1', metric='M006_1').value)
api.delete_one_metric(metric)
print(api.get_metrics_perimeter_one(perimeter='P1_1', metric='M006_1').value)
