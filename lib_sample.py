##############################################################
# Project : AugmentedCISO Public API
# Author : EXCUBE (contact@excube.fr)
# This is a sample of how to use the AugmentedCISO API with the python library
# Full API documentation: https://api.augmentedciso.com/api/public/doc
##############################################################

from aciso import AugmentedCISOApi
from aciso.metric import Metric, MetricList

# Change these to match your needs
API_KEY = 'YOU_API_KEY'

# WARNING: this sample will change the current value of the specified metric!

# Instanciate API with key
api = AugmentedCISOApi(api_key=API_KEY)

print("# Key information (empty perimeter set implies access to all perimeters)")
print(api.get_key_information())
print()

print("# List of available metrics")
print(api.get_metrics_list())
print()

print("# List of metrics of a given perimeter")
selected_perimeter = input('Please type a perimeter identifier and press Enter\n')
print(api.get_metrics_perimeter_list(selected_perimeter))
print()

## single update

print("# Update metric value for one perimeter")
# Create a metric objet (to store a new value for a given metric and perimeter)
selected_perimeter = input('Please type a perimeter identifier and press Enter\n')
selected_metric = input('Please type a metric identifier you which to update and press Enter\n')
value = input('Please type a value\n')
try:
    value = int(value)
except:
    print("Value must be an integer")
    exit(0)

m = Metric(perimeter=selected_perimeter, metric=selected_metric, value=value)
print()

print("# Send the metric objet (this will update the current value to %d)" % (value))
input("Type Enter to proceed")
print(api.put_one_metric(m))

print("# Get current value (to check it was successfuly set)")
print(api.get_metrics_perimeter_one(perimeter=selected_perimeter, metric=selected_metric).value)
print()

## Bulk updates

# Create a MetricList objet (to store a list of metric objects)
metric_list = MetricList()
m1 = Metric(perimeter=selected_perimeter, metric=selected_metric, value=value)
metric_list.append_metric(m1)

print("# Send the MetricList objet (this will update all values)")
print(api.put_metrics(metric_list))
print()

print("# Get current value (to check it was successfuly updated)")
print(api.get_metrics_perimeter_one(perimeter=selected_perimeter, metric=selected_metric).value)
print()

print("# Send the MetricList objet (this will update all values for given perimeter)")
print(api.put_metrics_perimeter(metric_list, selected_perimeter))
print()

## Delete value
print("# Delete current valu for selected metric and perimeter")
input("Type Enter to proceed")
print(api.delete_one_metric(m1))

print("# Get current value (to check it was successfuly deleted)")
print(api.get_metrics_perimeter_one(perimeter=selected_perimeter, metric=selected_metric).value)
