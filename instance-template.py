# Instance Template to define the properties for each VM
# The image and machine size are hardcoded. They could be parameterized


URL_BASE = 'https://www.googleapis.com/compute/v1/projects/'

# Every Python Template needs to have the GenerateConfig() or generate_config()
# method
# This method is called by DM in expansion and must return either:
#    - the yaml format required by DM
#    - a python dictionary representing the yaml (this is more efficient)


def GenerateConfig(context):
  """Generates the configuration."""

  # Create a dictionary which represents the resources
  # (Intstance Template, IGM, etc.)
  resources = [
      {
          'name': context.env['name'] + '-template',
          'type': 'compute.v1.instanceTemplate',
          'properties': {
              'properties': {
                  'machineType':
                      'n1-standard-2',
                  'tags':{
                    'items': ['http-server']  
                  },
                  'networkInterfaces': [{
                      'subnetwork':
                          URL_BASE + context.env['project'] +
                          context.properties['subnetwork'],
                      'accessConfigs': [{
                          'name': 'External NAT',
                          'type': 'ONE_TO_ONE_NAT'
                      }]
                  }],
                  'disks': [{
                      'deviceName': 'boot',
                      'type': 'PERSISTENT',
                      'boot': True,
                      'autoDelete': True,
                      'initializeParams': {
                          'sourceImage':
                              URL_BASE + context.env['project'] +
                              context.properties['sourceImage']
                      }
                  }]
              }
          }
      },
  ]
  return {'resources': resources}
