# Create an Instance Template""

# Instance Template to define the properties for each VM in a managed
# instance group

# This will be used to build the Web and App Tiers

# Required to provide instance image

URL = 'https://www.googleapis.com/compute/v1/projects/'

def GenerateConfig(context):
# Generates the configuration."""

# Create a dictionary which represents the resources

  resources = [
      {
          'name': context.env['name'],
          'type': 'compute.v1.instanceTemplate',
          'properties': {
              'properties': {
                  'machineType': context.properties[‘machineType’],
                  'networkInterfaces': [{
                      'network': URL + context.properties['network'],
                      'accessConfigs': [{
                          'name': 'External NAT',
                          'type': 'ONE_TO_ONE_NAT'
                      }]
                  }],
                  'disks': [{
                      'deviceName': 'boot',
                      'type': 'PERSISTENT',
                      'boot': True,
                      'mode': 'READ_WRITE',
                      'autoDelete': True,
                      'initializeParams': {
                          'sourceImage':     
                              context.properties['sourceImage'],
                          'diskSizeGb':     
                              context.properties['diskSize']
                      }
                  }],
                  'tags': {
                      'items': context.properties['tags']  
                  }
              }
          }
      }
  ]
return {'resources': resources}:
