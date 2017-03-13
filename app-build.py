"""Build Application Tier from Components"""

def GenerateConfig(context):

  resources = [{
    'name': ''.join([context.env['name'], '-template']),
    'type': instance-template.py,
    'properties': {
       'description': ''.join(['Instance Template for ', context.properties['description']]),
       'machineType': context.properties['machineType'],
       'network': context.properties['network'],
       'sourceImage': context.properties['sourceImage'],
       'diskSize': context.properties['diskSize'],
       'tags': context.properties['tags'],
    }
}, {
    'name': ''.join([context.env['name'], '-ig']),
    'type': managed-instance-group.py,
    'properties': {
       'description': ''.join(['Managed Instance Group for ', context.properties['description']]),
       'instanceTemplate': ''.join(['$ref.', context.env['name'], '-template.selflink']),
       'region': context.properties['region']
    }
},
   {
   'name': ''.join([context.env['name'], '-as']),
    'type': autoscaler.py,
    'properties': {
       'description': ''.join(['Autoscaling for ', context.properties['description']]),
       'managedInstanceGroup': ''.join(['$ref.', context.env['name'], '-ig.selflink']),
      'region': context.properties['region'],
      'minSize': context.properties['minSize'],
      'maxSize': context.properties['maxSize'],
      'cpuUtil': context.properties['cpuUtil']
  }
}
]
return {'resources': resources}
